#This program removes parenthesis as well as the elements inside it
def remove_parentheses(s):
    r=''
    p=0
    for ch in s:
        if ch=='(':
            p=p+1
            r=r+''
            
        elif (ch==')') and p:
            r=r+''
            p=p-1
            
        elif not p:
            r +=ch
    return r   
