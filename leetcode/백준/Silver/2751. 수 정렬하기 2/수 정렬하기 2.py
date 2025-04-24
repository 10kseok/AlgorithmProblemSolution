# bubble sort
from typing import MutableSequence
import sys

def quick_sort(nums: MutableSequence, left, right):
    left_pointer = left
    right_pointer = right
    pivot = nums[(left + right) // 2]

    while left_pointer <= right_pointer:
        while nums[left_pointer] < pivot: left_pointer += 1
        while nums[right_pointer] > pivot: right_pointer -= 1

        if left_pointer <= right_pointer:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    if left < right_pointer: quick_sort(nums, left=left, right=right_pointer)
    if left_pointer < right: quick_sort(nums, left=left_pointer, right=right)

def merge_sort(nums: MutableSequence):
    def _merge_sort(nums: MutableSequence, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(nums, left, center)
            _merge_sort(nums, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buffer[p] = nums[i]
                p += 1
                i += 1
            
            while i <= right and j < p:
                if buffer[j] <= nums[i]:
                    nums[k] = buffer[j]
                    j += 1
                else:
                    nums[k] = nums[i]
                    i += 1
                k += 1

            while j < p:
                nums[k] = buffer[j]
                k += 1
                j += 1

    n = len(nums)
    buffer = [None] * n
    _merge_sort(nums, 0, n - 1)

n = int(input())
sys.setrecursionlimit(10 ** 6)
input_buffer = [int(sys.stdin.readline()) for _ in range(n)]
# quick_sort(buffer, 0, len(buffer) - 1)
merge_sort(input_buffer)
sys.stdout.write('\n'.join(map(str, input_buffer)))
# print(*input_buffer, sep="\n")