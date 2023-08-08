#!/usr/bin/python3
for m in range(0, 8):
    for n in range(m + 1, 10):
        print("{:d}{:d}".format(m, n), end=", ")
print("{:d}{:d}".format(m + 1, n))
