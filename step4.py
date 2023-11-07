from collections import deque

n = int(input())
weight = deque()
for _ in range(n):
    query = input()
    q =  query.split()[0]
    if q == "ADD_RIGHT":
        weight.append(int(query.split()[1]))
    elif q == "ADD_LEFT":
        weight.appendleft( int(query.split()[1]))
    elif q == "REMOVE_RIGHT":
        weight.pop()
    elif q == "REMOVE_LEFT":
        weight.popleft()
print(sum(weight))