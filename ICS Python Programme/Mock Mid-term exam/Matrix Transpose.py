import ast

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
    
matrix = ast.literal_eval(input())
print(transpose(matrix))
