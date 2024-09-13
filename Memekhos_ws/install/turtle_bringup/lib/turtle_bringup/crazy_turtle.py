#!/usr/bin/python3

from turtle_bringup.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist , Point ,TransformStamped , PointStamped
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler
from std_msgs.msg import Float64
from controller_interface.srv import SetParam
import time

import numpy as np

class Crazy_turtle(Node):
    def __init__(self):
        super().__init__('Crazy_turtle')
        self.spawn_turtle2_client = self.create_client(Spawn,'spawn_turtle')
        self.odom_publisher = self.create_publisher(Odometry, '/odom',10)           
        self.cmd_vel_pub = self.create_publisher(Twist,f'{self.get_namespace()}'+'cmd_vel',10)
        self.tf_boardcaster = TransformBroadcaster(self)
        self.create_subscription(Pose,f'{self.get_namespace()}'+'pose',self.pose_callback,10)
        self.create_subscription(Pose,'/crazy_pizza',self.cpizza_pose_callback,10)
        # self.create_subscription(Point,'/mouse_position',self.mouse_position_callback,10)    
        # self.create_subscription(PointStamped,'/clicked_point',self.rvis_click_position_callback,10)    
        self.spawn_pizza_client = self.create_client(GivePosition,'spawn_pizza')
        self.eat_pizza_client = self.create_client(Empty,f'{self.get_namespace()}'+'eat')
        # self.create_timer(0.01,self.timer_callback)
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.mouse_pose = np.array([0.0,0.0])
        self.rvis_pose = np.array([0.0,0.0])
        self.cpizza_pose = np.array([0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44
        time.sleep(10)
        self.spawn_turtle()
        self.eaten = 0

        self.kp_linear = 0.0
        self.kp_angular = 0.0
        self.kp = 0.8
        self.kp_a = 20.0
        self.set_param = np.array([0.8,20.0])

        self.declare_parameter('frequency', 10.0)
        self.frequency = self.get_parameter('frequency').get_parameter_value().double_value
        self.tim = 1.0/self.frequency
        self.create_timer(self.tim,self.timer_callback)

        # self.set_target_server = self.create_service( SetTarget, 'set_target' ,self.set_target_callback )
        self.set_param_server = self.create_service( SetParam, '/set_param' ,self.set_param_callback)
        #start a timer for publisher /noise
        # self.create_timer(self.tim,self.timer_callback)
        self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter,  kp_linear:{self.kp_linear}, kp_angular:{self.kp_angular}')
    

    def set_param_callback(self, request:SetParam.Request , response:SetParam.Response):
        self.kp = request.kp_linear.data
        self.kp_a = request.kp_angular.data
        # self.settarget_x = request.variance.data
        return response

    def cpizza_pose_callback(self,msg):
        self.cpizza_pose[0] = msg.x
        self.cpizza_pose[1] = msg.y
        self.spawn_pizza(self.cpizza_pose[0],self.cpizza_pose[1])
        # print(msg)
        print(self.cpizza_pose)

    def rvis_click_position_callback(self,msg):
        self.rvis_pose[0] = msg.point.x
        self.rvis_pose[1] = msg.point.y
        # self.spawn_pizza(self.rvis_pose[0],self.rvis_pose[1])
        # print(self.rvis_pose)



    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_client.call_async(eat_request)

    def  spawn_turtle(self):
        position_re = Spawn.Request()
        position_re.x = 0.5
        position_re.y = 0.5
        self.spawn_turtle2_client.call_async(position_re)


    def  spawn_pizza(self,x,y):
        if(self.eaten == 0):
            position_request = GivePosition.Request()
            position_request.x = x
            position_request.y = y
            self.target_x = x
            self.target_y = y
            self.spawn_pizza_client.call_async(position_request)
        else:
            pass

    def mouse_position_callback(self,msg):
        self.mouse_pose[0] = msg.x
        self.mouse_pose[1] = msg.y
        # self.spawn_pizza(self.mouse_pose[0],self.mouse_pose[1])
        # print(msg)
        # print(self.mouse_pose)
        
    def cmdvel(self,v,w):
        msg =  Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        

    def pose_callback(self,msg):
        # print(msg)
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta
        # print(self.robot_pose)
        
        # odom_msg.twist.twist.angular

    def timer_callback(self):
        now_x = self.robot_pose[0]
        now_y = self.robot_pose[1]
        diff_x = self.target_x - now_x 
        diff_y = self.target_y - now_y 
        distance = np.sqrt((diff_x**2)+(diff_y**2))
        diff_theta = np.arctan(diff_y/diff_x) - self.robot_pose[2]
        # use_theta = np.arctan2(np.sin(diff_theta),np.cos(diff_theta))
        use_theta = np.arctan2(diff_y,diff_x)  - self.robot_pose[2]
        # print(self.robot_pose)
        # print(self.mouse_pose)
        # print(diff_x)
        # print(diff_y)
        # print(np.arctan(diff_y/diff_x))
        # print(diff_theta)
        # print(distance)
        # print(use_theta)
        # vx = 0.2*distance
        # vx = 0.8*distance
        # wz = 20*use_theta
        wz = self.kp_a*use_theta
        # if(diff_x < 0):
        #     wz = -2*use_theta
        # else:
        #     wz = 2*use_theta
        # wz = 0.2*diff_theta
        if(distance < 1):
            self.eat_pizza()
            self.eaten = 0
            vx = 0.0
        else:
            self.eaten = 1
            vx = self.kp*distance
        self.cmdvel(vx,wz)
        

def main(args=None):
    rclpy.init(args=args)
    node = Crazy_turtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
