from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

browser = webdriver.Chrome(executable_path='./chromedriver')


browser.get('http://www.facebook.com')
elem = browser.find_element_by_name('email')

elem.send_keys(os.environ['FB_ID'])

elem = browser.find_element_by_name('pass')

elem.send_keys(os.environ['FB_PASS'])

h=['2','b','4']
for i in h:
    try:
        elem = browser.find_element_by_xpath('//*[@id="u_0_'+i+'"]')
        elem.click()
    except:
         print("try")
browser.get('https://www.facebook.com/NASA/photos/a.67899501771/10157957295556772/?type=3&theater')

elem = browser.find_element_by_class_name('_3dlf')
print(elem)
link = elem.get_attribute('href')

browser.get(link)

elem = browser.find_element_by_xpath('//*[@id="js_0"]/ul')
print(elem.text)



#it worked!! UN-CRASHABLE
