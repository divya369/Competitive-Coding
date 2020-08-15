def hIndex(citations):
    if len(citations) == 0:
        return 0
    if len(citations) == 1:
        if citations[0] == 0:
            return 0
        else:
            return 1
    citations.sort(reverse=True)
    answer = 0
    for i, citation in enumerate(citations):
        if citation >= i+1:
            answer = i+1
        else:
            break
    return answer


print(hIndex([2, 2, 3]))