// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from controller_interface:srv/SetParam.idl
// generated code does not contain a copyright notice
#include "controller_interface/srv/detail/set_param__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `kp_linear`
// Member `kp_angular`
#include "std_msgs/msg/detail/float64__functions.h"

bool
controller_interface__srv__SetParam_Request__init(controller_interface__srv__SetParam_Request * msg)
{
  if (!msg) {
    return false;
  }
  // kp_linear
  if (!std_msgs__msg__Float64__init(&msg->kp_linear)) {
    controller_interface__srv__SetParam_Request__fini(msg);
    return false;
  }
  // kp_angular
  if (!std_msgs__msg__Float64__init(&msg->kp_angular)) {
    controller_interface__srv__SetParam_Request__fini(msg);
    return false;
  }
  return true;
}

void
controller_interface__srv__SetParam_Request__fini(controller_interface__srv__SetParam_Request * msg)
{
  if (!msg) {
    return;
  }
  // kp_linear
  std_msgs__msg__Float64__fini(&msg->kp_linear);
  // kp_angular
  std_msgs__msg__Float64__fini(&msg->kp_angular);
}

bool
controller_interface__srv__SetParam_Request__are_equal(const controller_interface__srv__SetParam_Request * lhs, const controller_interface__srv__SetParam_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // kp_linear
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->kp_linear), &(rhs->kp_linear)))
  {
    return false;
  }
  // kp_angular
  if (!std_msgs__msg__Float64__are_equal(
      &(lhs->kp_angular), &(rhs->kp_angular)))
  {
    return false;
  }
  return true;
}

bool
controller_interface__srv__SetParam_Request__copy(
  const controller_interface__srv__SetParam_Request * input,
  controller_interface__srv__SetParam_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // kp_linear
  if (!std_msgs__msg__Float64__copy(
      &(input->kp_linear), &(output->kp_linear)))
  {
    return false;
  }
  // kp_angular
  if (!std_msgs__msg__Float64__copy(
      &(input->kp_angular), &(output->kp_angular)))
  {
    return false;
  }
  return true;
}

controller_interface__srv__SetParam_Request *
controller_interface__srv__SetParam_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Request * msg = (controller_interface__srv__SetParam_Request *)allocator.allocate(sizeof(controller_interface__srv__SetParam_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(controller_interface__srv__SetParam_Request));
  bool success = controller_interface__srv__SetParam_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
controller_interface__srv__SetParam_Request__destroy(controller_interface__srv__SetParam_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    controller_interface__srv__SetParam_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
controller_interface__srv__SetParam_Request__Sequence__init(controller_interface__srv__SetParam_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Request * data = NULL;

  if (size) {
    data = (controller_interface__srv__SetParam_Request *)allocator.zero_allocate(size, sizeof(controller_interface__srv__SetParam_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = controller_interface__srv__SetParam_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        controller_interface__srv__SetParam_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
controller_interface__srv__SetParam_Request__Sequence__fini(controller_interface__srv__SetParam_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      controller_interface__srv__SetParam_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

controller_interface__srv__SetParam_Request__Sequence *
controller_interface__srv__SetParam_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Request__Sequence * array = (controller_interface__srv__SetParam_Request__Sequence *)allocator.allocate(sizeof(controller_interface__srv__SetParam_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = controller_interface__srv__SetParam_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
controller_interface__srv__SetParam_Request__Sequence__destroy(controller_interface__srv__SetParam_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    controller_interface__srv__SetParam_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
controller_interface__srv__SetParam_Request__Sequence__are_equal(const controller_interface__srv__SetParam_Request__Sequence * lhs, const controller_interface__srv__SetParam_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!controller_interface__srv__SetParam_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
controller_interface__srv__SetParam_Request__Sequence__copy(
  const controller_interface__srv__SetParam_Request__Sequence * input,
  controller_interface__srv__SetParam_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(controller_interface__srv__SetParam_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    controller_interface__srv__SetParam_Request * data =
      (controller_interface__srv__SetParam_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!controller_interface__srv__SetParam_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          controller_interface__srv__SetParam_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!controller_interface__srv__SetParam_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
controller_interface__srv__SetParam_Response__init(controller_interface__srv__SetParam_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
controller_interface__srv__SetParam_Response__fini(controller_interface__srv__SetParam_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
controller_interface__srv__SetParam_Response__are_equal(const controller_interface__srv__SetParam_Response * lhs, const controller_interface__srv__SetParam_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
controller_interface__srv__SetParam_Response__copy(
  const controller_interface__srv__SetParam_Response * input,
  controller_interface__srv__SetParam_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

controller_interface__srv__SetParam_Response *
controller_interface__srv__SetParam_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Response * msg = (controller_interface__srv__SetParam_Response *)allocator.allocate(sizeof(controller_interface__srv__SetParam_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(controller_interface__srv__SetParam_Response));
  bool success = controller_interface__srv__SetParam_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
controller_interface__srv__SetParam_Response__destroy(controller_interface__srv__SetParam_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    controller_interface__srv__SetParam_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
controller_interface__srv__SetParam_Response__Sequence__init(controller_interface__srv__SetParam_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Response * data = NULL;

  if (size) {
    data = (controller_interface__srv__SetParam_Response *)allocator.zero_allocate(size, sizeof(controller_interface__srv__SetParam_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = controller_interface__srv__SetParam_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        controller_interface__srv__SetParam_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
controller_interface__srv__SetParam_Response__Sequence__fini(controller_interface__srv__SetParam_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      controller_interface__srv__SetParam_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

controller_interface__srv__SetParam_Response__Sequence *
controller_interface__srv__SetParam_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  controller_interface__srv__SetParam_Response__Sequence * array = (controller_interface__srv__SetParam_Response__Sequence *)allocator.allocate(sizeof(controller_interface__srv__SetParam_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = controller_interface__srv__SetParam_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
controller_interface__srv__SetParam_Response__Sequence__destroy(controller_interface__srv__SetParam_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    controller_interface__srv__SetParam_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
controller_interface__srv__SetParam_Response__Sequence__are_equal(const controller_interface__srv__SetParam_Response__Sequence * lhs, const controller_interface__srv__SetParam_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!controller_interface__srv__SetParam_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
controller_interface__srv__SetParam_Response__Sequence__copy(
  const controller_interface__srv__SetParam_Response__Sequence * input,
  controller_interface__srv__SetParam_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(controller_interface__srv__SetParam_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    controller_interface__srv__SetParam_Response * data =
      (controller_interface__srv__SetParam_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!controller_interface__srv__SetParam_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          controller_interface__srv__SetParam_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!controller_interface__srv__SetParam_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
