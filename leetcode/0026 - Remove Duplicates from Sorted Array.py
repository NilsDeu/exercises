""" leetcode: 26. Remove Duplicates from Sorted Array """

def removeDuplicates(nums: list[int]) -> int:
    """ remove the duplicates in-place of nums in place.
    The relative order stays the sam.
    Returns the number of uniques."""
    nums[:] = list(set(nums))
    #nums[:] = sorted(list(set(nums)))
    return (len(nums))

#Example 1:
nums = [1,1,2]
print(f"Uniques: {removeDuplicates(nums)}; {nums=}")

#Example 2:
nums = [0,0,1,1,1,2,2,3,3,4]
print(f"Uniques: {removeDuplicates(nums)}; {nums=}")

# negative
nums = [-1,1,1,2]
print(f"Uniques: {removeDuplicates(nums)}; {nums=}")
