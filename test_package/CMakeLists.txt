project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(PostgreSQL REQUIRED)

add_executable(example example.cpp)

target_include_directories(example PRIVATE ${PostgreSQL_INCLUDE_DIRS})
link_libraries(${PostgreSQL_LIBRARY_DIRS})
target_link_libraries(example ${CONAN_LIBS} ${PostgreSQL_LIBRARIES})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
