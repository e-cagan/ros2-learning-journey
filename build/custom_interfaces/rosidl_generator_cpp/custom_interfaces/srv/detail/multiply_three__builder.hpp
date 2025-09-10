// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/MultiplyThree.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__MULTIPLY_THREE__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__MULTIPLY_THREE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/multiply_three__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_MultiplyThree_Request_c
{
public:
  explicit Init_MultiplyThree_Request_c(::custom_interfaces::srv::MultiplyThree_Request & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::MultiplyThree_Request c(::custom_interfaces::srv::MultiplyThree_Request::_c_type arg)
  {
    msg_.c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::MultiplyThree_Request msg_;
};

class Init_MultiplyThree_Request_b
{
public:
  explicit Init_MultiplyThree_Request_b(::custom_interfaces::srv::MultiplyThree_Request & msg)
  : msg_(msg)
  {}
  Init_MultiplyThree_Request_c b(::custom_interfaces::srv::MultiplyThree_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return Init_MultiplyThree_Request_c(msg_);
  }

private:
  ::custom_interfaces::srv::MultiplyThree_Request msg_;
};

class Init_MultiplyThree_Request_a
{
public:
  Init_MultiplyThree_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MultiplyThree_Request_b a(::custom_interfaces::srv::MultiplyThree_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_MultiplyThree_Request_b(msg_);
  }

private:
  ::custom_interfaces::srv::MultiplyThree_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::MultiplyThree_Request>()
{
  return custom_interfaces::srv::builder::Init_MultiplyThree_Request_a();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_MultiplyThree_Response_product
{
public:
  Init_MultiplyThree_Response_product()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::MultiplyThree_Response product(::custom_interfaces::srv::MultiplyThree_Response::_product_type arg)
  {
    msg_.product = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::MultiplyThree_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::MultiplyThree_Response>()
{
  return custom_interfaces::srv::builder::Init_MultiplyThree_Response_product();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__MULTIPLY_THREE__BUILDER_HPP_
