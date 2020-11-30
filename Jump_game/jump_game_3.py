'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''
def canReach(self, arr: List[int], start: int) -> bool:
    seen_set = set([start])# 集合存儲訪問過的下標
    q = [start]
    while q:
        p = q.pop(0)
        if arr[p] == 0:
            return True

        for k in [p-arr[p], p+arr[p]]:
            if k in seen_set: continue            
            if 0 <= k <= len(arr)-1:
                q.append(k)
                seen_set.add(k)    
    return False