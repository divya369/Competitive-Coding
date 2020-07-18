def print_symbol(flag):
    if int(flag) == 0:
        print('*', end='')
    else:
        print('.', end='')


def print_pattern():
    cases = int(input())
    for case in range(cases):
        a, b = input().split()
        for i in range(int(a)):
            for j in range(int(b)):
                if (i == 0) or (j == 0) or (j == int(b)-1) or (i == int(a)-1):
                    print_symbol(0)
                else:
                    print_symbol(1)
            print('\n')
        print('\n')


def main():
    print_pattern()


if __name__ == '__main__':
    main()
