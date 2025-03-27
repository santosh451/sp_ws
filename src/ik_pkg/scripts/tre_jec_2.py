#! /usr/bin/env python3

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32MultiArray

class SingleLegTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('single_leg_trajectory_publisher')
        self.publisher = self.create_publisher(Float32MultiArray, '/foot_pose', 10)
        self.timer = self.create_timer(0.05, self.publish_trajectory)  # 50ms 
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.cmd_vel_callback, 10)
        self.t = 0.0  # Time

        self.cmd_vel_x = 0.0  # x velo
        self.cmd_vel_yaw = 0.0  # yaw
        self.cmd_vel_y = 0.0  # y velo

    def cmd_vel_callback(self, msg):

        self.cmd_vel_x = msg.linear.x   
        self.cmd_vel_yaw = msg.angular.z  
        self.cmd_vel_y = msg.linear.y
        self.get_logger().info(f"received vel0: linear_x={self.cmd_vel_x}, linear_y={self.cmd_vel_y}")
    
    def generate_leg_trajectory(self, height, length, y_offset, theta, delay, x_off, leg_side):

        frequency = 1.5 # Step cycle frequency
        
        z_in = math.sin(2 * math.pi * frequency * self.t+delay)
        if z_in <= 0:
            z_in = 0
        z_offset = height * z_in
        x_offset = length * (math.cos(2 * math.pi * frequency * self.t+delay)) / 2
        
        fw = 0.1 + x_offset  
        hi = 0.6 - z_offset  
        side = y_offset

        fw_final = fw * math.cos(theta)+x_off-0.1
        side_final = side-fw * math.sin(theta)
        if leg_side == 0:
            side_final == -side_final
        print(fw_final, side_final)

        return [hi, fw_final, side_final + side]

    def publish_trajectory(self):

        theta = math.atan2(self.cmd_vel_y,self.cmd_vel_x)
        # print(theta)
        length = math.sqrt(self.cmd_vel_x**2+self.cmd_vel_y**2)

        # theta = 0
        height = length*1.3

        if length> 0.2:
            length = 0.2
            height = 0.2
        
        # if (self.cmd_vel_x < 0 & self.cmd_vel_y >=0):
        #     length = -length
        # elif(self.cmd_vel_x < 0 & self.cmd_vel_y >=0)
        y_offset = 0.04
        fl = self.generate_leg_trajectory(height, length,  y_offset,  theta, 0, 0, 1)  # Front Left
        fr = self.generate_leg_trajectory(height, length, -y_offset, theta, math.pi, 0, 0) # Front Right
        hl = self.generate_leg_trajectory(height, length,  y_offset,  theta, math.pi, 0.2, 1)  # Hind Left
        hr = self.generate_leg_trajectory(height, length, -y_offset, theta, 0, 0.2, 0) # Hind Right

        foot_positions = fl + fr + hl + hr
        
        msg = Float32MultiArray()
        msg.data = foot_positions
        self.publisher.publish(msg)
        # self.get_logger().info(f"Publishing Foot Positions: {foot_positions}")
        self.t += 0.05  


def main():
    rclpy.init()
    node = SingleLegTrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
