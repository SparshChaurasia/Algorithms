def search(lst, n):
    for i in lst:
        if i == n:
            return lst.index(n)
    else:
        return None


lst = [1, 5, 6, 3, 4, 8, 9, 0, 1, 3, 5]
target = 9

print(search(lst, target))
