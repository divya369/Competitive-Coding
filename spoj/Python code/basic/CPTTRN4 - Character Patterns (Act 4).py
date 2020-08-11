"""
Using two characters: . (dot) and * (asterisk) print a grid-like pattern.

Input
You are given t - the number of test cases and for each of the test cases four positive integers: l - the number of lines, c - the number of columns in the grid; h and w - the high and the with of the single rectangle.

Output
For each of the test cases output the requested pattern (please have a look at the example). Use one line break in between successive patterns.

Example
Input:
3
3 1 2 1
4 4 1 2
2 5 2 2

Output:
***
*.*
*.*
***
*.*
*.*
***
*.*
*.*
***

*************
*..*..*..*..*
*************
*..*..*..*..*
*************
*..*..*..*..*
*************
*..*..*..*..*
*************

****************
*..*..*..*..*..*
*..*..*..*..*..*
****************
*..*..*..*..*..*
*..*..*..*..*..*
****************

"""


def print_symbol(flag):
    if int(flag) == 0:
        print('*', end='')
    elif int(flag) == 1:
        print('.', end='')


def print_pattern():
    cases = int(input())
    for case in range(cases):
        a, b, h, w = map(int, input().split())
        for i in range(a*h + a + 1):
            for j in range(b*w + b + 1):
                if (i % (h+1) != 0) and (j % (w+1) != 0):
                    print_symbol(1)
                else:
                    print_symbol(0)
            print('\n')
        print('\n')


def main():
    print_pattern()


if __name__ == '__main__':
    main()
