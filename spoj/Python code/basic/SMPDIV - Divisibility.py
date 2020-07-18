def problem():
    cases = int(input())
    for case in range(cases):
        n, x, y = input().split()
        n = int(n)
        x = int(x)
        y = int(y)
        for i in range(n):
            if (i % x == 0) and (i % y != 0):
                print(f'{i} ', end='')
        print('\n')


def main():
    problem()


if __name__ == '__main__':
    main()