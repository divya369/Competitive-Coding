def problem():
    number = int(input())
    print('W', end='')
    for i in range(number):
        print('o', end='')
    print('w')


def main():
    problem()


if __name__ == '__main__':
    main()