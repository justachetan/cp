nos = input().strip().split()

k = int(nos[0])

s = int(nos[1])
count = 0
for x in range(k+1):
	for y in range(min(k+1, s - x + 1)):
		for z in range(min(k+1, s - x - y + 1)):
			if x + y + z == s:
				count+=1

print(count)
