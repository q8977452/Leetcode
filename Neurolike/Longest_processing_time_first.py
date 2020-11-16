# read and prepare n, m, and p
n = int(input('Number of jobs: '))
m = int(input('Number of machines: '))
pStr = input('Processing times: ')

p = pStr.split(' ')
for i in range(n):
	p[i] = int(p[i])
	
# machine completion times
loads = [0] * m
assignment = [0] * n

# in iteration j, assign job j to the least loaded machines
for j in range(n):

	#find the least loaded machine
	leastLoadedMachine = 0
	leastLoad = loads[0]
	for i in range(1,m):
		if loads[i] < leastLoad:
			leastLoadedMachine = i
			leastLoad = loads[i]
			
	# schedule a job
	loads[leastLoadedMachine] += p[j]
	assignment[j] = leastLoadedMachine + 1
	# check the process
    print(str(p[j]) + ': ' + str(loads))

# the result
print('Job assignment: ' + str(assignment))
print('Machine loads: ' + str(loads))