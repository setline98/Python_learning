
import math as math
import numpy as np


def main():
    numbers = [[63, 128],
               [100, 32]]
    numbers = np.reshape(numbers, 4)
    array_of_functions = [[func0, func1],
                          [func2, func3]]
    array_of_functions = np.reshape(array_of_functions, 4)
    _map = list(map(lambda x, func: func(x), numbers, array_of_functions))
    result = np.reshape(_map, (2, 2))
    print(result)
    return 0

def func0(number):
    output = number * 3.14
    return output
def func1(number):
    output = number * math.pi
    return output
def func2(number):
    output = number*4
    return output
def func3(number):
    output = math.sqrt(number)
    return output

if __name__ == '__main__':
    main()
