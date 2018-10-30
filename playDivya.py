import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/divyamsodhi/')

firstBox = browser.find_element_by_class_name('_bz0w')
firstBox.click()

time.sleep(2)
#
for x in range(0,10):
    time.sleep(2)
    secondBox = browser.find_element_by_class_name('OAXCp')
    secondBox.click()

    time.sleep(10)

    next = browser.find_element_by_class_name('coreSpriteRightPaginationArrow')
    next.click()