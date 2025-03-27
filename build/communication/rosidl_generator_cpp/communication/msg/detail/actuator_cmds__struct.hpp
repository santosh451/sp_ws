// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from communication:msg/ActuatorCmds.idl
// generated code does not contain a copyright notice

#ifndef COMMUNICATION__MSG__DETAIL__ACTUATOR_CMDS__STRUCT_HPP_
#define COMMUNICATION__MSG__DETAIL__ACTUATOR_CMDS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__communication__msg__ActuatorCmds __attribute__((deprecated))
#else
# define DEPRECATED__communication__msg__ActuatorCmds __declspec(deprecated)
#endif

namespace communication
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ActuatorCmds_
{
  using Type = ActuatorCmds_<ContainerAllocator>;

  explicit ActuatorCmds_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit ActuatorCmds_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _actuators_name_type =
    rosidl_runtime_cpp::BoundedVector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _actuators_name_type actuators_name;
  using _kp_type =
    rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _kp_type kp;
  using _pos_type =
    rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _pos_type pos;
  using _kd_type =
    rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _kd_type kd;
  using _vel_type =
    rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _vel_type vel;
  using _torque_type =
    rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _torque_type torque;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__actuators_name(
    const rosidl_runtime_cpp::BoundedVector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->actuators_name = _arg;
    return *this;
  }
  Type & set__kp(
    const rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->kp = _arg;
    return *this;
  }
  Type & set__pos(
    const rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__kd(
    const rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->kd = _arg;
    return *this;
  }
  Type & set__vel(
    const rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->vel = _arg;
    return *this;
  }
  Type & set__torque(
    const rosidl_runtime_cpp::BoundedVector<float, 30, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->torque = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    communication::msg::ActuatorCmds_<ContainerAllocator> *;
  using ConstRawPtr =
    const communication::msg::ActuatorCmds_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<communication::msg::ActuatorCmds_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<communication::msg::ActuatorCmds_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      communication::msg::ActuatorCmds_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<communication::msg::ActuatorCmds_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      communication::msg::ActuatorCmds_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<communication::msg::ActuatorCmds_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<communication::msg::ActuatorCmds_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<communication::msg::ActuatorCmds_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__communication__msg__ActuatorCmds
    std::shared_ptr<communication::msg::ActuatorCmds_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__communication__msg__ActuatorCmds
    std::shared_ptr<communication::msg::ActuatorCmds_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ActuatorCmds_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->actuators_name != other.actuators_name) {
      return false;
    }
    if (this->kp != other.kp) {
      return false;
    }
    if (this->pos != other.pos) {
      return false;
    }
    if (this->kd != other.kd) {
      return false;
    }
    if (this->vel != other.vel) {
      return false;
    }
    if (this->torque != other.torque) {
      return false;
    }
    return true;
  }
  bool operator!=(const ActuatorCmds_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ActuatorCmds_

// alias to use template instance with default allocator
using ActuatorCmds =
  communication::msg::ActuatorCmds_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace communication

#endif  // COMMUNICATION__MSG__DETAIL__ACTUATOR_CMDS__STRUCT_HPP_
