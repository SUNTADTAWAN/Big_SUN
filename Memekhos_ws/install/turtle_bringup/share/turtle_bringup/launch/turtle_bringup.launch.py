# from launch import LaunchDescription
# from launch_ros.actions import Node

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess,DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

# def generate_launch_description():
#     launch_description = LaunchDescription()
#     rate_mux = LaunchConfiguration('frequency')
#     rate_launch_arg = DeclareLaunchArgument(
#         'frequency',
#         default_value= '10.0'
#     )
#     launch_description.add_action(rate_launch_arg)

#     # name_launch_arg = DeclareLaunchArgument(
#     #     'namespace',
#     #     default_value= 'Turtle'
#     # )
#     # launch_description.add_action(name_launch_arg)


#     package_name = 'turtle_bringup'
#     executable_name = ['controller.py','crazy_turtle.py']
#     namespace = ['xx1','xx2']
#     rate = [100.0,100.0]
#     for i in range(len(executable_name)):
#         turtle_gen = Node(
#             package= package_name,
#             namespace= namespace[i],
#             executable=executable_name[i],
#             name= namespace[i]+"_turtle",
#             parameters=[
#                 {'frequency':rate[0]}
#             ]
#         )
#         launch_description.add_action(turtle_gen)
#     pizza_n = Node(
#             package=package_name,
#             namespace='',
#             executable='velocity_mux.py',
#             name='mux',
#             remappings=[
#                 ('/cmd_vel', 'turtle1/cmd_vel')
#             ],
#             parameters=[
#                 {'rate':rate_mux}
#             ]
#         )
#     launch_description.add_action(pizza_n)
#     turtlesim_node = Node(
#             package='turtlesim_plus',
#             namespace='',
#             executable='turtlesim_plus_node.py',
#             name='turtlesim'
#         )
#     launch_description.add_action(turtlesim_node)


    

#     return launch_description
def generate_launch_description():
    launch_description = LaunchDescription()
    kill = 'turtle1'
    nametao = ['NongTao1','NongTao2']
    remove_turtle = ExecuteProcess(
            cmd = [[
                'ros2 service call /remove_turtle turtlesim/srv/Kill "name: \'turtle1\'" ',
            ]],
            shell =True
        )
    spawn_turtle = ExecuteProcess(
            cmd = [[
                'ros2 service call /spawn_turtle turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: \''+nametao[0]+'\'}"',
            ]],
            shell =True
        )
    spawn_turtle2 = ExecuteProcess(
            cmd = [[
                'ros2 service call /spawn_turtle turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: \''+nametao[1]+'\'}"',
            ]],
            shell =True
        )
    run_node = Node(
            package='turtlesim_plus',
            namespace='',
            executable='turtlesim_plus_node.py',
            name='turtlesim'
        )
    run_spawn = Node(
            package='turtle_bringup',
            namespace=nametao[0],
            executable='controller.py',
            name='controller_turtle',
            parameters=[
                {'frequency':100.0}
            ]
        )
    run_spawn_pizza = Node(
            package='turtle_bringup',
            namespace='',
            executable='crazy_pizza.py',
            name='crazy_pizza'
        )
        # Node(
        #     package='turtle_bringup',
        #     namespace='',
        #     executable='odom_publisher.py',
        #     name='odom_pub'
        # ),
        # Node(
        #     package='rviz2',
        #     namespace='',
        #     executable='rviz2',
        #     name='rviz2',
        #     arguments = ['-d', [' /home/aitthikit/Memekhos_ws/src/fun2.rviz']]
        # ),
    run_spawn_crazyturtle =  Node(
            package='turtle_bringup',
            namespace=nametao[1],
            executable='crazy_turtle.py',
            name='crazy_turtle',
            parameters=[
                {'frequency':100.0}
            ]
        )
    launch_description.add_action(run_node)
    launch_description.add_action(remove_turtle) 
    launch_description.add_action(spawn_turtle)
    launch_description.add_action(run_spawn)
    launch_description.add_action(spawn_turtle2)
    launch_description.add_action(run_spawn_pizza)
    launch_description.add_action(run_spawn_crazyturtle)

    
    return launch_description
        
        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )

 