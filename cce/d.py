def check_valid(x, y, r, c):
	if x < 0 or x >= r or y < 0 or y >= c:
		return False
	else:
		if graph[x][y] == "X":
			return False
		else:
			return True

def do_bfs_step(x, y, q, v, r, c):

	if check_valid(x-1, y, r, c) and (x-1, y) not in v:
		q.append((x-1, y))
		v.append((x-1, y))
	if check_valid(x+1, y, r, c) and (x+1, y) not in v:
		q.append((x+1, y))
		v.append((x+1, y))
	if check_valid(x, y-1, r, c) and (x, y-1) not in v:
		q.append((x, y-1))
		v.append((x, y-1))
	if check_valid(x, y+1, r, c) and (x, y+1) not in v:
		q.append((x, y+1))
		v.append((x, y+1))

	return q, v



xy = input().strip().split()

dims = [int(i) for i in xy]

graph = []

for r in range(dims[0]):
	row = input().strip()
	graph.append(row)

tests = input().strip()
tests = int(tests)


for i in range(tests):

	coords = input().strip().split()
	coords = [int(j) - 1 for j in coords]
	v = list()
	q = [(coords[0], coords[1])]
	flag = False
	while len(q) != 0:
		q, v = do_bfs_step(q[0][0], q[0][1], q, v, dims[0], dims[1])
		a = q.pop(0)
		if (coords[2], coords[3]) in q:
			print('YES')
			flag = True
			break
	if flag == False:
		print('NO')









