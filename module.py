GLOBAL = 'GLOBAL'


def sum_module(a, b):
    return a + b


def mul_module(a, b):
    return a * b


def _im_hidden():
    print('I\'m hidden!')


def main():
    _im_hidden()
    print(sum_module(1, 3))


if __name__ == '__main__':
    main()
    # print('Hi there, I am module!')
    # assert sum_module(3, 6) == 1
    # print('Sum of 10 and 10: ', sum_module(10, 10))
