n = float(input().strip())

total = (n * (n + 1)) / 2

for i in range(1, int(n + 1)):

	total += (i * (n - i + 1)) + ((n * (n+1)) / 2) - (((i - 1) * (i)) / 2)

print(int(total))