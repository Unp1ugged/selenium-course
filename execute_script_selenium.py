from selenium import webdriver
import math
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")
x = browser.find_element_by_id("input_value").text
solve = str(math.log(abs(12*math.sin(int(x)))))
browser.execute_script("window.scrollBy(0, 150);")
browser.find_element_by_id("answer").send_keys(solve)
browser.find_element_by_class_name("form-check-label").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_tag_name("button").click()
