#Import Usernames and Passwords
import logins
import time
#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Global variables and functions
#initialize information about the team in question
team_name = "Chattanooga"


players = [ #list of player names to gather info on
    "player0",
    "player1",
    "player2",
    "player3",
    "player4",
    "player5",
    #etc...
]


#Code Begins ↓


#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Let the page load for a few seconds
def wait():
    time.sleep(5)

#delete an element from the page. select the item to delete by putting className contents in the parameters
def remove_by_class(x):
    driver.execute_script("return document.getElementsByClassName('"+x+"')[0].remove();")

#ShotQuality Screenshot Function
def shot_quality():
    #Goes to the ShotQuality Website
    driver.get("https://shotquality.com/login")
    #Checks if "ShotQuality" is in the title to varify we are in the right place
    assert "ShotQuality" in driver.title 
    #Load page
    wait()
    #maximizes browser
    driver.maximize_window()
    wait()
    #Find the locations of necessary LOGIN page items
    email_input = driver.find_element(By.XPATH, "//input[@type=\"email\"]") #email field
    pass_input = driver.find_element(By.XPATH, "//input[@type=\"password\"]") #password field
    login_button = driver.find_element(By.XPATH, "//button[@type=\"submit\"]") #Login Button
    #writes in the login information into the fields priviously found
    email_input.send_keys(logins.email1)
    pass_input.send_keys(logins.password1)
    #Clicks Login
    login_button.click()
    wait()
    #Selects search bar and types the team name into it
    search_bar_init = driver.find_element(By.XPATH, "//input[@type=\"text\"]") #Search Bar on Initial Page
    search_bar_init.send_keys(team_name)
    wait()
    #Clicks the FIRST search result when team name is written in
    content_box = driver.find_element(By.XPATH, "//span[@class=\"search-results__text\"]")
    content_box.click()
    wait()
    #click the team link to open their stats page
    team_link = driver.find_element(By.LINK_TEXT, team_name)
    team_link.click()
    wait()
    #Scroll until Element is within the screen
    team_stats = driver.find_element(By.XPATH, "//ul[@class=\"list-description rankList\"]")
    driver.execute_script("arguments[0].scrollIntoView();", team_stats)
    #remove navbar
    remove_by_class("header fixed-header")
    #Screenshot the main team stats
    team_stats.screenshot('UTC Basketball\img\shot_quality_team_stats.png')
    #pauses program at end
    time.sleep(111)


shot_quality()