#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Goes to the ShotQuality Website
driver.get("https://shotquality.com/team/college_mens/2023/Chattanooga")
#Checks if "ShotQuality" is in the title to varify we are in the right place
assert "ShotQuality" in driver.title 
#Finds the Class for the rankList on the webpage and selects it as elem
elem = driver.find_element_by_class_name("rankList")
#screenshots elem and names the file 'foo.png'
elem.screenshot('foo.png')