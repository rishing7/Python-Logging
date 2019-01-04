import logging


def add(x, y):
    """ Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x // y


num_1 = 10
num_2 = 2

add_result = add(num_1, num_2)
logging.error(add_result)

sub_result = subtract(num_1, num_2)
logging.error(sub_result)

mul_result = multiply(num_1, num_2)
logging.error(mul_result)

div_result = divide(num_1, num_2)
logging.error(div_result)
