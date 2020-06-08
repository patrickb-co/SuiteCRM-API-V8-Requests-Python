import requests

# sample account data
randomusers = 'https://api.randomuser.me'
def getUsers(endpoint):
    r = requests.get(endpoint)
    
    results_first = format(r.json()["results"][0]["name"]["first"])
    results_last = format(r.json()["results"][0]["name"]["last"])
    full_name = " ".join([results_first, results_last])
    return full_name

#suitecrm api request data:
instance_api_url = "http://localhost:8888/SuiteCRM-7.11.13/Api/"
module_name = "Accounts"
auth_url = instance_api_url + "access_token"
modules_url = instance_api_url + "V8/module/" + module_name 
post_url = instance_api_url + "V8/module"
#example
# set it on SuiteCRM Admin/OAuth2 Clients and Tokens
client_id = "" 
client_secret = ""
# regular SuiteCRM user
username = ""
password = ""

data = '{"data": {"type": "' + module_name + '","attributes": {"name":"' + getUsers(randomusers) + '"}}}'


def authenticateSuiteCRM(auth_url, client_id, client_secret, username, password):  
    payload = {"grant_type":"password","client_id":client_id,"client_secret":client_secret,"username":username,"password":password}
    auth_request = requests.post(auth_url,data = payload)
    crm_token = format(auth_request.json()["access_token"])
    header_str = "Bearer " + crm_token
    headers = {"Authorization": header_str, "Content-Type":"application/json"}

    return headers

def getAccounts(url):
    request = requests.get(url, headers = authenticateSuiteCRM(auth_url,client_id,client_secret,username,password))
    return format(request.json())

def postAccount(url):
    request = requests.post(url, headers = authenticateSuiteCRM(auth_url,client_id,client_secret,username,password), data = data)
    return format(request.json())

print(getAccounts(modules_url))

print(postAccount(post_url))
