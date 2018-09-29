#!/usr/bin/env python

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys  

usr=raw_input('Enter email id:')
pwd=raw_input('Enter password:')

driver = webdriver.firefox()
driver.get('https://www.facebook.com/')
print "opened facebook"
sleep(2)


username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ('Emailid entered')
sleep(2)


password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)
print ('password entered')

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print('Done')
input('press anything to quit ')
driver.quit()
print "Finished"




