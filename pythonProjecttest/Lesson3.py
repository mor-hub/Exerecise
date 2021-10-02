import datetime
import requests

# print(datetime.datetime.now())

req = requests.get("https://github.com")
print(req)
if req.status_code == 200:
    print("Github is ok")

# def check_website(url):
#     req = requests.get(url)
#     print(req)
#     if req.status_code == 200:
#         print("is ok")
#
#
# try:
#     check_website("www.updates.checkpoint.com")
# except MissingSchema:
#     print("you have a schema issue")
#     raise ("Github is a bad website")

