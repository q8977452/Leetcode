def batchnorm_forward(x, gamma, beta, eps):
	N, D = x.shape
	
	#step1: calculate mean
	mu = 1./N * np.sum(x ,axis = 0)
	
	#step2: substract mean vector of every trainings example
	xmu = x - mu
	
	#step3: following the Lower branch - calculation denominator
	sq = xmu ** 2
	
	#step4: calculate variance
	var = 1./N * np,sum(sq, axis = 0)
	
	#step5: add eps for numerical stability, then sqrt
	sqrtvar = np.(var + eps)
	
	#step6: invert sqrtvar
	ivar = 1./sqrtvar
	
	#step7: execute normalization
	xhat = xmu * ivar
	
	#step8: Nor the two transformation steps
	gammax = gamma * xhat
	
	#step9
	out = gammax + beta
	
	#store intermediate
	cache = (xhat,gamma,xmu,ivar,sqrtvar,var,eps)
	
	return out, cache