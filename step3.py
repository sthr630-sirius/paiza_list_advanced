n, q = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

is_ok = [1] * n

for i in range(n):
    for j in range(q):
        if a[i] % b[j] == 0:
            is_ok[i] = 0

ans =[]

if sum(is_ok) == 0:
    print("You")
else:
    print("Kyoko")
    for i, flag in enumerate(is_ok):
        if flag == 1:
           ans.append(a[i])
    print(*ans)