#!/usr/bin/env python3


# P001: Multiples of 3 or 5
def p001(m):
    sum = 0
    for i in range(2, m):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    ret = p001(1000)
    print(ret)
