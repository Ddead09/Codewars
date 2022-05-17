#Instead of using iterations to find the number od squares just use the formula
def count_squares(n):
    return int((n*(n+1)*(2*n+1))//6)
