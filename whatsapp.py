#!/usr/bin/env python2
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://web.whatsaap.com/')

name = input('Enter the name of user or group :')
msg = input('Enter your message :')
count = int(input('Enter the count '))

input('Enter anythiing after scanning QR code ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('compose-btn-send')
	button.click()

