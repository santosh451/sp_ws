#! /usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from communication.msg import ActuatorCmds

# Link lengths
# this is used to get the joint pose and publish that pose
L1 = 0.11  # Hip to thigh joint
L2 = 0.321  # Thigh length
L3 = 0.335  # Shin length

class QuadrupedIK(Node):
    def __init__(self):
        super().__init__('quadruped_ik_node')
        
        self.subscription = self.create_subscription(
            Float32MultiArray, '/foot_pose', self.ik_callback, 10)
        
        self.publisher = self.create_publisher(
            ActuatorCmds, '/simulation/actuators_cmds', 10)

        self.get_logger().info("quadruped ik node Initialized")

    def calculate_ik(self, x, y, z):
        try:
            theta1 = math.atan2(z, x)

            x_proj = math.hypot(x, z) - L1
            y_proj = y
            D = math.hypot(x_proj, y_proj) 

            if D > (L2 + L3) or D < abs(L2 - L3):
                raise ValueError("invalid pose")

            cos_theta3 = (x_proj**2 + y_proj**2 - L2**2 - L3**2) / (2 * L2 * L3)
            theta3 = math.acos(cos_theta3)  
            
            theta3 = -theta3

            alpha = math.atan2(y_proj, x_proj)
            beta = math.atan2(L3 * math.sin(theta3), L2 + L3 * math.cos(theta3))
            theta2 = alpha - beta 

            return theta1, theta2, theta3

        except ValueError as e:
            self.get_logger().error(f"IK Error: {e}")
            return None


    def ik_callback(self, msg):
        if len(msg.data) != 12:
            self.get_logger().error("Invalid foot_pose data length")
            return
        foot_positions = {
            "fl": (msg.data[0], msg.data[1], msg.data[2]),
            "fr": (msg.data[3], msg.data[4], msg.data[5]),
            "hl": (msg.data[6], msg.data[7], msg.data[8]),
            "hr": (msg.data[9], msg.data[10], msg.data[11]),
        }

        joint_angles = {}
        for leg, (x, y, z) in foot_positions.items():
            angles = self.calculate_ik(x, y, z)
            if angles:
                joint_angles[leg] = angles
            else:
                return  

        self.publish_joint_angles(joint_angles)

    def publish_joint_angles(self, joint_angles):
        msg = ActuatorCmds()
        msg.actuators_name = ['fl.hx', 'fl.hy', 'fl.kn', 
                              'fr.hx', 'fr.hy', 'fr.kn', 
                              'hl.hx', 'hl.hy', 'hl.kn', 
                              'hr.hx', 'hr.hy', 'hr.kn']

        msg.pos = [
            joint_angles["fl"][0], joint_angles["fl"][1], joint_angles["fl"][2],
            joint_angles["fr"][0], joint_angles["fr"][1], joint_angles["fr"][2],
            joint_angles["hl"][0], joint_angles["hl"][1], joint_angles["hl"][2],
            joint_angles["hr"][0], joint_angles["hr"][1], joint_angles["hr"][2]
        ]

        msg.kp = [400.0] * 12
        msg.kd = [4.5] * 12 
        msg.vel = [0.0] * 12 
        msg.torque = [0.0] * 12 

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = QuadrupedIK()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
