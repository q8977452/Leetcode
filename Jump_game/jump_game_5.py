'''
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

	i + x where: i + x < arr.length and 0 < x <= d.
	i - x where: i - x >= 0 and 0 < x <= d.

In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j 
(More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
'''
def maxJumps(self, arr: List[int], d: int) -> int:
	@lru_cache(None)
	def jump(index):
		left = max(0, index - d)
		right = min(len(arr) - 1, index + d)
		res = 0
		for i in range(index + 1, right + 1):
			if arr[i] < arr[index]:
				res = max(res, jump(i))
			else: break
		for i in range(index - 1, left - 1, -1):
			if arr[i] < arr[index]:
				res = max(res, jump(i))
			else: break
			return 1 + res
	res = 0
	for i in range(len(arr)):
		res = max(res, jump(i))
	return res