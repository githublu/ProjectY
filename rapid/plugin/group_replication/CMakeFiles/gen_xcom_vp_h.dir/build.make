# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/yilu/Projects/mysql-server

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/yilu/Projects/mysql-server

# Utility rule file for gen_xcom_vp_h.

# Include the progress variables for this target.
include rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/progress.make

rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h: rapid/plugin/group_replication/xdr_gen/xcom_vp.h


rapid/plugin/group_replication/xdr_gen/xcom_vp.h: rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom/xcom_vp.x
rapid/plugin/group_replication/xdr_gen/xcom_vp.h: rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom/xcom_vp_platform.h.gen
rapid/plugin/group_replication/xdr_gen/xcom_vp.h: rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom/xcom_proto_enum.h
rapid/plugin/group_replication/xdr_gen/xcom_vp.h: rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom/xcom_limits.h
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating xdr_gen/xcom_vp.h, xdr_gen/xcom_vp_xdr.c, xdr_gen/xcom_vp_platform.h"
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E copy_if_different /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom//xcom_proto_enum.h /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_proto_enum.h
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E copy_if_different /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom//xcom_limits.h /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_limits.h
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E copy_if_different /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom//xcom_vp.x /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp.x
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E copy_if_different /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/libmysqlgcs/src/bindings/xcom/xcom//xcom_vp_platform.h.gen /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp_platform.h
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E remove -f /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp.h
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && rpcgen -C -h -o /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp.h xcom_vp.x
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && /Applications/CMake.app/Contents/bin/cmake -E remove -f /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp_xdr.c
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen && rpcgen -C -c -o /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/xdr_gen/xcom_vp_xdr.c xcom_vp.x

rapid/plugin/group_replication/xdr_gen/xcom_vp_xdr.c: rapid/plugin/group_replication/xdr_gen/xcom_vp.h
	@$(CMAKE_COMMAND) -E touch_nocreate rapid/plugin/group_replication/xdr_gen/xcom_vp_xdr.c

rapid/plugin/group_replication/xdr_gen/xcom_vp_platform.h: rapid/plugin/group_replication/xdr_gen/xcom_vp.h
	@$(CMAKE_COMMAND) -E touch_nocreate rapid/plugin/group_replication/xdr_gen/xcom_vp_platform.h

gen_xcom_vp_h: rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h
gen_xcom_vp_h: rapid/plugin/group_replication/xdr_gen/xcom_vp.h
gen_xcom_vp_h: rapid/plugin/group_replication/xdr_gen/xcom_vp_xdr.c
gen_xcom_vp_h: rapid/plugin/group_replication/xdr_gen/xcom_vp_platform.h
gen_xcom_vp_h: rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/build.make

.PHONY : gen_xcom_vp_h

# Rule to build all files generated by this target.
rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/build: gen_xcom_vp_h

.PHONY : rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/build

rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/clean:
	cd /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication && $(CMAKE_COMMAND) -P CMakeFiles/gen_xcom_vp_h.dir/cmake_clean.cmake
.PHONY : rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/clean

rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/depend:
	cd /Users/yilu/Projects/mysql-server && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication /Users/yilu/Projects/mysql-server/rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : rapid/plugin/group_replication/CMakeFiles/gen_xcom_vp_h.dir/depend
