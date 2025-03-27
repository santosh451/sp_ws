cmake_minimum_required(VERSION 3.8)
project(ik_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(communication REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(orocos_kdl REQUIRED)
find_package(Eigen3 REQUIRED)
find_package(kdl_parser REQUIRED)
find_package(urdf REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(ament_index_cpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install( DIRECTORY 
  launch
  scripts
  DESTINATION share/${PROJECT_NAME})

add_executable(leg_run_2 src/ik_solver_numerical.cpp)
ament_target_dependencies(leg_run_2
  rclcpp 
  std_msgs 
  communication
  orocos_kdl
  Eigen3
  kdl_parser
  urdf
  ament_index_cpp
  )

install(TARGETS
  leg_run_2

  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/tre_jec_2.py  # Add your Python script here
  scripts/test_mod.py
  scripts/tf_pub.py
  scripts/mp_o_tf.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
