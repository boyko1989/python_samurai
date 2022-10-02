GLOBAL = 'GLOBAL'


def sum_module(a, b):
    return a + b


def mul_module(a, b):
    return a * b


def _im_hidden():
    print('I\'m hidden!')


def get_hidden():
    _im_hidden()

# if __name__ == '__main__':
#      print('Hi there, I am module!')
#      print('Sum of 10 and 10: ', sum_module(10,10))
