#!/usr/bin/python

#start programming for githuv login

#import web files
from selenium import webdriver 
from time import sleep 
  
usr=raw_input('Enter Email Id:')  
pwd=raw_input('Enter Password:')  
  
driver = webdriver.Chrome() 
driver.get('https://www.github.com/login') 
print ("Opened Github ") 
sleep(1) 
  
username_box = driver.find_element_by_id('login_field') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_name('commit') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit: ') 
driver.quit() 
print("Finished")
