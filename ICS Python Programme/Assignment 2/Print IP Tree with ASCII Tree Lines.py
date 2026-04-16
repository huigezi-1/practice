import sys
import ast

def print_ip_tree(ip_tree):
    """
    打印 IP 树的 ASCII 树形结构。
    ip_tree: 嵌套列表，如 [['192', ['168', ['1', ['1']]]], ...]
    """
    # 对顶层节点按字符串排序
    top_nodes = sorted(ip_tree, key=lambda x: x[0])
    n = len(top_nodes)
    for i, node in enumerate(top_nodes):
        # 打印当前根节点的值
        print(node[0])
        # 获取子节点列表并排序
        children = node[1:]
        if not children:
            continue
        sorted_children = sorted(children, key=lambda x: x[0])
        # 判断当前根节点是否为最后一个
        is_last_root = (i == n - 1)
        # 根节点的子节点使用特殊连接符：若根不是最后一个，所有子节点用"├──"；否则用"└──"
        for j, child in enumerate(sorted_children):
            # 对于根的直接子节点，连接符由根节点是否是最后一个决定
            connector = "└──" if is_last_root else "├──"
            # 打印当前子节点
            print(connector + child[0])
            # 递归打印子节点的子节点，此时使用标准规则（根据兄弟位置）
            # 前缀：如果根是最后一个，则子节点前缀为"   "；否则为"│  "
            prefix = "   " if is_last_root else "│  "
            # 该子节点在兄弟中的位置（只有它自己，所以是最后一个）
            _print_subtree(child, prefix, True)

def _print_subtree(node, prefix, is_last):
    """
    递归打印子树（非根节点的子节点）
    node: 当前节点，格式 [value, child1, child2, ...]
    prefix: 当前行前缀（用于缩进和竖线）
    is_last: 当前节点是否是父节点的最后一个子节点（决定连接符）
    """
    children = node[1:]
    if not children:
        return
    sorted_children = sorted(children, key=lambda x: x[0])
    for i, child in enumerate(sorted_children):
        is_last_child = (i == len(sorted_children) - 1)
        # 连接符根据当前节点在父节点中的位置决定
        connector = "└──" if is_last_child else "├──"
        print(prefix + connector + child[0])
        # 下一级前缀：如果当前子节点是最后一个，则用"   "，否则用"│  "
        new_prefix = prefix + ("   " if is_last_child else "│  ")
        _print_subtree(child, new_prefix, is_last_child)

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    ip_tree = ast.literal_eval(data)
    print_ip_tree(ip_tree)
