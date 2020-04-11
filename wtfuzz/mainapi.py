from wtfuzz_core import wtfuzz
import requests
import json

MITMPROXY_ENDPOINT = 'http://localhost:8081/getFolders'

body = {}

body['domain'] = "localhost"
body['file'] = "testzap.txt"

r = requests.post(MITMPROXY_ENDPOINT, json=body)
if (r.status_code == 200):
    folders = json.loads(r.content)
    filename = 'actuatortest.txt'
    wtf = wtfuzz()
    for folder in folders:
        wtf.config(url=folder, filename=filename)
        # wtf.sendAllVerbsRequest()
        wtf.sendFullRequest("GET")
