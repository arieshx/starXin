from .utils import sum_node_list
from .utils import find_topo_sort
from .autodiff import ones_like


# 反向求导
def gradients(output_node, node_list):
    node_to_output_grads_list = {}  # node到ouput的梯度，之所以是列表，是因为梯度可能从output从不同的图路径到达，因此存放的是output从不同的路径传播过来的梯度有
    node_to_output_grads_list[output_node] = [ones_like(output_node)]
    # a map from node to the gradient of that node
    node_to_output_grad = {}
    reverse_topo_order = reversed(find_topo_sort([output_node]))
    for node in reverse_topo_order:
        output_grad = sum_node_list(node_to_output_grads_list[node])
        node_to_output_grad[node] = output_grad  # node 当前节点，output对当前节点的梯度，

        input_grads_list = node.op.gradient(node, output_grad)
        for i in range(len(node.inputs)):
            if node.inputs[i] not in node_to_output_grads_list:
                node_to_output_grads_list[node.inputs[i]] = []
            node_to_output_grads_list[node.inputs[i]].append(input_grads_list[i])

    grad_node_list = [node_to_output_grad[node] for node in node_list]
    return grad_node_list