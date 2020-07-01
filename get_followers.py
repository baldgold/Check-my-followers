import json
from pprint import pprint
import subprocess
import time
import urllib.parse


url_base = 'https://www.instagram.com/graphql/query/?'

command_template = """curl '{url}' \
  -H 'authority: www.instagram.com' \
  -H 'accept: */*' \
  -H 'x-ig-www-claim: hmac.AR1lLOvPqSCnW8LHqmoIz8t4kt1kr4YcslBCuPHfe8qt4JAX' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36' \
  -H 'x-csrftoken: ezsRIKt6wI61vvcDziGGrE3dp4Rm08Im' \
  -H 'x-ig-app-id: 936619743392459' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.instagram.com/_baldgold/followers/' \
  -H 'accept-language: en-US,en;q=0.9,ru;q=0.8' \
  -H 'cookie: ig_did=D52BCDDD-C82A-4F01-812C-065025A20749; mid=XtgMOQAEAAF-77qnHNUzpDnqTz_w; csrftoken=ezsRIKt6wI61vvcDziGGrE3dp4Rm08Im; ds_user_id=969454378; sessionid=969454378%3ARgHStuOlPxawXv%3A18; shbid=13258; shbts=1593351917.920729; rur=VLL; urlgen="{{\"5.228.94.80\": 42610}}:1jqEIP:_ONPvOTwy7i4W_r1wDEBWp9Q0j8"' \
  --compressed > json/followers_{index}.json"""

index = 1
after = None
followers_in_progress = 0

while True:
    after_value = f',"after":"{after}"' if after else ''
    variables = f'{{"id": "969454378", "include_reel": true, "fetch_mutual": true, "first": 50{after_value}}}'
    get_params = {
        'query_hash': 'c76146de99bb02f6415203be841dd25a',
        'variables': variables
    }
    ws_url = url_base + urllib.parse.urlencode(get_params)

    result = subprocess.run(command_template.format(url= ws_url, index=index), shell=True, capture_output=True)
    if result.returncode != 0:
        exit("Произошло зло! Отбой!")
        
    with open(f'json/followers_{index}.json') as f:
        data = json.load(f)

    if not data['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        break

    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers = data['data']['user']['edge_followed_by']['count']
    in_current_batch = len(data['data']['user']['edge_followed_by']['edges'])
    followers_in_progress += in_current_batch
    print(f'Обратобано {followers_in_progress}/{all_followers}')

    time.sleep(1 if index % 10 != 0 else 20)
    index += 1

print("Дело сделано!")