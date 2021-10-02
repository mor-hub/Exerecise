
import requests
req = requests.get("http://192.168.43.142:5001//whatismyname")
assert req.status_code == 200
assert req.text == "<font size=7>My name is Doron</font>"
# print(req.text)

# print(requests.post("http://192.168.43.142:5001//whatismyname"))
post1 = (requests.post("http://192.168.43.142:5001//whatismyname"))
print(post1.text)