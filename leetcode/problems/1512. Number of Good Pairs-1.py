def good_pair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    print(count)


if __name__ == '__main__':
    good_pair([1, 2, 3, 1, 1, 3])
