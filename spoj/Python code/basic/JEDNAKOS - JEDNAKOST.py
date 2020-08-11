"""
While browsing a math book, Mirko found a strange equation of the form A=S.What makes the equation strange is that A and S are not the same,which makes the equation incorrect. Mirko realized that the left side of the equation should have addition operations between some pairs of digits in A. Write a program that inserts the smallest number of addition operations on the left side to make the equation correct. The numbers in the corrected equation may contain arbitrary amounts of eading zeros.

Input

The first line contains the equation in the form A=S.

A and S will both be positive integers without leading zeros. They will be different.

A will contain at most 1000 digit

S will be less than or equal to 5000

Note: The input data will guarantee that a solution, although not necessarily unique, will always exist.

Output

Output the number of addition operations needed

Example

Input:
143175=120

Output:
2
Input:
5025=30

Output:
1
Input:
999899=125

Output:
4
"""


def find_addition():
    a, s = input().split('=')
    a = a + '.*'                # dummy string attached to check end of string object (a)
    s = int(s)
    num_list = []
    count_plus = 0
    start = 0
    end = 1
    while a[end] != '*':
        temp = int(a[start:end])
        if temp + sum(num_list) > s:
            count_plus += 1
            num_list.append(int(a[start:end-1]))
            start = end - 1
        else:
            end += 1
    return count_plus


def main():
    count = find_addition()
    print(count)


if __name__ == '__main__':
    main()
