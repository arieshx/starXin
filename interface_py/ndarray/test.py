from ..ndarray import ndarray
from . import gpu_op
import numpy as np


def test_array_set():
    ctx = ndarray.gpu(0)
    shape = (500, 200)
    # oneslike
    arr_x = ndarray.empty(shape, ctx=ctx)
    gpu_op.array_set(arr_x, 1.)
    x = arr_x.asnumpy()
    np.testing.assert_allclose(np.ones(shape), x)
    # zeroslike
    gpu_op.array_set(arr_x, 0.)
    x = arr_x.asnumpy()
    print(x)
    np.testing.assert_allclose(np.zeros(shape), x)

def test_softmax():
    ctx = ndarray.gpu(0)
    shape = (400, 1000)
    x = np.random.uniform(-5, 5, shape).astype(np.float32)
    arr_x = ndarray.array(x, ctx=ctx)
    arr_y = ndarray.empty(shape, ctx=ctx)
    gpu_op.softmax(arr_x, arr_y)
    y = arr_y.asnumpy()
    np.testing.assert_allclose(autodiff.softmax_func(x), y, rtol=1e-5)



test_array_set()