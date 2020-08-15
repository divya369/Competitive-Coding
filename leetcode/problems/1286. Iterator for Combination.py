# --------------- OTHERS SOLUTION --------------------

# The hints clearly says to use bitmasking. From problem statement we observe that maximum length of string would be 15, which is nothing but "111111111111111" in binary, whose decimal would be 32767.
#
# GENERATION OF COMBINATIONS:
# The idea here is to run a loop from 0 to a decimal number which has len(characters) of binary digits and all bits are set. Check number of set bits in each number in its binary form. Keep those numbers in an array.
#
# The problem statement asks us to print the combinations in lexicographical order. Don't give a sweat, as the power of binary comes to rescue. The generated combination will already be in reverse order.
#
# Eg: "abc", 2
#
# We start with "111" which is 7. Run a loop over 0 to 7 both inclusive. The possible values with 2 set bits are ["011", "101", "110"]
# PRINTING next:
# Just take the appropriate combination. Run a loop. If the bit is set, include the char in the given position in the initial character.


# class CombinationIterator:
#
#     def __init__(self, characters: str, combinationLength: int):
#         self.characters = characters
#         self.n = len(characters)
#         self.combinations = gen_combinations(self.n, combinationLength)
#         self.ind = len(self.combinations) - 1
#
#     def next(self) -> str:
#         s = ""
#         for i in range(self.n):
#             if self.combinations[self.ind][i] != "0":
#                 s += self.characters[i]
#         self.ind -= 1
#         return s
#
#     def hasNext(self) -> bool:
#         return self.ind > -1
#
#
# def gen_combinations(l, n):
#     end = int("1" * l, 2)
#     ans = []
#     for i in range(end + 1):
#         b = bin(i)[2:]
#         if b.count('1') == n:
#             ans.append(b.zfill(l))
#     return ans


# -------------------------------------- OTHERS SOLUTION -------------------------------------


# class CombinationIterator(object):
#
#     def __init__(self, characters, combinationLength):
#         self.characters = characters
#         self.combination_length = combinationLength
#         self.count = 0
#
#         self.combination_list = []  # ['ab','ac','bc'] # populate the list with combinationLength
#         self.helper('', 0, self.combination_length, self.combination_list, 0)
#
#     def helper(self, string, index, combination_length, combination_list, compare):
#         if compare == combination_length:
#             combination_list.append(string)
#             return
#         for i in range(index, len(self.characters)):
#             self.helper(string + self.characters[i], i + 1, combination_length, combination_list, compare + 1)
#
#     def next(self):
#         self.count += 1
#         return self.combination_list[self.count - 1]
#
#     def hasNext(self):
#         return self.count < len(self.combination_list)




# -------------------------------------- OTHERS SOLUTION -------------------------------------

# from itertools import combinations
#
#
# class CombinationIterator(object):
#
#     def __init__(self, characters, combinationLength):
#         self.iterable = combinations(characters, combinationLength)
#         self.buffer = "".join(next(self.iterable)) if characters else None
#
#     def next(self):
#         result = self.buffer
#         try:
#             self.buffer = "".join(next(self.iterable))
#         except:
#             self.buffer = None
#         return result
#
#     def hasNext(self):
#         return self.buffer is not None




# -------------------------------------- OTHERS SOLUTION -------------------------------------
# import itertools
#
# class CombinationIterator(object):
#
#     def __init__(self, characters, combinationLength):
#         self.it = itertools.combinations(characters, combinationLength)
#
#     def next(self):
#         try:
#             self.buffer = next(self.it, None)
#             res = ''.join(self.buffer)
#         except:
#             res = None
#         return res
#
#     def hasNext(self):
#         return self.buffer is not None





# -------------------------------------- OTHERS SOLUTION : using generator -------------------------------------


# class CombinationIterator(object):
#
#     def __init__(self, characters, combinationLength):
#         self.generator = self.gen(characters, combinationLength)
#         self.buffer = next(self.generator)
#
#     def gen(self, characters, length):
#         if length == 0:
#             yield ""
#         elif len(characters) == length:
#             yield characters
#         elif len(characters) > length:
#             for tail in self.gen(characters[1:], length - 1):
#                 yield characters[0] + tail
#             for tail in self.gen(characters[1:], length):
#                 yield tail
#
#     def next(self):
#         res = self.buffer
#         try:
#             self.buffer = next(self.generator)
#         except StopIteration:
#             self.buffer = None
#         return res
#
#     def hasNext(self):
#         return self.buffer is not None




# BEST ------------------------------------- OTHERS SOLUTION : using generator -------------------------------------

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def combinations(cur, idx):
            if len(cur) == combinationLength:
                yield ''.join(cur)
                return
            for i in range(idx, len(characters)):
                cur.append(characters[i])
                yield from combinations(cur, i + 1)
                cur.pop()

        self.combos = combinations([], 0)
        self.current = True
        self.hasNextCalled = False

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)


obj = CombinationIterator('abc', 2)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
