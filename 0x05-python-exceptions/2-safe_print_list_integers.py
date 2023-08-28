#!/usr/bin/python3

#  Prints the first x elements of a list and only integers.
# Handles ValueError and TypeError exceptions but not IndexError
# exception so an x out of range error will show exception in
# Traceback
def safe_print_list_integers(my_list=[], x=0):
    print_num = 0
    for indx in range(0, x):
        try:
            item = my_list[indx]
            print("{:d}".format(item), end='')
            print_num += 1
        except ValueError as ie:
            continue
        except TypeError as e:
            continue
    print("")
    return print_num


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
