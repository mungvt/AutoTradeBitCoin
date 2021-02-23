import json
import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['DEFAULT']['TOKEN']
query = {
  "q": {
    "find": { "out.s2": "19HxigV4QyBv3tHpQVcUEQyq1pzZVdoAut", "blk.i": { "$gt": 609000 } },
    "sort": { "blk.i": 1 },
    "project": { "blk": 1, "tx.h": 1, "out.s4": 1, "out.o1": 1 }
  }
}
headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'token': TOKEN }
body = json.dumps(query)
r = requests.post(f'https://txo.bitbus.network/block',
                  headers=headers,
                  data=body,
                  stream=True)
for line in r.iter_lines():
    print(json.loads(line))