# my code


def lengthOfLongestSubstring(s) -> int:
    lst = list(s)
    count = 0
    final = 0
    length = len(s)
    set1 = set()
    i = 0
    set_index = 0
    while True:
        if i == length:
            if final < count:
                final = count
            break
        if lst[i] not in set1:
            count += 1
            set1.add(lst[i])
            i += 1
        else:
            if final <= count:
                final = count
            count = 0
            set1.clear()
            set_index += 1
            i = set_index
    return final


x = lengthOfLongestSubstring("abb")
print(x)
