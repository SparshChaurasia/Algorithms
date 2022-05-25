def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        nums[i], nums[minpos] = nums[minpos], nums[i]


lst = [2, 5, 4, 3, 7, 8, 4, 1, 0, 9]
print(lst)

sort(lst)
print(lst)
 