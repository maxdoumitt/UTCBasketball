#Import other files from this program
import logins
import teamSearches
#general imports
import time
import os
#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Global variables and functions

#constant variables
#website links
fast_scout_login = "https://id.fastmodelsports.com/authorize?response_type=token&client_id=sxeeft0umTGiqwU4-scout&redirect_uri=https%3A%2F%2Ffastscout.fastmodelsports.com"
shot_quality_login = "https://shotquality.com/login"

#initialize information about the team in question
team_name = "Chattanooga"


players = [ #list of player names to gather info on
    "Asher Woods",
    "Sean Conway",
    "Rickey Bradley"
    #etc...
]

#variable for length of player array players[Asher Woods][]
players_length = len(players)

team_list = [
    "Chattanooga",
    "VMI",
    "Tennessee Tech"
]

#Create extra folders in the img folder to subdivide the data for the players
try:
    os.mkdir("UTC Basketball\\img\\general_team_data")
except:
    pass
try:
    for i in range(players_length):
        os.mkdir("UTC Basketball\\img\\"+players[i])
except:
    pass

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
    driver.get(shot_quality_login)
    #Checks if "ShotQuality" is in the title to varify we are in the right place
    assert "ShotQuality" in driver.title 
    #Load page
    #maximizes browser
    driver.maximize_window()
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

def shot_quality_select_team(chosen_team):
    #Selects search bar and types the team name into it
    search_bar_init = driver.find_element(By.XPATH, "//input[@type=\"text\"]") #Search Bar on Initial Page
    search_bar_init.send_keys(teamSearches.teams[chosen_team]['ShotQuality'])
    #Clicks the FIRST search result when team name is written in
    content_box = driver.find_element(By.XPATH, "//span[@class=\"search-results__text\"]")
    content_box.click()
    #click the team link to open their stats page
    team_link = driver.find_element(By.LINK_TEXT, teamSearches.teams[chosen_team]['ShotQuality'])
    team_link.click()
    wait()


#screenshots the teams general stats
def capture_shot_quality_team_stats(team_name):
    #Scroll until Element is within the screen
    team_stats = driver.find_element(By.XPATH, "//ul[@class=\"list-description rankList\"]")
    driver.execute_script("arguments[0].scrollIntoView();", team_stats)
    #remove navbar
    remove_by_class("header fixed-header")
    #Screenshot the main team stats
    team_stats.screenshot('UTC Basketball\img\general_team_data\shot_quality_'+team_name+'_stats.png')

#opens specific players page
def shot_quality_player_page(player_name, i):
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
    try: #this should work unless the player name doesn't match the player name on the page
        driver.execute_script("arguments[0].scrollIntoView();", player_stats)
        player_stats.screenshot('UTC Basketball\img\\'+players[i]+"\\"+player_name+'_shot_quality_player_stats.png')
        wait()
        #scroll to and capture player_in_cards. If theres no player_cards: pass
        try: #if there are player_in_cards, capture them
            driver.execute_script("arguments[0].scrollIntoView();", player_in_cards)
            player_in_cards.screenshot('UTC Basketball\img\\'+players[i]+"\\"+player_name+'_shot_quality_player_in_cards.png')
            wait()
        except: #if there are not player_in_cards, pass
            pass
        #scroll to filter scroller and capture player_stats_table
        try: #if there is a player_stats_table, capture it
            driver.execute_script("arguments[0].scrollIntoView();", player_stats_table_scroller)
            player_stats_table.screenshot('UTC Basketball\img\\'+players[i]+"\\"+player_name+'_shot_quality_player_stats_table.png')
            wait()
        except: #if there is not a player_stats_table, pass
            print("error finding player stats table for player \""+player_name+"\" in shot_quality_player_page")
            pass
    except:
        print("error finding player \""+player_name+"\" on ShotQuality Website in shot_quality_player_page")
        pass
    #goes back to main team page
    driver.back()
    wait()

def open_fast_scout(chosen_team):
    #go to FastScout website login page
    driver.get(fast_scout_login)
    #maximizes browser
    try:
        driver.maximize_window()
    except:
        print("error maximizing window in open_fast_scout()")
        pass
    wait()
    #Find Login Info Inputs and  Login Button
    email_input = driver.find_element(By.XPATH, "//input[@type=\"text\"]") #email field
    password_input = driver.find_element(By.XPATH, "//input[@type=\"password\"]") #password field
    login_button = driver.find_element(By.XPATH, "//button[@type=\"submit\"]") #Login Button
    #writes in the login information into the fields priviously found
    email_input.send_keys(logins.email1)
    password_input.send_keys(logins.password3)
    #Clicks Login
    login_button.click() 
    wait()
    #Click the Opponents Page
    opponents_page_link = driver.find_element(By.LINK_TEXT, "OPPONENTS")
    opponents_page_link.click()
    wait()
    #find the team in the opponents list
    find_opponent = driver.find_element(By.XPATH, "//span[text()[contains(.,'"+teamSearches.teams[chosen_team]["FastScout"]+"')]]")
    find_opponent.click()
    wait()

def capture_fast_scout_image_and_stats(player_name, loops):
    #open players box scores page
    find_player_box_stats = driver.find_element(By.XPATH, "//div[text()[contains(.,'"+player_name+"')]]")
    find_player_box_stats.click()
    wait()
    #capture player image
    try:
        find_player_image = driver.find_element(By.XPATH, "//img[@style=\"display: block; margin-right: 0px; object-fit: contain; height: 130px; width: auto; border: none; border-radius: 4px; cursor: inherit; pointer-events: all;\"]")
        find_player_image.screenshot('UTC Basketball\img\\'+players[loops]+"\\"+player_name+'fast_scout_image.png')
    except:
        print("error finding "+player_name+"'s image in capture_fast_scout_box_scores")
        pass
    #capture player box score
    try:
        capture_player_box_stats = driver.find_element(By.XPATH, "//div[@class=\"Tile singlePlayerStats top-left-tile\"]")
        capture_player_box_stats.screenshot('UTC Basketball\img\\'+players[loops]+"\\"+teamSearches.players[team_list[1]]["FastScout"][players[loops]]+'fast_scout_box_score.png')
    except:
        print("error finding "+teamSearches.players[team_list[1]]["FastScout"][players[loops]]+"'s box scores in capture_fast_scout_box_scores")
        pass
    wait()
    #goes back to main team page
    driver.back()
    wait()




def main():
    #Start of ShotQuality Stuff
    #open ShotQuality website and logs in
    open_shot_quality()
    #opens the teams page in ShotQuality
    shot_quality_select_team(team_list[1])
    #capture general team stats from ShotQuality
    capture_shot_quality_team_stats(team_list[1])
    #Capture specific players stat data and loop through the list of white listed players
    for i in range(players_length):
        shot_quality_player_page(teamSearches.players[team_list[1]]["ShotQuality"][players[i]], i)
    #End of ShotQuality Stuff

    #Start of FastScout Stuff
    #open fast scout website to the opponents page
    open_fast_scout(team_list[1])
    #loops through the players and gets their boxscore scores
    for i in range(players_length):
        try:
            capture_fast_scout_image_and_stats(teamSearches.players[team_list[1]]["FastScout"][players[i]], i)
        except: 
            print("error finding player \""+players[i]+"\" in capture_fast_scout_box_scores()")
            pass
    #End of FastScout stuff

main()
#pauses program at end
time.sleep(30)
