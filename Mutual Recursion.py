def f(n):
    if n==0:
        valf=1
    else:
        valf=n-m(f(n-1))
    return valf

def m(n):
    if n==0:
        valm=0
    else:
        valm=n-f(m(n-1))
    return valm
