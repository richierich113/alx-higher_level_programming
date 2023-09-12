#!/usr/bin/python3

'''module with class that inherits from int class
and inverts operators
'''


class MyInt(int):
    '''Overriding base int class'''

    def __eq__(self, other):
        '''makes equal not equal
        Returns
            bool: not equal
        '''
        return str(self) != str(other)

    def __ne__(self, other):
        '''makes not equal equal
        '''
        return str(self) == str(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
