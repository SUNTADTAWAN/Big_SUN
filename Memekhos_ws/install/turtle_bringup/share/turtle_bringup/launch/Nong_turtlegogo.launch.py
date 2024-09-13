from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py',
            name='turtlesim'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='controller.py',
            name='controller'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='crazy_pizza.py',
            name='crazy_pizza'
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='odom_publisher.py',
            name='odom_pub'
        ),
        Node(
            package='rviz2',
            namespace='',
            executable='rviz2',
            name='rviz2',
            arguments = ['-d', [' /home/aitthikit/Memekhos_ws/src/fun2.rviz']]
        ),
        Node(
            package='turtle_bringup',
            namespace='',
            executable='crazy_turtle.py',
            name='crazy_turtle'
        ),
        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])  