// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ised7881_service:srv/Ised7881Service.idl
// generated code does not contain a copyright notice

#ifndef ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_H_
#define ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'input'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Ised7881Service in the package ised7881_service.
typedef struct ised7881_service__srv__Ised7881Service_Request
{
  rosidl_runtime_c__String input;
} ised7881_service__srv__Ised7881Service_Request;

// Struct for a sequence of ised7881_service__srv__Ised7881Service_Request.
typedef struct ised7881_service__srv__Ised7881Service_Request__Sequence
{
  ised7881_service__srv__Ised7881Service_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ised7881_service__srv__Ised7881Service_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'reversed_text'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Ised7881Service in the package ised7881_service.
typedef struct ised7881_service__srv__Ised7881Service_Response
{
  rosidl_runtime_c__String reversed_text;
  double runtime;
} ised7881_service__srv__Ised7881Service_Response;

// Struct for a sequence of ised7881_service__srv__Ised7881Service_Response.
typedef struct ised7881_service__srv__Ised7881Service_Response__Sequence
{
  ised7881_service__srv__Ised7881Service_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ised7881_service__srv__Ised7881Service_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_H_
