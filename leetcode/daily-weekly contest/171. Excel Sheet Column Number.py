# ------------------------------- Others solution - 1 -------------------------------


def titleToNumber(s: str) -> int:
    res = 0
    for i in s:
        res = res * 26 + ord(i) - ord('A') + 1
    return res


print(titleToNumber('BAC'))


# ------------------------------- Others solution - 1 -------------------------------

#
# from functools import reduce
#
#
# def titleToNumber(self, s: str) -> int:
#     return reduce(lambda x, y: 26 * x + ord(y) - 64, s, 0)
#
#




# ----------------------------- my solution -------------------------------

# from math import pow
#
#
# def titleToNumber(s: str) -> int:
#     alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
#                 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
#                 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
#     length = len(s)
#     answer = 0
#     for character in s:
#         if length == 1:
#             answer += alphabet[character]
#         else:
#             answer += int(pow(26, length-1)) * alphabet[character]
#             length -= 1
#     return int(answer)
#
#
# x = titleToNumber('AB')
# print(x)


# TO GENERATE DICTIONARY

# i = 1
# file = open('write.txt', 'w')
# while True:
#     alpha = input("Enter character : ")
#     if alpha == '1':
#         break
#     string = f"'{alpha}': {i}, "
#     file.write(string)
#     i += 1