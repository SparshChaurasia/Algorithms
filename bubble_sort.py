def sort(nums):
    for i in reversed(range(0, len(nums))):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


lst = [2, 5, 4, 3, 7, 8, 4, 1, 0, 9]
print(lst)

sort(lst)
print(lst)
