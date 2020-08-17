import collections

# -------------------------------------- MY SOLUTION ----------------------------------------

# def longestPalindrome(s):
#     answer = 0
#     flag = 0
#     dictionary = collections.Counter(s)
#     if s == "":
#         return 0
#     if len(dictionary) == 1:
#         return len(s)
#     for value in dictionary.values():
#         if value % 2 == 0:
#             answer += value
#         else:
#             if flag == 0:
#                 answer += value
#                 flag = 1
#             else:
#                 answer += value - 1
#     return answer



# ---------------------------------------- OTHERS SOLUTION ----------------------------------------


# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     hash = set()
#     for c in s:
#         if c not in hash:
#             hash.add(c)
#         else:
#             hash.remove(c)
#     # len(hash) is the number of the odd letters
#     return (len(s) - len(hash) + 1) if len(hash) > 0 else len(s)





# ---------------------------------------- OTHERS SOLUTION ----------------------------------------


def longestPalindrome(s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)


print(longestPalindrome("abababa"))