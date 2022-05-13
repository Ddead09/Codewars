def create_phone_number(n):
    x= ''.join(map(str,n))
    return '({}) {}-{}'.format(x[:3],x[3:6],x[6:])
