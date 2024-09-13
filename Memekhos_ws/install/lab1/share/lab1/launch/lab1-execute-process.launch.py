from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess,DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    launch_description = LaunchDescription()

    interface_type = "lab1_interface/srv/SetNoise"
    noise_propeties = [
        ('linear',1.0,0.1,2),
        ('angular',0.0,3.0,2)
    ]

    for ns,mean,var,sca in noise_propeties:
        set_noise = ExecuteProcess(
            cmd = [[
                'ros2 service call ',
                str(ns),
                '/set_noise ',
                interface_type,
                ' ',
                f'"{{mean: {{data: {mean}}}, variance: {{data: {var}}}, scale: {{data: {sca}}}}}"'
            ]],
            shell =True
        )
        launch_description.add_action( set_noise )

    return launch_description