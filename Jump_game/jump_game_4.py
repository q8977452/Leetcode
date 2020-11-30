'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

	i + 1 where: i + 1 < arr.length.
	i - 1 where: i - 1 >= 0.
	j where: arr[i] == arr[j] and i != j.
	
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
'''
def minJumps(self, arr: List[int]) -> int:
	g = defaultdict(list)
	for i,a in enumerate(arr):
		if (i > 0) and (i < len(arr) - 1) and (a == arr[i-1] == arr[i+1]):
			continue
                
		g[a].append(i)
                
	seen_set = set([0])
	q = [(0, 0)]
	step = 0
	## BFS
	while q:
		p, step = q.pop(0)
		
		if p == len(arr) - 1:
			return step

		for k in [p-1, p+1] + g[arr[p]]:
			if k in seen_set: continue
                
			if 0 <= k <= len(arr)-1:
				q.append((k, step+1))
				seen_set.add(k)
        return 0