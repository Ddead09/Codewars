def find_short(s):
    x= ''.join(s).split()
    y=min(x,key=len)
    return len(y)
