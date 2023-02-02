#Import Usernames and Passwords
import logins
#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Global variables and functions
#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Let the page load for a few seconds
def let_load(x):
    driver.implicitly_wait(x) 


#ShotQuality Screenshot Function
def shot_quality():
    #Goes to the ShotQuality Website
    driver.get("https://shotquality.com/login")
    #Checks if "ShotQuality" is in the title to varify we are in the right place
    assert "ShotQuality" in driver.title 
    #Load page
    let_load(150)
    #Find the locations of necessary LOGIN page items
    email_input = driver.find_element(By.XPATH, "//input[@type=\"email\"]") #email field
    pass_input = driver.find_element(By.XPATH, "//input[@type=\"password\"]") #password field
    #writes in the login information into the fields priviously found
    print(email_input)
    print(pass_input)
    let_load(100)
    email_input.send_keys(logins.email1)
    let_load(100)
    pass_input.send_keys(logins.password1)
    let_load(100)

shot_quality()