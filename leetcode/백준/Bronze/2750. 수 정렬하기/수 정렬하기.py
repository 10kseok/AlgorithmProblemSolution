# bubble sort
from typing import MutableSequence

def bubble_sort(nums: MutableSequence):
    n = len(nums)
    k = 0

    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, -1):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                last = j
        k = last

def cocktail_sort(nums: MutableSequence):
    left = 0
    right = len(nums) - 1
    last = right
    
    while left < right:
        for j in range(right, left, -1):
            if nums[j - 1] > nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                last = j
        left = last

        for j in range(left, right):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                last = j
        right = last

n = int(input())
buffer = [int(input()) for _ in range(n)]
cocktail_sort(buffer)
print(*buffer, sep="\n")