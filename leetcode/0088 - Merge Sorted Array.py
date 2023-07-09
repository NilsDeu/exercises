""" leetcode: 88. Merge Sorted Array"""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    one = two = 0
    if n > 0:
        for _ in range(n):
            nums1[m+one] = nums2[two]
            one += 1
            two += 1
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)
