# import requests
# from time import sleep

from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="/Users/mor/Downloads/chromedriver")

my_driver.get("https://translate.google.co.il/?hl=iw")

# ChromeOptions options = new ChromeOptions();
# options.addArguments("--disable-extensions")


search_input_box = my_driver.find_element_by_class_name("er8xn")
print(search_input_box)


# search_input_box = my_driver.find_element_by_name("q")
# search_input_box.send_keys("Selenium")
# search_input_box.send_keys(Keys.ENTER)


# email_box = my_driver.find_element_by_id("email")
# email_box.send_keys("lion king")
# addres_box = my_driver.find_element_by_id("pass")
# addres_box.send_keys("lion king")
# search_click = my_driver.find_element_by_name("login")
# search_click.click()

# search_input_box = my_driver.find_element_by_id("i5")
#
# print(search_input_box)
# my_driver.find_element_by_class_name("V5PAJd")
# my_driver.find_element_by_class_name("tm8pq")

# my_driver = webdriver.Chrome(executable_path="/Users/mor/Downloads/chromedriver")
# my_driver.get("https://youtube.com")

