class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp=[]
        rtype=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j==i:
                    break
                for k in range(i+2,len(nums)):
                    if k==j:
                        break
                    if nums[i]+nums[j]+nums[k]==0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        rtype.append(temp)
                    if rtype.count(temp)>1:
                        rtype.remove(temp)
        return(rtype)