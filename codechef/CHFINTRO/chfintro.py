inp = input()

t = int(inp.strip().split()[0])
rat = int(inp.strip().split()[1])

for i in range(t):
	s = input()
	k = int(s.strip())
	if k < rat:
		print("Bad boi")
	else:
		print("Good boi")