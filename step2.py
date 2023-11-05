'---------------------------------------'
'       function search_idx          '
def search_idx(start_idx, end_idx, p):
    idx = next_ptr[start_idx]
    target_idx = 0
    counter = 1
    while counter <= p:
        if counter == p:
            target_idx = idx
        idx = next_ptr[idx]
        counter += 1
    return target_idx

'---------------------------------------'
'       function insert_cup          '
def insert_cup(empty_min_idx, target_idx):
    cups[empty_min_idx] = empty_min_idx
    next_ptr[empty_min_idx] = next_ptr[prev_ptr[target_idx]]
    next_ptr[prev_ptr[target_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[target_idx]
    prev_ptr[target_idx] = empty_min_idx

'---------------------------------------'
'       function swap_cup           '
def swap_cup(target_idx_x, target_idx_y):
    temp_cup = cups[target_idx_x]
    cups[target_idx_x] = cups[target_idx_y]
    cups[target_idx_y] = temp_cup

'---------------------------------------'
'       function search_ball          '
def search_ball(start_idx, end_idx):
    ball_idx = next_ptr[start_idx]
    ans = 1
    while ball_idx <= end_idx:
        if cups[ball_idx] == 1:
            print(ans)
            break
        ball_idx = next_ptr[ball_idx]
        ans += 1

'---------------------------------------'
'                definition                  '
n, q = map(int, input().split())
size_array = 3000
start_idx = 0
end_idx = size_array-1
cups = [None]*size_array
next_ptr = [None]*size_array
prev_ptr = [None]*size_array
cups[start_idx] = -1
cups[end_idx] = -1
next_ptr[start_idx] = end_idx
next_ptr[end_idx] = -1
prev_ptr[start_idx] = -1
prev_ptr[end_idx] = start_idx
empty_min_idx = 1

'---------------------------------------'
'               initialization               '
for i in range(n):
    cups[empty_min_idx] = i+1
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx
    empty_min_idx += 1

'---------------------------------------'
'                     main                    '
for _ in range(q):
    query = input()
    order = int(query.split()[0])
    x = int(query.split()[1])
    y = int(query.split()[2])

    if order == 2:
        #print("insert")
        #print(x, y)
        target_idx = search_idx(start_idx, end_idx, y)
        insert_cup(empty_min_idx, target_idx)
        empty_min_idx += 1
    elif order == 1:
        #print("swap")
        #print(x, y)
        target_idx_x = search_idx(start_idx, end_idx, x)
        target_idx_y = search_idx(start_idx, end_idx, y)
        swap_cup(target_idx_x, target_idx_y)
    ' test code '
    #test_idx = next_ptr[start_idx]
    #while test_idx != end_idx:
    #    print(cups[test_idx], end="")
    #    test_idx = next_ptr[test_idx]
    #print(" ")
    ' test code '

search_ball(start_idx, end_idx)


