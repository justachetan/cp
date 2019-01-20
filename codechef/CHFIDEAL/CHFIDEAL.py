import random

s = [1, 2, 3]

me = random.choice(s)

print(me)

s.pop(s.index(me))

grader = int(input().strip())


s.pop(s.index(grader))

print(s[0])