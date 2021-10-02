from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome(executable_path="/Users/mor/Downloads/chromedriver")
# my_driver.get("https://ynet.co.il")
# for i in range(5):
#     sleep(5)
#     my_driver.refresh()

my_driver.get("file://C:/Users/mor/Desktop/צ'ק פוינט/DevOps_Experts/tip_calc/index.html")
bill = my_driver.find_element_by_id("billamt")
assert bill.text == ""
assert bill.get_attribute("placeholder") == "Bill Amount"
bill.send_keys("100")
my_driver.find_element_by_id("serviceQual").send_keys("30")
my_driver.find_element_by_id("peopleamt").send_keys("4")
my_driver.find_element_by_id("calculate").click()
if my_driver.find_element_by_id("tip").text == "7.50":
    print("wow")


assert my_driver.find_element_by_id("tip").text == "7.50"

