import json, requests 

url = requests.get("https://api.comick.app/chapter/?page=1&order=new&accept_mature_content=true")
text = url.text

data = json.loads(text)

user = data[0]
print(user['status'])

address = user['chap']
print(address)