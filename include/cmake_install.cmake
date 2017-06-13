# Install script for directory: /Users/yilu/Projects/mysql-server/include

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Users/yilu/mysql-bin/5.7")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES "/Users/yilu/Projects/mysql-server/include/../libbinlogevents/export/binary_log_types.h")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/Users/yilu/Projects/mysql-server/include/mysql.h"
    "/Users/yilu/Projects/mysql-server/include/mysql_com.h"
    "/Users/yilu/Projects/mysql-server/include/my_command.h"
    "/Users/yilu/Projects/mysql-server/include/mysql_time.h"
    "/Users/yilu/Projects/mysql-server/include/my_list.h"
    "/Users/yilu/Projects/mysql-server/include/my_alloc.h"
    "/Users/yilu/Projects/mysql-server/include/typelib.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin_audit.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin_ftparser.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin_validate_password.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin_keyring.h"
    "/Users/yilu/Projects/mysql-server/include/mysql/plugin_group_replication.h"
    "/Users/yilu/Projects/mysql-server/include/my_dbug.h"
    "/Users/yilu/Projects/mysql-server/include/m_string.h"
    "/Users/yilu/Projects/mysql-server/include/my_sys.h"
    "/Users/yilu/Projects/mysql-server/include/my_xml.h"
    "/Users/yilu/Projects/mysql-server/include/mysql_embed.h"
    "/Users/yilu/Projects/mysql-server/include/my_thread.h"
    "/Users/yilu/Projects/mysql-server/include/my_thread_local.h"
    "/Users/yilu/Projects/mysql-server/include/decimal.h"
    "/Users/yilu/Projects/mysql-server/include/errmsg.h"
    "/Users/yilu/Projects/mysql-server/include/my_global.h"
    "/Users/yilu/Projects/mysql-server/include/my_getopt.h"
    "/Users/yilu/Projects/mysql-server/include/sslopt-longopts.h"
    "/Users/yilu/Projects/mysql-server/include/my_dir.h"
    "/Users/yilu/Projects/mysql-server/include/sslopt-vars.h"
    "/Users/yilu/Projects/mysql-server/include/sslopt-case.h"
    "/Users/yilu/Projects/mysql-server/include/sql_common.h"
    "/Users/yilu/Projects/mysql-server/include/keycache.h"
    "/Users/yilu/Projects/mysql-server/include/m_ctype.h"
    "/Users/yilu/Projects/mysql-server/include/my_compiler.h"
    "/Users/yilu/Projects/mysql-server/include/mysql_com_server.h"
    "/Users/yilu/Projects/mysql-server/include/my_byteorder.h"
    "/Users/yilu/Projects/mysql-server/include/byte_order_generic.h"
    "/Users/yilu/Projects/mysql-server/include/byte_order_generic_x86.h"
    "/Users/yilu/Projects/mysql-server/include/little_endian.h"
    "/Users/yilu/Projects/mysql-server/include/big_endian.h"
    "/Users/yilu/Projects/mysql-server/include/thr_cond.h"
    "/Users/yilu/Projects/mysql-server/include/thr_mutex.h"
    "/Users/yilu/Projects/mysql-server/include/thr_rwlock.h"
    "/Users/yilu/Projects/mysql-server/include/mysql_version.h"
    "/Users/yilu/Projects/mysql-server/include/my_config.h"
    "/Users/yilu/Projects/mysql-server/include/mysqld_ername.h"
    "/Users/yilu/Projects/mysql-server/include/mysqld_error.h"
    "/Users/yilu/Projects/mysql-server/include/sql_state.h"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Development" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mysql" TYPE DIRECTORY FILES "/Users/yilu/Projects/mysql-server/include/mysql/" REGEX "/[^/]*\\.h$" REGEX "/psi\\_abi[^/]*$" EXCLUDE)
endif()

