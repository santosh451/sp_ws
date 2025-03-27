import os
from ament_index_python.packages import get_package_share_path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import Command

def generate_launch_description():
    xml_file_name = "model/xml/spot_mini/spot_mini.xml"
    xml_file = os.path.join(get_package_share_path("description"), xml_file_name)
    rviz_config_file = os.path.join(xml_file, 'config', 'rviz_2.rviz')

    return LaunchDescription(
        [
            Node(
                package="mujoco",
                executable="simulation",
                name="simulation_mujoco",
                output="screen",
                parameters=[
                    {"simulation/model_file": xml_file},
                ],
                emulate_tty=True,
                arguments=[("__log_level:=debug")],
            ),
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                output='screen',
                parameters=[{
                    'robot_description': Command(['xacro ', 
                        PathJoinSubstitution([
                            FindPackageShare('description'),
                            'model/urdf/spot_mini/model.urdf'
                        ])
                    ])
                }],
                remappings=[('/joint_states', '/simulation/joint_states')]
            ),
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', rviz_config_file],
                output='screen'
            )
            # Node(
            #     package='tf2_ros',
            #     executable='static_transform_publisher',
            #     name='odom_base_tf',
            #     arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
            # )

        ]
    )
