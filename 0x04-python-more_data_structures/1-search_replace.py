#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if len(my_list) > 0:
        modified_list = []
        for i in range(len(my_list)):
            num = my_list[i]
            if num == search:
                modified_list.append(replace)
            else:
                modified_list.append(num)
        return modified_list

    return None


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
