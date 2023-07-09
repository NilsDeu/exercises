""" leetcode: 27. Remove Element"""

def removeElements(nums: list[int], val: int) -> int:
    """ Removes all occurences of val from nums.
    Returns the number of remaining entries."""
    nums[:]= sorted(i for i in nums if i !=val)
    return(len(nums))

#Example 1:
nums = [3,2,2,3]; val = 3
k = removeElements(nums, val)
print(f"{k=} {nums=}")

#Example 2:
nums = [0,1,2,2,3,0,4,2]; val = 2
k = removeElements(nums, val)
print(f"{k=} {nums=}")
