#!/usr/bin/python3
def print_last_digit(number):
    
    if number >= 0:
        ldig = number % 10
        print(ldig, end='')
        return (ldig)
    else:
       ldig = number % -10
        print(ldig, end='')
        return (ldig)
