x = input().strip()

nos = [int(a) for a in x.split()]

start = nos[0]

if nos[0] < nos[2]:
	start = nos[2]

end = nos[1]

if nos[1] > nos[3]:
	end = nos[3]

time = 0

if end - start <= 0:
	time = 0
else:
	time = end - start

print(time)

