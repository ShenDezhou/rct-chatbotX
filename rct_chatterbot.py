import urllib
from requests_toolbelt import MultipartEncoder
import json

import requests

MEDUSA='http://localhost:5000'
#create
name = "rct-qi-liuli-20210601"
key = 'ac92ffbf-bf43-400f-9f1f-1f363d340b5e'
create = False
train = True
test = False
if create:
    create_api = MEDUSA+'/api-v1/bot/create/'
    header = {'Authorization': '9aGM5qSvaTUQvWHfdJvLuY7g3BdR4gSReSXJAzWARjkX2x6H',
              "Content-Type": "application/json"}
    payload = {
        "name": name
    }
    r = requests.post(create_api, headers=header, data=json.dumps(payload))
    print(r.json())
    key = r.json()['response']['key']


if train:
    train_api = MEDUSA+'/api-v1/bot/train/'
    payload = {
        "name": name,
        'key': key,
        'file': ('file', open('data/sms.yml', 'rb'), 'text/plain')
    }
    m = MultipartEncoder(fields=payload)
    header = {'Authorization': '9aGM5qSvaTUQvWHfdJvLuY7g3BdR4gSReSXJAzWARjkX2x6H',
              "Content-Type": m.content_type}
    r = requests.post(train_api, headers=header, data=m)
    print(r.json())
    msg = r.json()['response']
    print(msg)

if test:
    payload = {'key': key, 'name':name, 'text': '什么是ai'}
    response_api = MEDUSA+'/api-v1/bot/get_response?' + urllib.parse.urlencode(payload)
    r = requests.get(response_api)
    print(r.json())
    response = r.json()['response']
    print(payload['text'])
    print(response)




