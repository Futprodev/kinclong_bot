# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_vac_bot_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED vac_bot_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(vac_bot_FOUND FALSE)
  elseif(NOT vac_bot_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(vac_bot_FOUND FALSE)
  endif()
  return()
endif()
set(_vac_bot_CONFIG_INCLUDED TRUE)

# output package information
if(NOT vac_bot_FIND_QUIETLY)
  message(STATUS "Found vac_bot: 0.0.0 (${vac_bot_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'vac_bot' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT vac_bot_DEPRECATED_QUIET)
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(vac_bot_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${vac_bot_DIR}/${_extra}")
endforeach()
