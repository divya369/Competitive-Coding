def problem():
    a, b = input().split()
    temp = int(a)
    b = int(b)
    sum = 0
    while b >= temp:
        sum += temp ** 2
        temp += 1
    print(sum)


def main():
    problem()


if __name__ == '__main__':
    main()
