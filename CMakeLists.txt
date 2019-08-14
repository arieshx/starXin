cmake_minimum_required(VERSION 3.8)
project(starXin)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        main.cpp
#        src/dlarray.h
#        src/device_api.h
#        src/c_runtime_api.h
#        src/c_runtime_api.cpp
#        src/cpu_device_api.h
#        src/cpu_device_api.cpp
#        src/runtime_base.h
#        test/test_cpu.h
#        test/test_cpu.cpp
#        # src/cuda_device_api.h src/cuda_device_api.cpp
 )
#include_directories(/usr/local/cuda/include)
add_executable(starXin ${SOURCE_FILES})