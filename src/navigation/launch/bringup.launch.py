from launch import LaunchDescription
from launch_ros.actions import Node
# from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, RegisterEventHandler, LogInfo, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    navigation_launch_dir = get_package_share_directory('navigation')
    robot_dir = get_package_share_directory('mujoco')
    cartographer_slam_launch_dir = get_package_share_directory('cartographer_slam')
    control_dir = get_package_share_directory('control_robo')

    control_path = os.path.join(control_dir, 'launch', 'robot_control.launch.py')
    robot_launch_path = os.path.join(robot_dir, 'launch', 'simulation_launch.py')
    ekf_launch_path = os.path.join(navigation_launch_dir, 'launch', 'ekf.launch.py')
    navigation_launch_path = os.path.join(navigation_launch_dir, 'launch', 'navigation.launch.py')
    cartographer_slam_path = os.path.join(cartographer_slam_launch_dir, 'launch', 'cartographer.launch.py')



    ld = LaunchDescription()

    robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(robot_launch_path)
    )

    control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(control_path)
    )

    ekf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(ekf_launch_path)
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(navigation_launch_path)
    )
    cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(cartographer_slam_path)
    )

    ld.add_action(robot_launch)
    ld.add_action(control_launch)
    # ld.add_action(ekf_launch)
    # ld.add_action(navigation_launch)
    ld.add_action(navigation_launch)
    # ld.add_action(static_tf_launch)
    # ld.add_action(cartographer_launch)


    return ld

    
