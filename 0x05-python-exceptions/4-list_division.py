#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = list()

    for indx_1 in range(0, list_length):
        try:
            element_1 = my_list_1[indx]
            element_2 = my_list_2[indx]

            '''req_element_1 = isinstance(element_1(int, float))
            req_element_2 = isinstance(element_2(int, float))
            '''

            if not isinstance(element_1, (int, float)) or
            not isinstance(element_2, (int, float)):
                raise TypeError("wrong type")
            results = element_1 / element_2
        except IndexError:
            print("out of range")
            results = 0
        except ZeroDivisionError:
            print("division by 0")
            results = 0
        except TypeError:
            print("wrong type")
            results = 0
        finally:
            new_list.append(results)
        i += 1
    return new_list


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
