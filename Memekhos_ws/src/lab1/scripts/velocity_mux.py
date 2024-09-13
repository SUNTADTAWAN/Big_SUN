#!/usr/bin/python3

from lab1.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64 , Int32
from geometry_msgs.msg import Twist
import sys
class VelocityMux(Node):
    def __init__(self):
        super().__init__('VelocityMux_node')
        # Create subscriber dor topic /linear/noise
        self.linear_vel_subscriber = self.create_subscription(Float64, '/linear/noise',self.linear_vel_sub_callback,10)
        self.angular_vel_subscriber = self.create_subscription(Float64, '/angular/noise',self.angular_vel_sub_callback,10)
        self.linear_scale_vel_subscriber = self.create_subscription(Int32, '/linear/scale',self.linear_scale_callback,10)
        self.angular_scale_vel_subscriber = self.create_subscription(Int32, '/angular/scale',self.angular_scale_callback,10)
        self.cmd_publisher = self.create_publisher(Twist, '/cmd_vel',10)
        
        self.declare_parameter('rate', 5.0)
        self.rate = self.get_parameter('rate').get_parameter_value().double_value


        # if len(sys.argv) >= 1:
        #     self.rate = float(sys.argv[1])
        # else:
        #     self.rate  = 5.0
        self.linear_scale = 1.0
        self.angular_scale = 1.0
        self.cmd_vel = Twist()
        self.timer  = self.create_timer(1/self.rate,self.timer_callback)
        self.get_logger().info(f'Starting {self.get_name()}')

    def linear_scale_callback(self, msg:Int32):
        self.linear_scale = float(msg.data)

    def angular_scale_callback(self, msg:Int32):
        self.angular_scale = float(msg.data)

    def linear_vel_sub_callback(self, msg:Float64):
        self.cmd_vel.linear.x = self.linear_scale*msg.data

    def angular_vel_sub_callback(self , msg:Float64):
        self.cmd_vel.angular.z = self.angular_scale*msg.data

    def timer_callback(self):
        self.cmd_publisher.publish(self.cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    node = VelocityMux()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
