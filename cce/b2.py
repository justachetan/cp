def sum2(s, k):
	poss = [i for i in range(k+1)]

	start = 0
	end = k

	count=0

	while start != end:
		if poss[start] + poss[end] > s:
			end-=1
		elif poss[start] + poss[end] < s:
			start+=1
		elif poss[start] + poss[end] == s:
			count+=1
			end-=1
	count = count * 2
	if poss[start] + poss[end] == s:
		count+=1
	return count

nos = input().strip().split()

k = int(nos[0])

s = int(nos[1])
tot=0


for i in range(k + 1):

	tot+=sum2(s - i, k)

print(tot)

