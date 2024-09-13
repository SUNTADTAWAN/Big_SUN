#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64 , Int32
from lab1_interface.srv import SetNoise
import sys
import numpy as np


class NoiseGenerator(Node):
    def __init__(self):
        #initialize super class node
        super().__init__('NoiseGenerator_node')
        # create publisher for topic /noise
        self.noise_publisher = self.create_publisher(Float64,'noise',10)
        self.scale_publisher = self.create_publisher(Int32,'scale',10)
        #set the publisher rate

        self.declare_parameter('rate', 5.0)
        self.rate = self.get_parameter('rate').get_parameter_value().double_value

        # if len(sys.argv) >= 1:
        #     self.rate = float(sys.argv[1] )
        # else:
        #     self.rate = 5.0
        # additional attribute
        self.mean = 0.0
        self.variance = 1.0
        self.scale = 1
        # create aservice server for /set noise
        self.set_noise_server = self.create_service( SetNoise, 'set_noise' ,self.set_noise_callback )
        #start a timer for publisher /noise
        self.timer = self.create_timer( 1/self.rate,self.timer_callback )
        self.get_logger().info(f'Starting {self.get_namespace()} / {self.get_name()} with thedefault parameter, mean:{self.mean} , variance {self.variance}, scale {self.scale}')

    def set_noise_callback(self, request:SetNoise.Request , response:SetNoise.Response):
        self.mean = request.mean.data
        self.variance = request.variance.data
        self.scale = request.scale.data
        return response

    
    def timer_callback(self):
        msg = Float64()
        msg_s = Int32()
        msg.data = np.random.normal(self.mean, np.sqrt(self.variance))
        msg_s.data = self.scale
        self.noise_publisher.publish(msg)
        self.scale_publisher.publish(msg_s)



def main(args=None):
    rclpy.init(args=args)
    node = NoiseGenerator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
