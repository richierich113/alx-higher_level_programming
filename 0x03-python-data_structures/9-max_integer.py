#!/usr/bin/python3

def max_integer(my_list=[]):
    new_list = []
    i = 0
    for num in my_list[i::1]:
        if i == 0:
            new_list.append(num)
        elif i == 1:
            if num > my_list[i - 1]:
                new_list.append(num)
            else:
                new_list.append(my_list[i - 1])
        elif i > 1 and i <= (len(my_list) - 1):
            if num > new_list[i - 1] and num > my_list[i - 1]:
                new_list.append(num)
            else:
                new_list.append(new_list[i - 1])

        i += 1

    if len(new_list) > 0:
        if len(new_list) == 1:
            return new_list[0]

        new1_list = []
        i = 0
        for num in new_list[i::1]:
            if i == 0:
                new1_list.append(num)
            elif i == 1:
                if num > new_list[i - 1]:
                    new1_list.append(num)
                else:
                    new1_list.append(new_list[i - 1])
            elif i > 1 and i <= (len(new_list) - 1):
                if num > new_list[i - 1] and num > new1_list[i - 1]:
                    new1_list.append(num)
                else:
                    new1_list.append(new_list[i - 1])

            i += 1

        return new1_list[-1]


# for testing function
if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
