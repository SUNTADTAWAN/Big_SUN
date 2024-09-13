#!/usr/bin/python3

from lecture2.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist , Point ,TransformStamped
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler

import numpy as np


class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.odom_publisher = self.create_publisher(Odometry, '/odom',10)           
        self.cmd_vel_pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self.tf_boardcaster = TransformBroadcaster(self)
        self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.create_subscription(Point,'/mouse_position',self.mouse_position_callback,10)        
        self.spawn_pizza_client = self.create_client(GivePosition,'spawn_pizza')
        self.eat_pizza_client = self.create_client(Empty,'/turtle1/eat')
        self.create_timer(0.01,self.timer_callback)
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.mouse_pose = np.array([0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44

    

    def eat_pizza(self):
        eat_request = Empty.Request()
        self.eat_pizza_client.call_async(eat_request)

    def  spawn_pizza(self,x,y):
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        self.spawn_pizza_client.call_async(position_request)

    def mouse_position_callback(self,msg):
        self.mouse_pose[0] = msg.x
        self.mouse_pose[1] = msg.y
        self.spawn_pizza(self.mouse_pose[0],self.mouse_pose[1])
        self.target_x = self.mouse_pose[0]
        self.target_y = self.mouse_pose[1]
        # print(msg)
        print(self.mouse_pose)
        
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
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "robot"

        odom_msg.pose.pose.position.x = self.robot_pose[0]
        odom_msg.pose.pose.position.y = self.robot_pose[1]

        q = quaternion_from_euler(0,0,self.robot_pose[2])
        odom_msg.pose.pose.orientation.x = q[0]
        odom_msg.pose.pose.orientation.y = q[1]
        odom_msg.pose.pose.orientation.z = q[2]
        odom_msg.pose.pose.orientation.w = q[3]

        self.odom_publisher.publish(odom_msg)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'robot'

        t.transform.translation.x = self.robot_pose[0]
        t.transform.translation.y = self.robot_pose[1]
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_boardcaster.sendTransform(t) 

        # odom_msg.twist.twist.angular

    def timer_callback(self):
        now_x = self.robot_pose[0]
        now_y = self.robot_pose[1]
        diff_x = self.target_x - now_x 
        diff_y = self.target_y - now_y 
        distance = np.sqrt((diff_x**2)+(diff_y**2))
        diff_theta = np.arctan(diff_y/diff_x) - self.robot_pose[2]
        use_theta = np.arctan2(np.sin(diff_theta),np.cos(diff_theta))
        # use_theta = np.arctan2(diff_y,diff_x)
        # print(self.robot_pose)
        # print(self.mouse_pose)
        print(diff_x)
        print(diff_y)
        # print(np.arctan(diff_y/diff_x))
        # print(diff_theta)
        # print(distance)
        # print(use_theta)
        # vx = 0.2*distance
        vx = 0.3*distance
        if(diff_x < 0):
            wz = -0.7*use_theta
        else:
            wz = 0.7*use_theta
        # wz = 0.2*diff_theta

        self.cmdvel(vx,wz)
        self.eat_pizza()

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
