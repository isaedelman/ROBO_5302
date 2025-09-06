// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from ised7881_service:srv/Ised7881Service.idl
// generated code does not contain a copyright notice

#ifndef ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__TRAITS_HPP_
#define ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "ised7881_service/srv/detail/ised7881_service__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace ised7881_service
{

namespace srv
{

inline void to_flow_style_yaml(
  const Ised7881Service_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: input
  {
    out << "input: ";
    rosidl_generator_traits::value_to_yaml(msg.input, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Ised7881Service_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: input
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "input: ";
    rosidl_generator_traits::value_to_yaml(msg.input, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Ised7881Service_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ised7881_service

namespace rosidl_generator_traits
{

[[deprecated("use ised7881_service::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ised7881_service::srv::Ised7881Service_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  ised7881_service::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ised7881_service::srv::to_yaml() instead")]]
inline std::string to_yaml(const ised7881_service::srv::Ised7881Service_Request & msg)
{
  return ised7881_service::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ised7881_service::srv::Ised7881Service_Request>()
{
  return "ised7881_service::srv::Ised7881Service_Request";
}

template<>
inline const char * name<ised7881_service::srv::Ised7881Service_Request>()
{
  return "ised7881_service/srv/Ised7881Service_Request";
}

template<>
struct has_fixed_size<ised7881_service::srv::Ised7881Service_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ised7881_service::srv::Ised7881Service_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ised7881_service::srv::Ised7881Service_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace ised7881_service
{

namespace srv
{

inline void to_flow_style_yaml(
  const Ised7881Service_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: reversed_text
  {
    out << "reversed_text: ";
    rosidl_generator_traits::value_to_yaml(msg.reversed_text, out);
    out << ", ";
  }

  // member: runtime
  {
    out << "runtime: ";
    rosidl_generator_traits::value_to_yaml(msg.runtime, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Ised7881Service_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: reversed_text
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reversed_text: ";
    rosidl_generator_traits::value_to_yaml(msg.reversed_text, out);
    out << "\n";
  }

  // member: runtime
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "runtime: ";
    rosidl_generator_traits::value_to_yaml(msg.runtime, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Ised7881Service_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace ised7881_service

namespace rosidl_generator_traits
{

[[deprecated("use ised7881_service::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const ised7881_service::srv::Ised7881Service_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  ised7881_service::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use ised7881_service::srv::to_yaml() instead")]]
inline std::string to_yaml(const ised7881_service::srv::Ised7881Service_Response & msg)
{
  return ised7881_service::srv::to_yaml(msg);
}

template<>
inline const char * data_type<ised7881_service::srv::Ised7881Service_Response>()
{
  return "ised7881_service::srv::Ised7881Service_Response";
}

template<>
inline const char * name<ised7881_service::srv::Ised7881Service_Response>()
{
  return "ised7881_service/srv/Ised7881Service_Response";
}

template<>
struct has_fixed_size<ised7881_service::srv::Ised7881Service_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<ised7881_service::srv::Ised7881Service_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<ised7881_service::srv::Ised7881Service_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<ised7881_service::srv::Ised7881Service>()
{
  return "ised7881_service::srv::Ised7881Service";
}

template<>
inline const char * name<ised7881_service::srv::Ised7881Service>()
{
  return "ised7881_service/srv/Ised7881Service";
}

template<>
struct has_fixed_size<ised7881_service::srv::Ised7881Service>
  : std::integral_constant<
    bool,
    has_fixed_size<ised7881_service::srv::Ised7881Service_Request>::value &&
    has_fixed_size<ised7881_service::srv::Ised7881Service_Response>::value
  >
{
};

template<>
struct has_bounded_size<ised7881_service::srv::Ised7881Service>
  : std::integral_constant<
    bool,
    has_bounded_size<ised7881_service::srv::Ised7881Service_Request>::value &&
    has_bounded_size<ised7881_service::srv::Ised7881Service_Response>::value
  >
{
};

template<>
struct is_service<ised7881_service::srv::Ised7881Service>
  : std::true_type
{
};

template<>
struct is_service_request<ised7881_service::srv::Ised7881Service_Request>
  : std::true_type
{
};

template<>
struct is_service_response<ised7881_service::srv::Ised7881Service_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__TRAITS_HPP_
