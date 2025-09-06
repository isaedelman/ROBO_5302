// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from ised7881_service:srv/Ised7881Service.idl
// generated code does not contain a copyright notice

#ifndef ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_HPP_
#define ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__ised7881_service__srv__Ised7881Service_Request __attribute__((deprecated))
#else
# define DEPRECATED__ised7881_service__srv__Ised7881Service_Request __declspec(deprecated)
#endif

namespace ised7881_service
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Ised7881Service_Request_
{
  using Type = Ised7881Service_Request_<ContainerAllocator>;

  explicit Ised7881Service_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->input = "";
    }
  }

  explicit Ised7881Service_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : input(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->input = "";
    }
  }

  // field types and members
  using _input_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _input_type input;

  // setters for named parameter idiom
  Type & set__input(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->input = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ised7881_service__srv__Ised7881Service_Request
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ised7881_service__srv__Ised7881Service_Request
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Ised7881Service_Request_ & other) const
  {
    if (this->input != other.input) {
      return false;
    }
    return true;
  }
  bool operator!=(const Ised7881Service_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Ised7881Service_Request_

// alias to use template instance with default allocator
using Ised7881Service_Request =
  ised7881_service::srv::Ised7881Service_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ised7881_service


#ifndef _WIN32
# define DEPRECATED__ised7881_service__srv__Ised7881Service_Response __attribute__((deprecated))
#else
# define DEPRECATED__ised7881_service__srv__Ised7881Service_Response __declspec(deprecated)
#endif

namespace ised7881_service
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Ised7881Service_Response_
{
  using Type = Ised7881Service_Response_<ContainerAllocator>;

  explicit Ised7881Service_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reversed_text = "";
      this->runtime = 0.0;
    }
  }

  explicit Ised7881Service_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : reversed_text(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reversed_text = "";
      this->runtime = 0.0;
    }
  }

  // field types and members
  using _reversed_text_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _reversed_text_type reversed_text;
  using _runtime_type =
    double;
  _runtime_type runtime;

  // setters for named parameter idiom
  Type & set__reversed_text(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->reversed_text = _arg;
    return *this;
  }
  Type & set__runtime(
    const double & _arg)
  {
    this->runtime = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__ised7881_service__srv__Ised7881Service_Response
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__ised7881_service__srv__Ised7881Service_Response
    std::shared_ptr<ised7881_service::srv::Ised7881Service_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Ised7881Service_Response_ & other) const
  {
    if (this->reversed_text != other.reversed_text) {
      return false;
    }
    if (this->runtime != other.runtime) {
      return false;
    }
    return true;
  }
  bool operator!=(const Ised7881Service_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Ised7881Service_Response_

// alias to use template instance with default allocator
using Ised7881Service_Response =
  ised7881_service::srv::Ised7881Service_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace ised7881_service

namespace ised7881_service
{

namespace srv
{

struct Ised7881Service
{
  using Request = ised7881_service::srv::Ised7881Service_Request;
  using Response = ised7881_service::srv::Ised7881Service_Response;
};

}  // namespace srv

}  // namespace ised7881_service

#endif  // ISED7881_SERVICE__SRV__DETAIL__ISED7881_SERVICE__STRUCT_HPP_
