def search_idx(p, start_idx, end_idx):
    idx = next_ptr[start_idx]
    target_idx = 0
    counter = 1
    while counter <= p:
        if counter == p:
            target_idx = idx
        idx = next_ptr[idx]
        counter += 1
    return target_idx

n, m = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
person_list = [None]*size_array
next_ptr = [None]*size_array
prev_ptr = [None]*size_array
person_list[0] = -1
person_list[end_idx] = -1
next_ptr[start_idx] = 1
next_ptr[end_idx] = -1
prev_ptr[start_idx] = -1
prev_ptr[end_idx] = 0
insert_person = []
ptr = []
empty_min_idx = 1

for person in input().split():
    person_list[empty_min_idx] = person
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx
    empty_min_idx += 1

for person in input().split():
    insert_person.append(person)

for p in input().split():
    ptr.append(int(p))

for person, p in zip(insert_person, ptr):
    target_idx = search_idx(p, start_idx, end_idx)
    person_list[empty_min_idx] = person
    next_ptr[empty_min_idx] = next_ptr[prev_ptr[target_idx]]
    next_ptr[prev_ptr[target_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[target_idx]
    prev_ptr[target_idx] = empty_min_idx
    empty_min_idx += 1

print_idx = next_ptr[start_idx]
while print_idx != end_idx:
    print(person_list[print_idx])
    print_idx = next_ptr[print_idx]
