def solution(number):
    l=[]
    for i in range(number):
        if i%5==0 or i%3==0:
            l.append(i)
            
    return sum(l)
