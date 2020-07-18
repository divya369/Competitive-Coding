def print_symbol(flag):
    if flag == 0:
        print('*', end='')
    else:
        print('.', end='')


def print_pattern():
    cases = int(input())
    for i in range(cases):
        a, b = input().split()
        for j in range(int(a)):
            for k in range(int(b)):
                if (j+k) % 2 == 0:
                    print_symbol(0)
                else:
                    print_symbol(1)
            print('\n')
        print('\n')


def main():
    print_pattern()


if __name__ == '__main__':
    main()
