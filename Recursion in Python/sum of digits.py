def sumod(n):
    assert n>=0 and int(n)==n,'the number should be positive'
    if n==0:
        return n
    else:
        return int(n%10) + sumod(int(n//10))

print(sumod(123))
