'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
'''
def jump(self, nums: List[int]) -> int:
    reach = 0
    cur = 0
    N = len(nums)
    count = 0
    pos = 0
    while cur < N - 1:
        count += 1
        pre = cur
        while pos <= pre:
            cur = max(cur, pos + nums[pos])
            pos += 1
    return count