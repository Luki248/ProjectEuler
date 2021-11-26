#!/usr/bin/env python3


# P002: Even Fibonacci numbers
def p002(m):
    sum = 0
    j = 0
    i = 1
    while i <= m:
        temp = i + j
        j = i
        i = temp
        if i % 2 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    ret = p002(4000000)
    print(ret)
