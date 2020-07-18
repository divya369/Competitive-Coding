from math import modf


def sum_2():
    cases = int(input())
    for _ in range(cases):
        a, b = input().split()
        sum = float(a)+float(b)
        if modf(sum) == (0.0, int(sum)):
            print(int(sum))
        else:
            print(sum)


def main():
    sum_2()


if __name__ == '__main__':
    main()