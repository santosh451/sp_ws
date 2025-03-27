#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_msgs.msg import Float32MultiArray

#to move robot at the custom joint pose

class FootPosePublisher(Node):
    def __init__(self):
        super().__init__('foot_pose_publisher')

        self.publisher_ = self.create_publisher(Float32MultiArray, '/foot_pose', 10)

        self.timer = self.create_timer(0.05, self.publish_pose)

        self.get_logger().info("Foot Pose Publisher Node Started")

    def publish_pose(self):
        msg = Float32MultiArray()

        # first is height(-z) secound is forward(x) and thired is side(y) 
        foot_positions = [
            0.6, 0.0, 0.08,  # FL 
            0.6, -0.0, 0.08,  # FR
            0.6, 0.1, 0.08,  # HL 
            0.6, 0.1, 0.08   # HR 
        ]

        msg.data = foot_positions
        self.publisher_.publish(msg)

        self.get_logger().info(f"Published Foot Poses: {foot_positions}")

def main(args=None):
    rclpy.init(args=args)
    node = FootPosePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
