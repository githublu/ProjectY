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

# Include any dependencies generated for this target.
include sql/CMakeFiles/master.dir/depend.make

# Include the progress variables for this target.
include sql/CMakeFiles/master.dir/progress.make

# Include the compile flags for this target's objects.
include sql/CMakeFiles/master.dir/flags.make

sql/CMakeFiles/master.dir/rpl_master.cc.o: sql/CMakeFiles/master.dir/flags.make
sql/CMakeFiles/master.dir/rpl_master.cc.o: sql/rpl_master.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object sql/CMakeFiles/master.dir/rpl_master.cc.o"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/master.dir/rpl_master.cc.o -c /Users/yilu/Projects/mysql-server/sql/rpl_master.cc

sql/CMakeFiles/master.dir/rpl_master.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/master.dir/rpl_master.cc.i"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/yilu/Projects/mysql-server/sql/rpl_master.cc > CMakeFiles/master.dir/rpl_master.cc.i

sql/CMakeFiles/master.dir/rpl_master.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/master.dir/rpl_master.cc.s"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/yilu/Projects/mysql-server/sql/rpl_master.cc -o CMakeFiles/master.dir/rpl_master.cc.s

sql/CMakeFiles/master.dir/rpl_master.cc.o.requires:

.PHONY : sql/CMakeFiles/master.dir/rpl_master.cc.o.requires

sql/CMakeFiles/master.dir/rpl_master.cc.o.provides: sql/CMakeFiles/master.dir/rpl_master.cc.o.requires
	$(MAKE) -f sql/CMakeFiles/master.dir/build.make sql/CMakeFiles/master.dir/rpl_master.cc.o.provides.build
.PHONY : sql/CMakeFiles/master.dir/rpl_master.cc.o.provides

sql/CMakeFiles/master.dir/rpl_master.cc.o.provides.build: sql/CMakeFiles/master.dir/rpl_master.cc.o


sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o: sql/CMakeFiles/master.dir/flags.make
sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o: sql/rpl_binlog_sender.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/master.dir/rpl_binlog_sender.cc.o -c /Users/yilu/Projects/mysql-server/sql/rpl_binlog_sender.cc

sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/master.dir/rpl_binlog_sender.cc.i"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/yilu/Projects/mysql-server/sql/rpl_binlog_sender.cc > CMakeFiles/master.dir/rpl_binlog_sender.cc.i

sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/master.dir/rpl_binlog_sender.cc.s"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/yilu/Projects/mysql-server/sql/rpl_binlog_sender.cc -o CMakeFiles/master.dir/rpl_binlog_sender.cc.s

sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.requires:

.PHONY : sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.requires

sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.provides: sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.requires
	$(MAKE) -f sql/CMakeFiles/master.dir/build.make sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.provides.build
.PHONY : sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.provides

sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.provides.build: sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o


# Object files for target master
master_OBJECTS = \
"CMakeFiles/master.dir/rpl_master.cc.o" \
"CMakeFiles/master.dir/rpl_binlog_sender.cc.o"

# External object files for target master
master_EXTERNAL_OBJECTS =

sql/libmaster.a: sql/CMakeFiles/master.dir/rpl_master.cc.o
sql/libmaster.a: sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o
sql/libmaster.a: sql/CMakeFiles/master.dir/build.make
sql/libmaster.a: sql/CMakeFiles/master.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libmaster.a"
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -P CMakeFiles/master.dir/cmake_clean_target.cmake
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/master.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sql/CMakeFiles/master.dir/build: sql/libmaster.a

.PHONY : sql/CMakeFiles/master.dir/build

sql/CMakeFiles/master.dir/requires: sql/CMakeFiles/master.dir/rpl_master.cc.o.requires
sql/CMakeFiles/master.dir/requires: sql/CMakeFiles/master.dir/rpl_binlog_sender.cc.o.requires

.PHONY : sql/CMakeFiles/master.dir/requires

sql/CMakeFiles/master.dir/clean:
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -P CMakeFiles/master.dir/cmake_clean.cmake
.PHONY : sql/CMakeFiles/master.dir/clean

sql/CMakeFiles/master.dir/depend:
	cd /Users/yilu/Projects/mysql-server && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server/sql/CMakeFiles/master.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sql/CMakeFiles/master.dir/depend
