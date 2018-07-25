import functools
def addOne (x):
    x = [68, 7623, 7142, 967, 5]
    x = filter(lambda x: x > 100, x)
    x = map(lambda x: 1, x)
    x = functools.reduce(sum, x)
    return x