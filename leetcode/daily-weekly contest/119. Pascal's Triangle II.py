# ---------------------------- MY SOLUTION ---------------------------

# Python3 program for Pascal's Triangle
# A O(n^2) time and O(1) extra
# space method for Pascal's Triangle

# Pascal function


def printPascal(n):
    answer = []
    for line in range(1, n+2):
        C = 1
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            if line-1 == n:
                answer.append(C)
            C = int(C * (line - i) / i)
    return answer


n = 5
print(printPascal(4))