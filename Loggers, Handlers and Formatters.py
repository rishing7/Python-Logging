"""
    Here we are creating instance variables those are unique to each employee.
    There are two ways to call a method.
"""
import logging

""" To do the following steps we use logger, handler and formatter"""
# logger.basicConfig(filename='employee.log', level=logger.INFO,
#                     format='%(name)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)   # Level of logger

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('name.log')  # Set log file name
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

""" Stream handler is like file handler that helps to get output over the console."""

# stream_handler = logger.StreamHandler()
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


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
    try:
        res = x//y
    except ZeroDivisionError:
        logger.error("Tried to divide by zero")
    else:
        return res


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(add_result)

sub_result = subtract(num_1, num_2)
logger.debug(sub_result)

mul_result = multiply(num_1, num_2)
logger.debug(mul_result)

div_result = divide(num_1, num_2)
logger.debug(div_result)
