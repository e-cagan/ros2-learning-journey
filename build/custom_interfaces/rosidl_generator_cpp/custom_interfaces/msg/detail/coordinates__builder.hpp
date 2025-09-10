// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:msg/Coordinates.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__BUILDER_HPP_
#define CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/msg/detail/coordinates__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace msg
{

namespace builder
{

class Init_Coordinates_y
{
public:
  explicit Init_Coordinates_y(::custom_interfaces::msg::Coordinates & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::msg::Coordinates y(::custom_interfaces::msg::Coordinates::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::msg::Coordinates msg_;
};

class Init_Coordinates_x
{
public:
  Init_Coordinates_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Coordinates_y x(::custom_interfaces::msg::Coordinates::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Coordinates_y(msg_);
  }

private:
  ::custom_interfaces::msg::Coordinates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::msg::Coordinates>()
{
  return custom_interfaces::msg::builder::Init_Coordinates_x();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__COORDINATES__BUILDER_HPP_
