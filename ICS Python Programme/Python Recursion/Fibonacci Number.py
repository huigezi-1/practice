def fib(n):
    fibn = 0
    if n == 0:
        fibn = 0
    elif n == 1:
        fibn = 1
    else:
        fibn = fib(n-1) + fib(n-2)
    return fibn

if __name__=="__main__":
    a= int(input())
    print(fib(a))
