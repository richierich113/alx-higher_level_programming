#!/usr/bin/python3
def magic_calculation(a, b):
    results = 0
    for indx in range(1, 3):
        try:
            if indx > a:
                raise Exception('Too far')
            else:
                results += (a ** b) / indx
        except Exception:
            results = b + a
            break
    return (results)
