import Lesson3_part2
# from Lesson3_part2 import div
# try:
#     div(10, 0)
# except TypeError.:
#     print("TypeError")
# except ZeroDivisionError.:
#     print("ZeroDivisionError")
# except Exception:
#     print(e.args)
#     print("division error")

# from Lesson3 import check_website
import requests

def check_website(url):
    url = input()
    req = requests.get(url)
    print(req)
    if req.status_code == 200:
        print("is ok")


try:
    url = input()
    check_website(url)
except MissingSchema:
    print("you have a schema issue")
    raise ("Github is a bad website")
