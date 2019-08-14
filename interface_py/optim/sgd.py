# @Time    : 19-8-12 下午2:34
# @Author  : Aries
# @Site    : 
# @File    : sgd.py
# @Software: CLion

import numpy as np
from .base import Base

try:
    from ..ndarray import gpu_op, ndarray
except ImportError:
    pass


class SGD(Base):
    def __init__(self, cost, params, lr=0.1, momentum=0.9, use_gpu=False):
        super().__init__(cost, params, lr=lr, use_gpu=use_gpu)
        self.momentum = momentum
        if use_gpu:
            self.velocity = [ndarray.array(np.zeros_like(param.const.asnumpy()), ctx=ndarray.gpu(0))
                             for param in params]
        else:
            self.velocity = [np.zeros_like(param.const) for param in params]

    def step(self, feed_dict):
        exe_output = self.executor.run(feed_dict)
        for i in range(len(self.params)):
            if self.use_gpu:
                gpu_op.matrix_elementwise_multiply_by_const(self.velocity[i], self.momentum, self.velocity[i])
                ndarray1 = ndarray.empty(exe_output[1 + i].shape)
                ndarray1._sync_copyfrom(exe_output[1+i].asnumpy())
                gpu_op.matrix_elementwise_multiply_by_const(exe_output[1 + i], -self.lr, exe_output[1 + i])
                ndarray2 = ndarray.empty(exe_output[1 + i].shape)
                ndarray2._sync_copyfrom(exe_output[1+i].asnumpy())
                if self.check_if_change(ndarray1, ndarray2):
                    pass
                else:
                    raise('梯度没有改变')
                gpu_op.matrix_elementwise_add(self.velocity[i], exe_output[1 + i], self.velocity[i])

                gpu_op.matrix_elementwise_add(self.params[i].const, self.velocity[i], self.params[i].const)
            else:
                self.velocity[i] = self.momentum * self.velocity[i] - self.lr * exe_output[1 + i]
                self.params[i].const += self.velocity[i]

        cost = exe_output[0]
        if self.use_gpu:
            cost = cost.asnumpy()
        return cost

    def check_if_change(self, ndarray1, ndarray2):
        array1 = ndarray1.asnumpy()
        array2 = ndarray2.asnumpy()
        return not (array1 == array2).all()