//
// Created by haoxin on 2019/8/1.
//


#include "test_cpu.h"
using namespace std;

int test_cpu_fn() {

    DLContext ctx;
    ctx.device_id = 0;
    ctx.device_type =kCPU;

    int ndim = 2;

    int64_t shape[]={4,2};

    auto *out = new DLArrayHandle();

    DLArrayAlloc(shape,ndim,ctx, out);

    cout<<(*out)->shape[0]<<" "<<(*out)->shape[1]<<endl;

    return 0;
}