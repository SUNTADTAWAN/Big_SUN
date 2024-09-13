// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lab1_interface:srv/SetNoise.idl
// generated code does not contain a copyright notice

#ifndef LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__BUILDER_HPP_
#define LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lab1_interface/srv/detail/set_noise__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lab1_interface
{

namespace srv
{

namespace builder
{

class Init_SetNoise_Request_scale
{
public:
  explicit Init_SetNoise_Request_scale(::lab1_interface::srv::SetNoise_Request & msg)
  : msg_(msg)
  {}
  ::lab1_interface::srv::SetNoise_Request scale(::lab1_interface::srv::SetNoise_Request::_scale_type arg)
  {
    msg_.scale = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab1_interface::srv::SetNoise_Request msg_;
};

class Init_SetNoise_Request_variance
{
public:
  explicit Init_SetNoise_Request_variance(::lab1_interface::srv::SetNoise_Request & msg)
  : msg_(msg)
  {}
  Init_SetNoise_Request_scale variance(::lab1_interface::srv::SetNoise_Request::_variance_type arg)
  {
    msg_.variance = std::move(arg);
    return Init_SetNoise_Request_scale(msg_);
  }

private:
  ::lab1_interface::srv::SetNoise_Request msg_;
};

class Init_SetNoise_Request_mean
{
public:
  Init_SetNoise_Request_mean()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetNoise_Request_variance mean(::lab1_interface::srv::SetNoise_Request::_mean_type arg)
  {
    msg_.mean = std::move(arg);
    return Init_SetNoise_Request_variance(msg_);
  }

private:
  ::lab1_interface::srv::SetNoise_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab1_interface::srv::SetNoise_Request>()
{
  return lab1_interface::srv::builder::Init_SetNoise_Request_mean();
}

}  // namespace lab1_interface


namespace lab1_interface
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab1_interface::srv::SetNoise_Response>()
{
  return ::lab1_interface::srv::SetNoise_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace lab1_interface

#endif  // LAB1_INTERFACE__SRV__DETAIL__SET_NOISE__BUILDER_HPP_
