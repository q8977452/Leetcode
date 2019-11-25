class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return binSearchRange(nums,target, 0, len(nums)-1)
    
def binSearchRange(nums, target, start, end):
    if start > end:
        return [-1, -1]
    m = int(start + (end - start)/2)
    if nums[m] == target:
        return [binLeftSearch(nums, target, start, m) , binRightSearch(nums, target, m, end)]
    elif nums[m] > target:
        return binSearchRange(nums, target, start, m-1)
    else:
        return binSearchRange(nums, target, m+1, end)
    
def binLeftSearch(nums, target, start, end):
    m = int(start + (end - start)/2)
    
    if nums[m] == target:
        if m == 0 or nums[m-1] != nums[m]:
            return m
        else: # nums[m-1] == nums[m]
            return binLeftSearch(nums, target, start, m-1)
    else: # nums[m] < target
        return binLeftSearch(nums, target, m+1, end)

def binRightSearch(nums, target, start, end):
    m = int(start + (end - start)/2)
    
    if nums[m] == target:
        if m == len(nums)-1 or nums[m+1] != nums[m]:
            return m
        else:
            return binRightSearch(nums, target, m+1, end)
    else:
        return binRightSearch(nums, target, start, m-1)    