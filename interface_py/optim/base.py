# @Time    : 19-8-12 下午2:33
# @Author  : Aries
# @Site    : 
# @File    : base.py
# @Software: CLion
""""
优化器的基类，所有的优化器方法需要继承此类

"""

from .. import autodiff as ad

try:
    from interface_py.ndarray import ndarray
except ImportError:
    pass


class Base:
    def __init__(self, cost, params, lr=0.1, use_gpu=False):
        self.cost = cost

        self.params = self._copy_to_gpu(params) if use_gpu else params
        self.lr = lr
        grads = ad.gradients(cost, params)  # params是需要求梯度的参数，该函数返回的是所有需要求导数的计算节点，但是和正向传播的w1不是一个node 对象
        grads.insert(0, cost)
        self.use_gpu = use_gpu
        self.executor = ad.Executor(grads, use_gpu=use_gpu)

    def step(self, feed_dict):
        raise NotImplementedError('This method should be implemented by subclasses')

    @staticmethod
    def _copy_to_gpu(params):
        ctx = ndarray.gpu(0)
        gpu_arrays = []
        for param in params:
            param.const = ndarray.array(param.const, ctx=ctx)
            gpu_arrays.append(param)
        return gpu_arrays
