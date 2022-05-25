def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        if lst[mid] == target:
            return mid
        else:
            if target < lst[mid]:
                right = mid-1
            else:
                left = mid+1
    return False


lst = [2, 4, 5, 7, 12, 23, 45, 54, 56]
target = 45

print(search(lst, target))
