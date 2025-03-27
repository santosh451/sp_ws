from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    show_gui = LaunchConfiguration("use_gui", default="True")

    actuator_cmd_publisher_node = Node(
        package='ik_pkg',
        executable='act_pub',
        name='actuator_cmd_publisher',
        output='screen'
    )

    joint_state_publisher_gui_node = Node(
        condition=IfCondition(show_gui),
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        remappings=[('/joint_states', '/simulation/joint_state')]
    )

    return LaunchDescription([
        actuator_cmd_publisher_node,
        joint_state_publisher_gui_node
    ])
