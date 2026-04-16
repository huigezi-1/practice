def print_christmas_tree(rows):
    if rows == 0:
        print("Error. Row shall not be 0.")
        return
    
    for i in range(1, rows + 1):
        spaces = rows - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
    
    trunk_spaces = rows - 1
    for _ in range(2):
        print(" " * trunk_spaces + "|")

rows = int(input())
print_christmas_tree(rows)
