import random 
import sys

sys.setrecursionlimit(1000000)

lst = [2, 4, 1, 6, 9, 3,]
ITERATION = 0

def sort(sequence):
    if sequence == sorted(sequence):
        return sequence

    globals()["ITERATION"] += 1
    print(f"Iteration {globals()['ITERATION']}: {sequence}")

    random.shuffle(sequence)
    sort(sequence)


print("original list is", lst)
sort(lst)
print("sorted list is", lst)
