#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

#this is used to publish static tfs

class StaticTransformPublisher(Node):
    def __init__(self):
        super().__init__('static_tf_publisher')
        self.tf_broadcaster = StaticTransformBroadcaster(self)
        
        # Publish static transforms
        self.publish_static_transform("odom", "map", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
        self.publish_static_transform("base", "base_link", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
        self.publish_static_transform("odom", "map", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
        self.get_logger().info("Static transforms published")

    def publish_static_transform(self, parent_frame, child_frame, x, y, z, qx, qy, qz, qw):
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = parent_frame
        transform.child_frame_id = child_frame
        transform.transform.translation.x = x
        transform.transform.translation.y = y
        transform.transform.translation.z = z
        transform.transform.rotation.x = qx
        transform.transform.rotation.y = qy
        transform.transform.rotation.z = qz
        transform.transform.rotation.w = qw
        
        self.tf_broadcaster.sendTransform(transform)


def main():
    rclpy.init()
    node = StaticTransformPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()