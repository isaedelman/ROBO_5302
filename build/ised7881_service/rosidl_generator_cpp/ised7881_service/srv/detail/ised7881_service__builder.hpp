// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ised7881_service:srv/Ised7881Service.idl
// generated code does not contain a copyright notice

#ifndef ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__BUILDER_HPP_
#define ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ised7881_service/srv/detail/ised7881_service__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ised7881_service
{

namespace srv
{

namespace builder
{

class Init_Ised7881Service_Request_input
{
public:
  Init_Ised7881Service_Request_input()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ised7881_service::srv::Ised7881Service_Request input(::ised7881_service::srv::Ised7881Service_Request::_input_type arg)
  {
    msg_.input = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ised7881_service::srv::Ised7881Service_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ised7881_service::srv::Ised7881Service_Request>()
{
  return ised7881_service::srv::builder::Init_Ised7881Service_Request_input();
}

}  // namespace ised7881_service


namespace ised7881_service
{

namespace srv
{

namespace builder
{

class Init_Ised7881Service_Response_runtime
{
public:
  explicit Init_Ised7881Service_Response_runtime(::ised7881_service::srv::Ised7881Service_Response & msg)
  : msg_(msg)
  {}
  ::ised7881_service::srv::Ised7881Service_Response runtime(::ised7881_service::srv::Ised7881Service_Response::_runtime_type arg)
  {
    msg_.runtime = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ised7881_service::srv::Ised7881Service_Response msg_;
};

class Init_Ised7881Service_Response_reversed_text
{
public:
  Init_Ised7881Service_Response_reversed_text()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Ised7881Service_Response_runtime reversed_text(::ised7881_service::srv::Ised7881Service_Response::_reversed_text_type arg)
  {
    msg_.reversed_text = std::move(arg);
    return Init_Ised7881Service_Response_runtime(msg_);
  }

private:
  ::ised7881_service::srv::Ised7881Service_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ised7881_service::srv::Ised7881Service_Response>()
{
  return ised7881_service::srv::builder::Init_Ised7881Service_Response_reversed_text();
}

}  // namespace ised7881_service

#endif  // ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__BUILDER_HPP_
