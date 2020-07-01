from pprint import pprint


def read_line_file(file, my_list):
    line = file.readline()
    while line:
        my_list.append(int(line))
        line = file.readline()
    pass


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


old_id = []
new_id = []
fucking_unsub = []

# засунуть открытие файла в функцию read_line_file
with open('old_followers_id.txt', 'r') as old_f:
    read_line_file(old_f, old_id)
    old_id.sort()

# засунуть открытие файла в функцию read_line_file
with open('new_followers_id.txt', 'r') as new_f:
    read_line_file(new_f, new_id)
    new_id.sort()

for item in old_id:
    if (bin_search(new_id, item)) == -1:
        print('FUCKING UNSUB:', item)

print('Дело сделано!')
