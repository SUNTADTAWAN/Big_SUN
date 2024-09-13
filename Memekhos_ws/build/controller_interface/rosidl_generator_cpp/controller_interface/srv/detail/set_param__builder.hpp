// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from controller_interface:srv/SetParam.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACE__SRV__DETAIL__SET_PARAM__BUILDER_HPP_
#define CONTROLLER_INTERFACE__SRV__DETAIL__SET_PARAM__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "controller_interface/srv/detail/set_param__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace controller_interface
{

namespace srv
{

namespace builder
{

class Init_SetParam_Request_kp_angular
{
public:
  explicit Init_SetParam_Request_kp_angular(::controller_interface::srv::SetParam_Request & msg)
  : msg_(msg)
  {}
  ::controller_interface::srv::SetParam_Request kp_angular(::controller_interface::srv::SetParam_Request::_kp_angular_type arg)
  {
    msg_.kp_angular = std::move(arg);
    return std::move(msg_);
  }

private:
  ::controller_interface::srv::SetParam_Request msg_;
};

class Init_SetParam_Request_kp_linear
{
public:
  Init_SetParam_Request_kp_linear()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetParam_Request_kp_angular kp_linear(::controller_interface::srv::SetParam_Request::_kp_linear_type arg)
  {
    msg_.kp_linear = std::move(arg);
    return Init_SetParam_Request_kp_angular(msg_);
  }

private:
  ::controller_interface::srv::SetParam_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::controller_interface::srv::SetParam_Request>()
{
  return controller_interface::srv::builder::Init_SetParam_Request_kp_linear();
}

}  // namespace controller_interface


namespace controller_interface
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::controller_interface::srv::SetParam_Response>()
{
  return ::controller_interface::srv::SetParam_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace controller_interface

#endif  // CONTROLLER_INTERFACE__SRV__DETAIL__SET_PARAM__BUILDER_HPP_
