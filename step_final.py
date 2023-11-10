n = int(input())
idx = 0
keys = ["*"]
queries = input().split()

#print(idx)
#print("--------")

for query in queries:
    #print(idx)
    #print(query)
    if query == 'Left':
        if idx == 0:
            pass
        else:
            idx -= 1
    elif query == 'Right':
        if idx == len(keys)-1:
            pass
        else:
            idx += 1
    elif query == "Delete":
        if idx == 0:
            pass
        else:
            idx -= 1
            keys.pop(idx)
    else:
        keys.insert(idx, query)
        idx += 1
    #print(keys)
    #print(idx)
    #print("------")

keys.pop()
print(*keys)