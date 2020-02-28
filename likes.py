from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

browser = webdriver.Chrome(executable_path='./chromedriver')


browser.get('http://www.facebook.com')
elem = browser.find_element_by_name('email')

elem.send_keys(os.environ['FB_ID'])

elem = browser.find_element_by_name('pass')

elem.send_keys(os.environ['FB_PASS'])

# h=['2','b','4']
# for i in h:
# 		elem = browser.find_element_by_xpath('//*[@id="u_0_'+i+'"]')
# 		elem.click()

elem = browser.find_element_by_xpath('//*[@id="u_0_b"]')
elem.click()

#it worked!
