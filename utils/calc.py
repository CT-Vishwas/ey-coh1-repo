PI = 3.1412
def add(a: int,b: int) -> int:
    '''
    Returns sum of a & b
    '''
    return a + b

def sub(a: int,b: int) -> int:
    '''
    Returns difference of a & b
    '''
    return a - b

def add_all(*args: float) -> float:
    return sum(args)

# if __name__ == '__main__':
#     print(add(2,3))
#     print(sub(6,2))


print(add(2,3))
print(sub(6,2))
