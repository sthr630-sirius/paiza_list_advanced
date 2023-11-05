'---------------------------------------'
'                definition                  '
n, q = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
cups = [None]*size_array
next_ptr = [None]*size_array
prev_ptr = [None]*size_array
cups[start_idx] = -1
cups[end_idx] = -1
next_ptr[start_idx] = 1023
next_ptr[end_idx] = -1
prev_ptr[start_idx] = -1
prev_ptr[end_idx] = 0
empty_min_idx = 1
print(cups)
print(next_ptr)
print(prev_ptr)

'---------------------------------------'
'               initialization               '
for i in range(n):
    cups[empty_min_idx] = i+1
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx
    empty_min_idx += 1
print(cups)

'---------------------------------------'
'                     main                    '
for _ in range(q):
    query = input()
    order = int(query.split()[0])
    x = int(query.split()[1])
    y = int(query.split()[2])

    if order == 1:
        print("insert")
        print(x, y)
    elif order == 2:
        print("swap")
        print(x, y)

'---------------------------------------'
'       function search_idx          '
'---------------------------------------'
'       function insert_cup          '
'---------------------------------------'
'       function swap_cup           '
'---------------------------------------'
'       function search_ball          '


