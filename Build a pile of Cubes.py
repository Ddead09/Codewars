def find_nb(m):
    s=0
    n=0
    while s<m:
        n=n+1
        s=s+n**3
    return n if m==s else -1
