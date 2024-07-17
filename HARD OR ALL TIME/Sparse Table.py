import math #It is for log purpose
def Sparse(arr, n):
	"""This function fill the 2D matrix of lookup /
	   because of based on range start at 2 to n-1 distance"""
	for i in range(0, n): 
		lookup[i][0] = arr[i] #starting 1 range fillup
	j = 1
	while (1 << j) <= n: 
		i = 0
		while (i + (1 << j) - 1) < n: 
			if (lookup[i][j - 1] < 
				lookup[i + (1 << (j - 1))][j - 1]): 
				lookup[i][j] = lookup[i][j - 1] 
			else: 
				lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1] 
			i += 1
		j += 1
def query(L, R):#performing the perticular task
	j = int(math.log2(R - L + 1)) #(R-L+1) This is the formula to find the length of the subarray length
	if lookup[L][j] <= lookup[R - (1 << j) + 1][j]: 
		print(R - (1 << j) + 1)
		return lookup[L][j] 
	else: 
		return lookup[R - (1 << j) + 1][j] 
if __name__ == "__main__": 
	a = [1, 2, 3, 10, 5, 10, 11, 12, 18] 
	n = len(a) 
	lookup = [[0 for i in range(n)] for j in range(n)] 
	Sparse(a, n)
	for i in lookup:
		print(i)
	print(query(0, 4))
	print(query(4, 7) )
	print(query(7, 8))