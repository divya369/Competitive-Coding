from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def prime_generator():
    cases = int(input())
    for _ in range(cases):
        start, end = input().split()
        for x in range(int(start), int(end)+1):
            flag = is_prime(x)
            if flag:
                print(x)
        print('\n')


def main():
    prime_generator()


if __name__ == '__main__':
    main()