def eraseOverlapIntervals(intervals):
    collection = set()
    answer = 0
    for sub in intervals:
        if (sub[0] in collection) and (sub[1] in collection):
            answer += 1
        else:
            for i in range(sub[0], sub[1] + 1):
                collection.add(i)
    # print(collection)
    return answer


print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))    # wrong answer
print(eraseOverlapIntervals([[1,2],[1,3],[2,3],[3,4]]))         # right answer
