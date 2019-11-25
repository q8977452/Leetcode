class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numlen,res,temp=len(nums),set(),{}
        nums.sort()
        if numlen<4 :
            return []
        nums.sort
        for p in range(numlen):
            for q in range(p+1,numlen):
                if nums[p]+nums[q] not in temp:
                    temp[nums[p]+nums[q]] = [(p,q)]
                else:
                    temp[nums[p]+nums[q]].append((p,q))
        for i in range(numlen):
            for j in range(i+1, numlen-2):
                T = target-nums[i]-nums[j]
                if T in temp:
                    for k in temp[T]:
                        if k[0] > j: res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]