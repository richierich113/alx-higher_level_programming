#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for item in range(0, x):
        try:
            element = my_list[item]
            print(f"{element}", end='')
        except IndexError as ie:
            print(f"IndexError: index {item} is out of range")
        except Exception as e:
            print(f"Error: {e}")

    return x

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
