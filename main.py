import json
import requests
import regex as re

pattern = re.compile("RegEx for IP here")

patternT = re.compile("RegEx for IP here")

cloudflare_api = "https://api.cloudflare.com/client/v4/"
zone_id = "zone id here"
account_id = "account id here"
auth_key = "Bearer token here"
headers = {'Authorization': auth_key, 'Content-Type':'application/json'}

cloudflare_dns = cloudflare_api + "zones/?per_page=50"  
cloudflare_dns_respon = requests.get(cloudflare_dns, headers=headers)

if cloudflare_dns_respon.status_code == 200:
    print("Ok")
else:
    print(cloudflare_dns_respon.status_code)    

dns_data = json.loads(cloudflare_dns_respon.text)
dns_data = dns_data['result']
list_of_ids = []

for i in dns_data:
    list_of_ids.append(i['id'])

    
cloudflare_dns = cloudflare_api + "zones/?per_page=50&page=2"  
cloudflare_dns_respon = requests.get(cloudflare_dns, headers=headers)

dns_data = json.loads(cloudflare_dns_respon.text)
dns_data = dns_data['result']
for i in dns_data:
    list_of_ids.append(i['id'])

print(len(list_of_ids))

for id in list_of_ids:
    cloudflare_dns = cloudflare_api + "zones/" + id + "/dns_records"  
    cloudflare_dns_respon = requests.get(cloudflare_dns, headers=headers)

    if cloudflare_dns_respon.status_code == 200:
        dns_data = json.loads(cloudflare_dns_respon.text)
        dns_data = dns_data['result']
        for i in dns_data:
            if pattern.match(i['content']):
                print(f"{i['name']} esta no Server1")
            elif patternT.match(i['content']):
                print(f"{i['name']} esta no Server2")

    else:
        print(cloudflare_dns_respon.status_code)   
        continue
