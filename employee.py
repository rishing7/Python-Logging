"""
    Here we are creating instance variables those are unique to each employee.
    There are two ways to call a method.
"""
import logging

logging.basicConfig(filename='Demo.log', level=logging.ERROR,
                    format='%(name)s:%(message)s')


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # print('Created employee: {} - {}'.format(self.fullName, self.email))
        logging.info('Created employee: {} - {}'.format(self.fullName, self.email))

    @property  # @property is used so that email can be called instead email().
    def fullName(self):
        return '{} {}'.format(self.fname, self.lname)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)


emp_1 = Employee('rishikesh', 'rishi')
emp_2 = Employee('aaa', 'bbb')
emp_3 = Employee('zzz', 'yyy')