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
include sql/CMakeFiles/udf_example.dir/depend.make

# Include the progress variables for this target.
include sql/CMakeFiles/udf_example.dir/progress.make

# Include the compile flags for this target's objects.
include sql/CMakeFiles/udf_example.dir/flags.make

sql/CMakeFiles/udf_example.dir/udf_example.cc.o: sql/CMakeFiles/udf_example.dir/flags.make
sql/CMakeFiles/udf_example.dir/udf_example.cc.o: sql/udf_example.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object sql/CMakeFiles/udf_example.dir/udf_example.cc.o"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/udf_example.dir/udf_example.cc.o -c /Users/yilu/Projects/mysql-server/sql/udf_example.cc

sql/CMakeFiles/udf_example.dir/udf_example.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/udf_example.dir/udf_example.cc.i"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/yilu/Projects/mysql-server/sql/udf_example.cc > CMakeFiles/udf_example.dir/udf_example.cc.i

sql/CMakeFiles/udf_example.dir/udf_example.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/udf_example.dir/udf_example.cc.s"
	cd /Users/yilu/Projects/mysql-server/sql && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/yilu/Projects/mysql-server/sql/udf_example.cc -o CMakeFiles/udf_example.dir/udf_example.cc.s

sql/CMakeFiles/udf_example.dir/udf_example.cc.o.requires:

.PHONY : sql/CMakeFiles/udf_example.dir/udf_example.cc.o.requires

sql/CMakeFiles/udf_example.dir/udf_example.cc.o.provides: sql/CMakeFiles/udf_example.dir/udf_example.cc.o.requires
	$(MAKE) -f sql/CMakeFiles/udf_example.dir/build.make sql/CMakeFiles/udf_example.dir/udf_example.cc.o.provides.build
.PHONY : sql/CMakeFiles/udf_example.dir/udf_example.cc.o.provides

sql/CMakeFiles/udf_example.dir/udf_example.cc.o.provides.build: sql/CMakeFiles/udf_example.dir/udf_example.cc.o


# Object files for target udf_example
udf_example_OBJECTS = \
"CMakeFiles/udf_example.dir/udf_example.cc.o"

# External object files for target udf_example
udf_example_EXTERNAL_OBJECTS =

sql/udf_example.so: sql/CMakeFiles/udf_example.dir/udf_example.cc.o
sql/udf_example.so: sql/CMakeFiles/udf_example.dir/build.make
sql/udf_example.so: sql/mysqld-debug
sql/udf_example.so: sql/CMakeFiles/udf_example.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module udf_example.so"
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/udf_example.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sql/CMakeFiles/udf_example.dir/build: sql/udf_example.so

.PHONY : sql/CMakeFiles/udf_example.dir/build

sql/CMakeFiles/udf_example.dir/requires: sql/CMakeFiles/udf_example.dir/udf_example.cc.o.requires

.PHONY : sql/CMakeFiles/udf_example.dir/requires

sql/CMakeFiles/udf_example.dir/clean:
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -P CMakeFiles/udf_example.dir/cmake_clean.cmake
.PHONY : sql/CMakeFiles/udf_example.dir/clean

sql/CMakeFiles/udf_example.dir/depend:
	cd /Users/yilu/Projects/mysql-server && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server/sql/CMakeFiles/udf_example.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sql/CMakeFiles/udf_example.dir/depend
