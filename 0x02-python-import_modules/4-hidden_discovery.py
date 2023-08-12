#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":

    module_names = dir(hidden_4)
    for name in module_names:
        if name[:2] == "__":
            continue
        print(f"{name}")
