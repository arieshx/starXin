//
// Created by haoxin on 2019/8/1.
//

#ifndef STARXIN_DEVICE_API_H
#define STARXIN_DEVICE_API_H

#include "c_runtime_api.h"
#include <assert.h>
#include <string>


namespace starxin {
    namespace runtime {
        class DeviceAPI{
        public:
            virtual ~DeviceAPI(){}
            virtual void *AllocDataSpace(DLContext ctx, size_t size,
                                         size_t alignment) = 0;
            virtual void FreeDataSpace(DLContext ctx, void *ptr) = 0;
            virtual void CopyDataFromTo(const void *from, void *to, size_t size,
                                        DLContext ctx_from, DLContext ctx_to,
                                        DLStreamHandle stream) = 0;
            virtual void StreamSync(DLContext ctx, DLStreamHandle stream) = 0;
        };
    }
}


#endif //STARXIN_DEVICE_API_H
