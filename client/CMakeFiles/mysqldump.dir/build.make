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
include client/CMakeFiles/mysqldump.dir/depend.make

# Include the progress variables for this target.
include client/CMakeFiles/mysqldump.dir/progress.make

# Include the compile flags for this target's objects.
include client/CMakeFiles/mysqldump.dir/flags.make

client/CMakeFiles/mysqldump.dir/mysqldump.c.o: client/CMakeFiles/mysqldump.dir/flags.make
client/CMakeFiles/mysqldump.dir/mysqldump.c.o: client/mysqldump.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object client/CMakeFiles/mysqldump.dir/mysqldump.c.o"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mysqldump.dir/mysqldump.c.o   -c /Users/yilu/Projects/mysql-server/client/mysqldump.c

client/CMakeFiles/mysqldump.dir/mysqldump.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mysqldump.dir/mysqldump.c.i"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yilu/Projects/mysql-server/client/mysqldump.c > CMakeFiles/mysqldump.dir/mysqldump.c.i

client/CMakeFiles/mysqldump.dir/mysqldump.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mysqldump.dir/mysqldump.c.s"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yilu/Projects/mysql-server/client/mysqldump.c -o CMakeFiles/mysqldump.dir/mysqldump.c.s

client/CMakeFiles/mysqldump.dir/mysqldump.c.o.requires:

.PHONY : client/CMakeFiles/mysqldump.dir/mysqldump.c.o.requires

client/CMakeFiles/mysqldump.dir/mysqldump.c.o.provides: client/CMakeFiles/mysqldump.dir/mysqldump.c.o.requires
	$(MAKE) -f client/CMakeFiles/mysqldump.dir/build.make client/CMakeFiles/mysqldump.dir/mysqldump.c.o.provides.build
.PHONY : client/CMakeFiles/mysqldump.dir/mysqldump.c.o.provides

client/CMakeFiles/mysqldump.dir/mysqldump.c.o.provides.build: client/CMakeFiles/mysqldump.dir/mysqldump.c.o


client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o: client/CMakeFiles/mysqldump.dir/flags.make
client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o: sql-common/my_user.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o   -c /Users/yilu/Projects/mysql-server/sql-common/my_user.c

client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.i"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/yilu/Projects/mysql-server/sql-common/my_user.c > CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.i

client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.s"
	cd /Users/yilu/Projects/mysql-server/client && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/yilu/Projects/mysql-server/sql-common/my_user.c -o CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.s

client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.requires:

.PHONY : client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.requires

client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.provides: client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.requires
	$(MAKE) -f client/CMakeFiles/mysqldump.dir/build.make client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.provides.build
.PHONY : client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.provides

client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.provides.build: client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o


# Object files for target mysqldump
mysqldump_OBJECTS = \
"CMakeFiles/mysqldump.dir/mysqldump.c.o" \
"CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o"

# External object files for target mysqldump
mysqldump_EXTERNAL_OBJECTS =

client/mysqldump: client/CMakeFiles/mysqldump.dir/mysqldump.c.o
client/mysqldump: client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o
client/mysqldump: client/CMakeFiles/mysqldump.dir/build.make
client/mysqldump: libmysql/libmysqlclient.a
client/mysqldump: client/CMakeFiles/mysqldump.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable mysqldump"
	cd /Users/yilu/Projects/mysql-server/client && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mysqldump.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
client/CMakeFiles/mysqldump.dir/build: client/mysqldump

.PHONY : client/CMakeFiles/mysqldump.dir/build

client/CMakeFiles/mysqldump.dir/requires: client/CMakeFiles/mysqldump.dir/mysqldump.c.o.requires
client/CMakeFiles/mysqldump.dir/requires: client/CMakeFiles/mysqldump.dir/__/sql-common/my_user.c.o.requires

.PHONY : client/CMakeFiles/mysqldump.dir/requires

client/CMakeFiles/mysqldump.dir/clean:
	cd /Users/yilu/Projects/mysql-server/client && $(CMAKE_COMMAND) -P CMakeFiles/mysqldump.dir/cmake_clean.cmake
.PHONY : client/CMakeFiles/mysqldump.dir/clean

client/CMakeFiles/mysqldump.dir/depend:
	cd /Users/yilu/Projects/mysql-server && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/client /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/client /Users/yilu/Projects/mysql-server/client/CMakeFiles/mysqldump.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : client/CMakeFiles/mysqldump.dir/depend
