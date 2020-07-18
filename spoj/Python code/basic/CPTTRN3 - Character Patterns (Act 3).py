def print_symbol(flag):
    if int(flag) == 0:
        print('*', end='')
    elif int(flag) == 1:
        print('..', end='')
    elif int(flag) == 2:
        print('**', end='')


def print_pattern():
    cases = int(input())
    for case in range(cases):
        a, b = input().split()
        for i in range(3 * int(a) + 1):
            for j in range(2 * int(b) + 1):
                if j % 2 == 0:
                    print_symbol(0)
                elif (i % 3 == 0) and (j % 2 == 1):
                    print_symbol(2)
                elif j % 2 == 1:
                    print_symbol(1)
            print('\n')
        print('\n')


def main():
    print_pattern()


if __name__ == '__main__':
    main()
