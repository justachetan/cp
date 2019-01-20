inp = input().strip().split()

N = int(inp[0])
c = int(inp[1])

start = 1

poonji = 1000

vol = start + ((N - start)//2)

mode = "test"

while poonji > 0 and N - start > 1:

	if mode == "test":

		print("1 " + str(vol))

		res = int(input().strip())

		if res == 0:

			poonji-=1

			start = vol

			

		elif res == 1:

			mode = "fix"

	elif mode == "fix":

		poonji-=c

		N = vol

		mode = "test"

		print(2)


	vol = start + ((N - start)//2)

if N == start:

	print("1 " + str(N))

	res = int(input().strip())

	if res == 0:

		print()






print("3", vol + 1)




