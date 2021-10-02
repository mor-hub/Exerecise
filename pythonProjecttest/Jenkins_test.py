from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="/Users/mor/Downloads/chromedriver")

my_driver.get("https://translate.google.co.il/?hl=iw")


search_input_box = my_driver.find_element_by_class_name("er8xn")
print(search_input_box)