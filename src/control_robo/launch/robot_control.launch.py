from launch import LaunchDescription
from launch_ros.actions import Node
# this launch file will launch all the nodes required to control the robot and required tf's
def generate_launch_description():

    trejectory_planner_node = Node(
        package='ik_pkg',
        executable='tre_jec_2.py',
        name='trejectory_planner',
        # output='screen'
    )
    ik_and_joint_pub_node = Node(
        package='ik_pkg',
        executable='test_mod.py',
        name='ik_solver_and_writer',
        # output='screen'
    )
    odom_tf_node = Node(
        package='ik_pkg',
        executable='tf_pub.py',
        name='trejectory_planner',
        # output='screen'
    )
    tf_node = Node(
        package='ik_pkg',
        executable='mp_o_tf.py',
        name='trejectory_planner',
        # output='screen'
    )

    return LaunchDescription([
        trejectory_planner_node,
        ik_and_joint_pub_node,
        odom_tf_node,
        tf_node
    ])
