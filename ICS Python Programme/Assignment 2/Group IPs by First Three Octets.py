'''
def group_by_prefix(ip_list):
    groups = []

    for ip in ip_list:
        parts = ip.split(".")
        frefix = ".".join(parts[:3])
        found = False

        for group in groups:

            if group and group[0].startswith(prefix):
                group.append(ip)
                found = True
                break

            if not found:
                groups.append([ip])

    return groups

if __name__ == "__main__":
    s = input().strip()

    if s.startswith("[") and s.endswith("]"):
        content = s[1:-1].strip()

        if content:
            ip_list = [item.strip().strip("'\"") for item in content.split(',')]
        else:
            ip_list = []
    else:
        ip_list = []

    result = group_by_prefix(ip_list)
    print(result)
'''
def group_by_prefix(ip_list):
    groups = []

    for ip in ip_list:
        parts = ip.split(".")
        prefix = ".".join(parts[:3])
        found = False

        for group in groups:
            # 修正：直接比较前缀是否相等
            if group and ".".join(group[0].split(".")[:3]) == prefix:
                group.append(ip)
                found = True
                break

        if not found:
            groups.append([ip])

    return groups


if __name__ == "__main__":
    s = input().strip()

    if s.startswith("[") and s.endswith("]"):
        content = s[1:-1].strip()

        if content:
            ip_list = [item.strip().strip("'\"") for item in content.split(',')]
        else:
            ip_list = []
    else:
        ip_list = []

    result = group_by_prefix(ip_list)
    print(result)
