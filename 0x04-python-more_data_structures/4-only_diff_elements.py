#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    only_set_1 = set_1.difference(set_2)
    only_set_2 = set_2.difference(set_1)
    new_set = only_set_1.union(only_set_2)
    return new_set



if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
