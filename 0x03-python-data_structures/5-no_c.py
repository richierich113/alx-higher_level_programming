#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for charac in my_string:
        if charac == "c" or charac == "C":
            continue

        new_string += charac

    return new_string


# for testing purposes of function
if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
