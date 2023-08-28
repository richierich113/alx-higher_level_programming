#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    items_in_range = 0
    for indx in range(0, x):
        try:
            element = my_list[indx]
            print(f"{element}", end='')
            items_in_range += 1
        except
            break
    print("")

    return items_in_range


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
