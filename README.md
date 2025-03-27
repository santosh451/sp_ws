# Spot roobot simulation in mujoco with gait controllers

## FK of a leg:-

Calculated using DH perameter

```
T03 = 

[cos(theta1)*cos(theta2)*cos(theta3) - cos(theta1)*sin(theta2)*sin(theta3), - cos(theta1)*cos(theta2)*sin(theta3) - cos(theta1)*cos(theta3)*sin(theta2),  sin(theta1), L2*cos(theta1)*cos(theta2) + L3*cos(theta1)*cos(theta2)*cos(theta3) - L3*cos(theta1)*sin(theta2)*sin(theta3)]

[cos(theta2)*cos(theta3)*sin(theta1) - sin(theta1)*sin(theta2)*sin(theta3), - cos(theta2)*sin(theta1)*sin(theta3) - cos(theta3)*sin(theta1)*sin(theta2), -cos(theta1), L2*cos(theta2)*sin(theta1) + L3*cos(theta2)*cos(theta3)*sin(theta1) - L3*sin(theta1)*sin(theta2)*sin(theta3)]

[                        cos(theta2)*sin(theta3) + cos(theta3)*sin(theta2),                           cos(theta2)*cos(theta3) - sin(theta2)*sin(theta3),            0,                                L1 + L2*sin(theta2) + L3*cos(theta2)*sin(theta3) + L3*cos(theta3)*sin(theta2)]

[                                                                        0,                                                                           0,            0,                                                                                                            1]
```
## IK solution:-

Implimented IK for each leg using analytical and numerical solution both for numerical solution KDL librery used.

```
theta1 = atan2(y, x)

r = sqrt(x² + y²)
D = (r² + z² - L₂² - L₃²) / (2 * L₂ * L₃)

theta3 = atan2(sqrt(1 - D²), D)

theta3 = atan2(z, r) - atan2(L₃ * sin(theta3), L₂ + L₃ * cos(theta3))
```

## Gait controller (Trotting Gait)

Implimented trotting gait controller where digonal legs left at a time and move forward.

In this sinosidial function is use to get the trejectory of individual legs
```
frequency = 1.5 # Step cycle frequency
        
z_in = math.sin(2 * pi * frequency * t+pi)
if z_in <= 0:
    z_in = 0
z_offset = height * z_in
x_offset = length * (cos(2 * pi * frequency * t+pi)) / 2
        
fw = 0.1 + x_offset  
hi = 0.6 - z_offset  
side = y_offset

fw_final = fw * cos(theta)+x_off-0.1
side_final = side-fw * sin(theta)

``` 
using this controller currently the robot can move in x y plane

## Navigation

- connected navigation stack to perform the autonomous navigation.
- Tested autonomous navigation in a obstrical free environment.
- added cartographer slam for mapping
- For navigation nav2 stack is used.


## To run:-

1. Clone the repo

2. build:-
```
colcon build --symlink-install --packages-select core
```
```
colcon build --symlink-install --packages-select communication
```
```
colcon build --symlink-install
```

3. sourse the ws:-
```
source install/setup.bash
```

4.Run the robot:-

```
ros2 launch navigation bringup.launch.py
```

This will launch all the required nodes and launch file 
including 
- simulation
- rviz2 (visulaizer)
- robot controller
- navigation stack


### Solution apporoch

To do this first of all I setup the simulation and the robot need to be simulated in MuJoCo simulator.

Connected MuJoCo to the rviz2 by remaping topics and to get the data of robot used robot state publisher node.

Solved FK and IK of a leg and implimented them so that whenever data published on foot_pose topic it will read that and write the final joint angles to the robot by the custom actuator_cmds.

Implimented trot gait controller for the robot which will enable the robot to move in x y plane. This takes input from the cmd_vel and based on that calculates the step height length and theta and then publish foot_pose.

Implemented navigation stack on top of this so this will enable robot to move autonomously. Currently navigation is done only in the obstrical free environment due to some issue with the depth topic data.

simulation pkg used:- 
```
https://github.com/MindSpaceInc/Spot-MuJoCo-ROS2
```




