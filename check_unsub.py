def read_line_file(file, my_list):
    line = file.readline()
    while line:
        my_list.append(int(line))
        line = file.readline()
    pass


def read_my_file(name):
    temp = []
    with open(f'{name}_followers_id.txt', 'r') as f:
        read_line_file(f, temp)
        temp.sort()
    return temp


# binary search
def bin_search(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (high+low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1


fucking_unsub = []
old_id = read_my_file('old')
new_id = read_my_file('new')

for item in old_id:
    if (bin_search(new_id, item)) == -1:
        print('FUCKING UNSUB:', item)

print('Дело сделано!')
