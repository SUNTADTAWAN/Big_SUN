#!/usr/bin/python3

from turtle_bringup.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist , Point ,TransformStamped , PointStamped
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler

import numpy as np


class DummyNode(Node):
    def __init__(self):
        super().__init__('dummy_node')
        self.odom_publisher = self.create_publisher(Odometry, '/odom1',10)
        self.odom_publisher2 = self.create_publisher(Odometry, '/odom2',10)
        self.odom_pub         
        self.tf_boardcaster = TransformBroadcaster(self)
        self.create_subscription(Pose,'/turtle1/pose',self.pose_callback,10)
        self.create_subscription(Pose,'/turtle2/pose',self.pose2_callback,10)
        self.create_timer(0.01,self.timer_callback)
        self.robot_pose = np.array([0.0,0.0,0.0])
        self.robot2_pose = np.array([0.0,0.0,0.0])
        self.target_x = 5.44
        self.target_y = 5.44

    def odom_pub(self,msg,turtle_name,child_frame):
        odom_msg = Odometry()
        odom_msg.header.stamp = self.get_clock().now().to_msg()
        odom_msg.header.frame_id = turtle_name
        odom_msg.child_frame_id = child_frame

        odom_msg.pose.pose.position.x = msg[0]-5.0
        odom_msg.pose.pose.position.y = msg[1]-5.0

        q = quaternion_from_euler(0,0,msg[2])
        odom_msg.pose.pose.orientation.x = q[0]
        odom_msg.pose.pose.orientation.y = q[1]
        odom_msg.pose.pose.orientation.z = q[2]
        odom_msg.pose.pose.orientation.w = q[3]

        if(child_frame == "turtle1"):
            self.odom_publisher.publish(odom_msg)
        else:
            self.odom_publisher2.publish(odom_msg)

        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = turtle_name
        t.child_frame_id = child_frame

        t.transform.translation.x = msg[0]-5.0
        t.transform.translation.y = msg[1]-5.0
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        self.tf_boardcaster.sendTransform(t) 

    def pose_callback(self,msg):
        # print(msg)
        self.robot_pose[0] = msg.x
        self.robot_pose[1] = msg.y
        self.robot_pose[2] = msg.theta
        # print(self.robot_pose)
        self.odom_pub(self.robot_pose,"odom","turtle1")
        # odom_msg = Odometry()
        # odom_msg.header.stamp = self.get_clock().now().to_msg()
        # odom_msg.header.frame_id = "odom"
        # odom_msg.child_frame_id = "robot1"

        # odom_msg.pose.pose.position.x = self.robot_pose[0]
        # odom_msg.pose.pose.position.y = self.robot_pose[1]

        # q = quaternion_from_euler(0,0,self.robot_pose[2])
        # odom_msg.pose.pose.orientation.x = q[0]
        # odom_msg.pose.pose.orientation.y = q[1]
        # odom_msg.pose.pose.orientation.z = q[2]
        # odom_msg.pose.pose.orientation.w = q[3]

        # self.odom_publisher.publish(odom_msg)

        # t = TransformStamped()
        # t.header.stamp = self.get_clock().now().to_msg()
        # t.header.frame_id = 'odom'
        # t.child_frame_id = 'robot1'

        # t.transform.translation.x = self.robot_pose[0]
        # t.transform.translation.y = self.robot_pose[1]
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]

        # self.tf_boardcaster.sendTransform(t) 

        # odom_msg.twist.twist.angular

    def pose2_callback(self,msg):
        # print(msg)
        self.robot2_pose[0] = msg.x 
        self.robot2_pose[1] = msg.y
        self.robot2_pose[2] = msg.theta
        # print(self.robot_pose)
        self.odom_pub(self.robot2_pose,"odom","turtle2")
        # odom_msg = Odometry()
        # odom_msg.header.stamp = self.get_clock().now().to_msg()
        # odom_msg.header.frame_id = "odom"
        # odom_msg.child_frame_id = "robot2"

        # odom_msg.pose.pose.position.x = self.robot2_pose[0]
        # odom_msg.pose.pose.position.y = self.robot2_pose[1]

        # q = quaternion_from_euler(0,0,self.robot2_pose[2])
        # odom_msg.pose.pose.orientation.x = q[0]
        # odom_msg.pose.pose.orientation.y = q[1]
        # odom_msg.pose.pose.orientation.z = q[2]
        # odom_msg.pose.pose.orientation.w = q[3]

        # self.odom_publisher2.publish(odom_msg)

        # t = TransformStamped()
        # t.header.stamp = self.get_clock().now().to_msg()
        # t.header.frame_id = 'odom'
        # t.child_frame_id = 'robot2'

        # t.transform.translation.x = self.robot2_pose[0]
        # t.transform.translation.y = self.robot2_pose[1]
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]

        # self.tf_boardcaster.sendTransform(t) 

        # odom_msg.twist.twist.angular

    

    def timer_callback(self):
        now_x = self.robot_pose[0]
        now_y = self.robot_pose[1]
        # vx = 0.2*distance

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
