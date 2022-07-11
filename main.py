import json

import requests
def resolve_ip(ip):
    url = "https://ip-location5.p.rapidapi.com/get_geo_info"

    payload = "ip="+ip
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "0a57485de3msh599b0b9ad124aeap14d1c8jsndbacf236da77",
        "X-RapidAPI-Host": "ip-location5.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(json.loads(response.text)['country']['name'])
    return json.loads(response.text)['country']['name']

lines =[]
for line in open('log.txt'):
    sp = line.split()
    lines.append(sp)
ips=set([x[0] for x in lines])
counties=set([resolve_ip(x) for x in ips])
print(counties)

