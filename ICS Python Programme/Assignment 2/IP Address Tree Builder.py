import ast
import sys

def build_ip_tree(ip_list):
    # 去重并保持原始顺序
    unique_ips = list(dict.fromkeys(ip_list))
    # 根的子节点列表，每个子节点格式为 [octet, children]
    root_children = []

    for ip in unique_ips:
        parts = ip.split('.')
        if len(parts) != 4:          # 只处理标准 IPv4 地址
            continue

        current_children = root_children
        for part in parts:
            found = False
            # 在当前层的子节点列表中查找是否已存在该八位组
            for node in current_children:
                if node[0] == part:
                    # 找到，移动到该节点的子节点列表
                    current_children = node[1]
                    found = True
                    break
            if not found:
                # 未找到，创建新节点并追加到当前层末尾（保持首次出现顺序）
                new_node = [part, []]
                current_children.append(new_node)
                current_children = new_node[1]

    # 递归将内部结构转换为题目要求的嵌套列表格式
    def convert(node):
        # node: [octet, children_list]
        if not node[1]:               # 叶子节点
            return [node[0]]
        else:                         # 非叶子节点
            return [node[0]] + [convert(child) for child in node[1]]

    # 转换根的所有子节点
    return [convert(child) for child in root_children]

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    ip_list = ast.literal_eval(data)
    result = build_ip_tree(ip_list)
    print(result)
