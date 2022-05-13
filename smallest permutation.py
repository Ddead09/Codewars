#Though there are multiple variations of test cases there are 4 vital cases that is being explored here
def min_permutation(n):
    n=str(n)
    if '0' not in n:
        x= ''.join((sorted(n)))
        return int(x)
    if n==''.join(sorted(n)):
        return int(n)
    
    c=n.count('0')
    n=''.join(sorted(n.replace('0','')))
    if n[0]!='-':
        return int(n[0:1]+'0'*c+n[1:])
    else:
        return int('-'+n[1]+'0'*c+n[2:])
