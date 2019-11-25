# 善用 profiler
## 不使用 IPython 的函式進行 profiling
import cProfile
import numpy as np
import pstats

def is_prime(a):
	'''費馬小定理'''
	a = abs(a)
	if a == 2:
		return True
	if a < 2 or a & 1 == 0:
		return False
	return pow(2, a-1, a) == 1

def mysum(N):
	return np.arange(1, N+1).sum()
	
def task1(N):
	# 從1~N的整數尋找質數
	out = []
	append = out.append
	for k in range(1,N+1):
		if is_prime(k):
			append(k)
	# 計算從1~N的整數和
	a = mysum(N)
	return [out,a]

def task2(N):
	return np.sqrt(np.arange(1,N+1))
	
def main():
	task1(10000)
	task2(10000)
if __name__ == '__main__':
	cProfile.run('main()',filename='main.prof')
	sts = pstats.Stats('main.prof')
	sts.strip_dirs().sort_stats('cumulative').print_stats()