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

# Utility rule file for GenServerSource.

# Include the progress variables for this target.
include sql/CMakeFiles/GenServerSource.dir/progress.make

sql/CMakeFiles/GenServerSource: sql/sql_yacc.h
sql/CMakeFiles/GenServerSource: sql/sql_yacc.cc
sql/CMakeFiles/GenServerSource: sql/sql_hints.yy.h
sql/CMakeFiles/GenServerSource: sql/sql_hints.yy.cc
sql/CMakeFiles/GenServerSource: sql/lex_hash.h


sql/sql_yacc.cc: sql/sql_yacc.yy
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating sql_yacc.cc, sql_yacc.h"
	cd /Users/yilu/Projects/mysql-server/sql && /usr/bin/bison --name-prefix=MYSQL --yacc --output=/Users/yilu/Projects/mysql-server/sql/sql_yacc.cc --defines=/Users/yilu/Projects/mysql-server/sql/sql_yacc.h /Users/yilu/Projects/mysql-server/sql/sql_yacc.yy

sql/sql_yacc.h: sql/sql_yacc.cc
	@$(CMAKE_COMMAND) -E touch_nocreate sql/sql_yacc.h

sql/sql_hints.yy.cc: sql/sql_hints.yy
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating sql_hints.yy.cc, sql_hints.yy.h"
	cd /Users/yilu/Projects/mysql-server/sql && /usr/bin/bison --name-prefix=HINT_PARSER_ --yacc --output=/Users/yilu/Projects/mysql-server/sql/sql_hints.yy.cc --defines=/Users/yilu/Projects/mysql-server/sql/sql_hints.yy.h /Users/yilu/Projects/mysql-server/sql/sql_hints.yy

sql/sql_hints.yy.h: sql/sql_hints.yy.cc
	@$(CMAKE_COMMAND) -E touch_nocreate sql/sql_hints.yy.h

sql/lex_hash.h: sql/gen_lex_hash
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/Users/yilu/Projects/mysql-server/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating lex_hash.h"
	cd /Users/yilu/Projects/mysql-server/sql && ./gen_lex_hash > lex_hash.h

GenServerSource: sql/CMakeFiles/GenServerSource
GenServerSource: sql/sql_yacc.cc
GenServerSource: sql/sql_yacc.h
GenServerSource: sql/sql_hints.yy.cc
GenServerSource: sql/sql_hints.yy.h
GenServerSource: sql/lex_hash.h
GenServerSource: sql/CMakeFiles/GenServerSource.dir/build.make

.PHONY : GenServerSource

# Rule to build all files generated by this target.
sql/CMakeFiles/GenServerSource.dir/build: GenServerSource

.PHONY : sql/CMakeFiles/GenServerSource.dir/build

sql/CMakeFiles/GenServerSource.dir/clean:
	cd /Users/yilu/Projects/mysql-server/sql && $(CMAKE_COMMAND) -P CMakeFiles/GenServerSource.dir/cmake_clean.cmake
.PHONY : sql/CMakeFiles/GenServerSource.dir/clean

sql/CMakeFiles/GenServerSource.dir/depend:
	cd /Users/yilu/Projects/mysql-server && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server /Users/yilu/Projects/mysql-server/sql /Users/yilu/Projects/mysql-server/sql/CMakeFiles/GenServerSource.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sql/CMakeFiles/GenServerSource.dir/depend
