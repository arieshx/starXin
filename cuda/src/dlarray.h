//
// Created by haoxin on 2019/7/31.
//

#ifndef STARXIN_DLARRAY_H
#define STARXIN_DLARRAY_H

#ifdef __cplusplus
#define DLSYS_EXTERN_C extern "C"
#else
#define STARXIN_EXTERN_C
#endif


#include <cstddef>
#include <cstdint>

DLSYS_EXTERN_C {
typedef enum {
    kCPU = 1,
    kGPU = 2,
}DLDeviceType;

typedef struct {
    int device_id;
    DLDeviceType device_type;
}DLContext;

// 无缝切换的数据结构
typedef struct {
void *data;    // 数据
DLContext ctx; // 上下文
int ndim;   // 维度
int64_t *shape;  // 每一个维度的大小
}DLArray;
}


#endif //STARXIN_DLARRAY_H
