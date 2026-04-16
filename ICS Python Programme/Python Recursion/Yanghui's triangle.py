def triangle(n):
    result = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(1,i):
            row [j] = result[i - 1 ][j - 1 ] + result[i - 1][j]
        result.append(row)
    return result

if __name__ == "__main__":
    n114514 = int(input())
    print(triangle(n114514))
