//
// Created by haoxin on 2019/8/1.
//

#ifndef STARXIN_CPU_DEVICE_API_H
#define STARXIN_CPU_DEVICE_API_H

// #include "c_runtime_api.h"
#include "device_api.h"
#include <assert.h>
#include <string>

namespace starxin{
    namespace runtime{
        class CPUDeviceAPI:public DeviceAPI{
        public:
            void *AllocDataSpace(DLContext ctx, size_t size, size_t alignment) final;
            void FreeDataSpace(DLContext ctx, void *ptr) final;
            void CopyDataFromTo(const void *from, void *to, size_t size,
                                DLContext ctx_from, DLContext ctx_to, DLStreamHandle stream) final;
            void StreamSync(DLContext ctx, DLStreamHandle stream) final;
        };
    }
}

#endif //STARXIN_CPU_DEVICE_API_H
