// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from controller_interface:srv/SetTarget.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__BUILDER_HPP_
#define CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "controller_interface/srv/detail/set_target__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace controller_interface
{

namespace srv
{

namespace builder
{

class Init_SetTarget_Request_target
{
public:
  Init_SetTarget_Request_target()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::controller_interface::srv::SetTarget_Request target(::controller_interface::srv::SetTarget_Request::_target_type arg)
  {
    msg_.target = std::move(arg);
    return std::move(msg_);
  }

private:
  ::controller_interface::srv::SetTarget_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::controller_interface::srv::SetTarget_Request>()
{
  return controller_interface::srv::builder::Init_SetTarget_Request_target();
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
auto build<::controller_interface::srv::SetTarget_Response>()
{
  return ::controller_interface::srv::SetTarget_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace controller_interface

#endif  // CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__BUILDER_HPP_
