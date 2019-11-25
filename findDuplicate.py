def findDuplicate(self, nums):
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            fast=nums[nums[fast]]
            slow=nums[slow]
        fast=0
        while slow!=fast:
            fast=nums[fast]
            slow=nums[slow]
        return fast
		#https://blog.csdn.net/fuxuemingzhu/article/details/79530847