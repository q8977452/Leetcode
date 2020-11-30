'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''
def canJump(self, nums: List[int]) -> bool:
    step = nums[0]
    for i in range(1, len(nums)):
        if step > 0 :
            step -= 1
            step = max(step, nums[i])
        else:
            return False
    return True