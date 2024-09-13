// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from controller_interface:srv/SetTarget.idl
// generated code does not contain a copyright notice

#ifndef CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__STRUCT_H_
#define CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'target'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in srv/SetTarget in the package controller_interface.
typedef struct controller_interface__srv__SetTarget_Request
{
  geometry_msgs__msg__Point target;
} controller_interface__srv__SetTarget_Request;

// Struct for a sequence of controller_interface__srv__SetTarget_Request.
typedef struct controller_interface__srv__SetTarget_Request__Sequence
{
  controller_interface__srv__SetTarget_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} controller_interface__srv__SetTarget_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetTarget in the package controller_interface.
typedef struct controller_interface__srv__SetTarget_Response
{
  uint8_t structure_needs_at_least_one_member;
} controller_interface__srv__SetTarget_Response;

// Struct for a sequence of controller_interface__srv__SetTarget_Response.
typedef struct controller_interface__srv__SetTarget_Response__Sequence
{
  controller_interface__srv__SetTarget_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} controller_interface__srv__SetTarget_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CONTROLLER_INTERFACE__SRV__DETAIL__SET_TARGET__STRUCT_H_
