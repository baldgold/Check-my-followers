import glob
import json
from pprint import pprint


def make_file_with_followers(name):
    with open(f"{name}_followers_id.txt", "w") as f:
        followers_id.sort()
        for item in followers_id:
            f.write(str(item) + '\n')


while True:
    answer = (input("""Выберите режим работы:\n\t1) Создание файла, из которого мы будем брать фолловеров и искать подписаны ли они сейчас. (OLD)
\t2) Создание файла, с которым мы будем сравнивать фолловеров, которые были подписаны раньше. (NEW)\n\t>>>"""))
    if answer == '1' or answer == '2':
        answer = int(answer)
        break
    else:
        print('\nОШИБКА! Введите 1 или 2...\n')
        continue

files = glob.glob('json/*.json')
followers = {}
followers_id = []

fuck = {}

for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        for user in data['data']['user']['edge_followed_by']['edges']:
            user_info = user['node']
            followers[user_info['username']] = {
                'id': user_info['id'],
                'username': user_info['username'],
                'full_name': user_info['full_name']
            }
            followers_id.append(int(user_info['id']))
            fuck[user_info['id']] = user_info['username']

# all information about followers
with open('followers.json', 'w') as f:
    json.dump(list(followers.values()), f)

# special file with followers id
if answer == 1:
    make_file_with_followers('old')
else:
    make_file_with_followers('new')

print('Дело сделано: parse_followers')

pprint(fuck)
