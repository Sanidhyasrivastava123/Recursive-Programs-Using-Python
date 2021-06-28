def fibo(n):
    assert n>=0 and int(n)==n ,'Fibonacci Number cannot be negative'
    if n in [0,1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))
