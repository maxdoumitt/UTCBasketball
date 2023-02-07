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
    "Jake Stephens",
    "Jamaal Walker",
    "Brody Robinson"
    #etc...
]
players_length = len(players)


#Code Begins ↓


#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Let the page load for a few seconds
def wait():
    time.sleep(5)

#delete an element from the page. select the item to delete by putting className contents in the parameters
def remove_by_class(x):
    driver.execute_script("return document.getElementsByClassName('"+x+"')[0].remove();")

#Opens to the team's page on the ShotQuality website
def open_shot_quality():
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


#screenshots the teams general stats
def capture_team_stats():
    #Scroll until Element is within the screen
    team_stats = driver.find_element(By.XPATH, "//ul[@class=\"list-description rankList\"]")
    driver.execute_script("arguments[0].scrollIntoView();", team_stats)
    #remove navbar
    remove_by_class("header fixed-header")
    #Screenshot the main team stats
    team_stats.screenshot('UTC Basketball\img\shot_quality_team_stats.png')

#opens specific players page
def player_page(player_name):
    #finds the link to the player's stat page by finding the link that matches the players name which is pulled from the players[] array
    player_link = driver.find_element(By.LINK_TEXT, player_name)
    player_link.click()
    wait()
    #define page sections
    player_stats = driver.find_element(By.XPATH, "//ul[@class=\"list-description rankList h-auto w-100\"]")
    player_in_cards = driver.find_element(By.XPATH, "//section[@class=\"mt-2 mb-4\"]")
    player_stats_table = driver.find_element(By.XPATH, "//div[@class=\"Scoreside text-center new\"]")
    player_stats_table_scroller = driver.find_element(By.XPATH, "//div[@class=\"Yearside\"]")
    #scroll to and capture player_stats
    driver.execute_script("arguments[0].scrollIntoView();", player_stats)
    player_stats.screenshot('UTC Basketball\img\\'+player_name+'shot_quality_player_stats.png')
    wait()
    #scroll to and capture player_in_cards. If theres no player_cards: pass
    try: #if there are player_in_cards, capture them
        driver.execute_script("arguments[0].scrollIntoView();", player_in_cards)
        player_in_cards.screenshot('UTC Basketball\img\\'+player_name+'shot_quality_player_in_cards.png')
        wait()
    except: #if there are not player_in_cards, pass
        pass
    #scroll to filter scroller and capture player_stats_table
    try: #if there is a player_stats_table, capture it
        driver.execute_script("arguments[0].scrollIntoView();", player_stats_table_scroller)
        player_stats_table.screenshot('UTC Basketball\img\\'+player_name+'shot_quality_player_stats_table.png')
        wait()
    except: #if there is not a player_stats_table, pass
        pass
    #goes back to main team page
    driver.back()
    wait()


def main():
    open_shot_quality()
    capture_team_stats()
    for i in range(players_length):
        player_page(players[i])

main()
#pauses program at end
time.sleep(30)
