import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'vac_bot'

    rsp = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory(package_name), 'launch', 'rsp.launch.py'  
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    default_world = os.path.join(
        get_package_share_directory(package_name), 
        'worlds', 
        'empty.world'
    )
    
    world = LaunchConfiguration('world')
    
    world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world,
        description='world to load'
    )

    gz_sim = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
                )]), launch_arguments={'gz_args': ['-r -v4', world], 'on_exit_shutdown': 'true'}.items()
    )

    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name','my_bot',
                                    '-z', '0.5'],
                        output='screen')
    
    return LaunchDescription([
        world_arg,
        gz_sim,
        rsp,
        spawn_entity
    ])