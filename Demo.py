import logging

my_logger = logging.getLogger('Demo')
my_logger.setLevel(logging.WARN)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fileHandler = logging.FileHandler('Demo.log')
fileHandler.setFormatter(formatter)

my_logger.addHandler(fileHandler)


def reverseList(input_list):
    try:
        my_logger.info('Just Entered into the function')
        my_logger.debug('Input List is {}'.format(input_list))
        for i in range(len(input_list) - 1):
            input_list[i], input_list[len(input_list) - i - 1] = input_list[len(input_list) - i - 1], input_list[i]
            my_logger.debug('After Certain Changes input list is {}'.format(input_list))
        my_logger.info('Just coming out of the function')
    except TypeError:
        my_logger.exception('Type Erroe!!!')
    else:
        return input_list


ip_list = [1, 4, 5, 2, 5, 7, 8, 10, 11, 'q']
my_logger.error(ip_list)
op_list = reverseList(ip_list)
my_logger.error(op_list)