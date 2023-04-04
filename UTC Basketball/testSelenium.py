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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#Global variables and functions

#constant variables
delay = 30 # seconds
#Names of Folders to Create
path_names = [
    "UTC Basketball\\img\\general_team_data",
    "UTC Basketball\\img\\shot_quality",
    "UTC Basketball\\img\\fast_scout"
]

#Check if the path, specified by the parameter, exists
def path_check(path):
    return os.path.exists(path)

#website links
fast_scout_login = "https://id.fastmodelsports.com/authorize?response_type=token&client_id=sxeeft0umTGiqwU4-scout&redirect_uri=https%3A%2F%2Ffastscout.fastmodelsports.com"
shot_quality_login = "https://shotquality.com/login"
bartorvik_site = "https://barttorvik.com"

#initialize information about the team in question
team_name = "Chattanooga"

team_list = [
    "Chattanooga",
    "VMI",
    "Tennessee Tech"
]



#Code Begins ↓


#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Let the page load for a few seconds
def wait(x = 2):
    time.sleep(x)

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

def shot_quality_select_team(chosen_team):
    #Selects search bar and types the team name into it
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@type=\"text\"]")))
    search_bar_init = driver.find_element(By.XPATH, "//input[@type=\"text\"]") #Search Bar on Initial Page
    search_bar_init.send_keys(teamSearches.teams[chosen_team]['ShotQuality'])
    #Clicks the FIRST search result when team name is written in
    content_box = driver.find_element(By.XPATH, "//span[@class=\"search-results__text\"]")
    content_box.click()
    #click the team link to open their stats page
    team_link = driver.find_element(By.LINK_TEXT, teamSearches.teams[chosen_team]['ShotQuality'])
    team_link.click()


#screenshots the teams general stats
def capture_shot_quality_team_stats(team_name):
    #Scroll until Element is within the screen
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//ul[@class=\"list-description rankList\"]")))
    team_stats = driver.find_element(By.XPATH, "//ul[@class=\"list-description rankList\"]")
    driver.execute_script("arguments[0].scrollIntoView();", team_stats)
    #remove navbar
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "header")))
    try:
        remove_by_class("header")
    except:
        for i in range(5):
            print("navbar didn't get removed")
    #Screenshot the main team stats
    wait()
    team_stats.screenshot('UTC Basketball\img\general_team_data\shot_quality_'+team_name+'_stats.png')

#opens specific players page
def shot_quality_player_page(player_name):
    #finds the link to the player's stat page by finding the link that matches the players name which is pulled from the players[] array
    player_link = driver.find_element(By.LINK_TEXT, player_name)
    wait(1)
    player_link.click()
    wait(1)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//li[@class=\"pl-3 pr-3 rankElement\"]")))    
    #define page sections
    player_stats = driver.find_element(By.XPATH, "//ul[contains(@class, 'list-description rankList')]")
    player_in_cards = driver.find_element(By.XPATH, "//section[@class=\"mt-2 mb-4\"]")
    player_stats_table = driver.find_element(By.XPATH, "//div[@class=\"Scoreside text-center new\"]")
    player_stats_table_scroller = driver.find_element(By.XPATH, "//div[@class=\"Yearside\"]")
    #scroll to and capture player_stats
    try: #this should work unless the player name doesn't match the player name on the page
        driver.execute_script("arguments[0].scrollIntoView();", player_stats)
        #must wait here because there is a loading blur in the js of the page
        wait(2)
        player_stats.screenshot('UTC Basketball\\img\\shot_quality\\'+player_name+"\\"+player_name+'_shot_quality_player_stats.png')
        #scroll to and capture player_in_cards. If theres no player_cards: pass
        try: #if there are player_in_cards, capture them
            driver.execute_script("arguments[0].scrollIntoView();", player_in_cards)
            player_in_cards.screenshot('UTC Basketball\\img\\shot_quality\\'+player_name+"\\"+player_name+'_shot_quality_player_in_cards.png')
        except: #if there are not player_in_cards, pass
            pass
        #scroll to filter scroller and capture player_stats_table
        try: #if there is a player_stats_table, capture it
            driver.execute_script("arguments[0].scrollIntoView();", player_stats_table_scroller)
            player_stats_table.screenshot('UTC Basketball\\img\\shot_quality\\'+player_name+"\\"+player_name+'_shot_quality_player_stats_table.png')
        except: #if there is not a player_stats_table, pass
            print("error finding player stats table for player \""+player_name+"\" in shot_quality_player_page")
            pass
    except:
        print("error finding player \""+player_name+"\" on ShotQuality Website in shot_quality_player_page")
        pass
    #goes back to main team page
    driver.back()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, player_name)))

def open_fast_scout(chosen_team):
    #go to FastScout website login page
    driver.get(fast_scout_login)
    #maximizes browser
    try:
        driver.maximize_window()
    except:
        print("error maximizing window in open_fast_scout()")
        pass
    #Find Login Info Inputs and  Login Button
    email_input = driver.find_element(By.XPATH, "//input[@type=\"text\"]") #email field
    password_input = driver.find_element(By.XPATH, "//input[@type=\"password\"]") #password field
    login_button = driver.find_element(By.XPATH, "//button[@type=\"submit\"]") #Login Button
    #writes in the login information into the fields priviously found
    email_input.send_keys(logins.email1)
    password_input.send_keys(logins.password3)
    #Clicks Login
    login_button.click() 
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.LINK_TEXT, "OPPONENTS")))
    #Click the Opponents Page
    opponents_page_link = driver.find_element(By.LINK_TEXT, "OPPONENTS")
    opponents_page_link.click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[text()[contains(.,'"+teamSearches.teams[chosen_team]["FastScout"]+"')]]")))
    #find the team in the opponents list
    find_opponent = driver.find_element(By.XPATH, "//span[text()[contains(.,'"+teamSearches.teams[chosen_team]["FastScout"]+"')]]")
    find_opponent.click()

def capture_fast_scout_image_and_stats(player_name, chosen_team):
    #open players box scores page
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[text()[contains(.,'"+player_name+"')]]")))
    find_player_box_stats = driver.find_element(By.XPATH, "//div[text()[contains(.,'"+player_name+"')]]")
    driver.execute_script("arguments[0].scrollIntoView();", find_player_box_stats)
    find_player_box_stats.click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[@class=\"Tile singlePlayerStats top-left-tile\"]")))
    #capture player image
    try:
        find_player_image = driver.find_element(By.XPATH, "//img[@style=\"display: block; margin-right: 0px; object-fit: contain; height: 130px; width: auto; border: none; border-radius: 4px; cursor: inherit; pointer-events: all;\"]")
        find_player_image.screenshot('UTC Basketball\\img\\fast_scout\\'+player_name+"\\"+player_name+'_fast_scout_image.png')
    except:
        print("error finding "+player_name+"'s image in capture_fast_scout_box_scores")
        pass
    #capture player box score
    try:
        capture_player_box_stats = driver.find_element(By.XPATH, "//div[@class=\"Tile singlePlayerStats top-left-tile\"]")
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[text()[contains(.,'All')]]")))
        wait(1)
        capture_player_box_stats.screenshot('UTC Basketball\\img\\fast_scout\\'+player_name+"\\"+player_name+'_fast_scout_box_score.png')
    except:
        print("error finding "+player_name+"'s box scores in capture_fast_scout_box_scores")
        pass
    #goes back to main team page
    driver.back()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//div[text()[contains(.,'"+player_name+"')]]")))

#Opens to the team's page on the ShotQuality website
def open_bartorvik(selected_team):
    #Goes to the ShotQuality Website
    driver.get(bartorvik_site)
    #Load page
    #maximizes browser
    try:
        driver.maximize_window()
    except: 
        pass
    #Find the locations of necessary LOGIN page items
    team_link = driver.find_element(By.LINK_TEXT, teamSearches.teams[selected_team]["Bartorvik"]) #email field
    #open the selected team's page 
    team_link.click()
    wait(4)

def capture_bartorvik_stats(selected_team):
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//span[text()[contains(.,'PRPG!')]]")))
    #I tried to loop this for quite some time with no success so I'e decided to leave it this way. runtime increase should be negligible.
    #Initialize the currently used stat change buttons in array
    PRPG = driver.find_element(By.XPATH, "//span[text()[contains(.,'PRPG!')]]")
    BPM = driver.find_element(By.XPATH, "//span[text()[contains(.,'BPM')]]")
    TS = driver.find_element(By.XPATH, "//span[text()[contains(.,'TS%')]]")
    OREB = driver.find_element(By.XPATH, "//span[text()[contains(.,'O Reb%')]]")
    DREB = driver.find_element(By.XPATH, "//span[text()[contains(.,'D Reb%')]]")
    AST = driver.find_element(By.XPATH, "//span[text()[contains(.,'Ast%')]]")
    TOV = driver.find_element(By.XPATH, "//span[text()[contains(.,'TOV')]]")
    BLK = driver.find_element(By.XPATH, "//span[text()[contains(.,'Blk%')]]")
    STL = driver.find_element(By.XPATH, "//span[text()[contains(.,'Stl%')]]")
    THREEPRATE = driver.find_element(By.XPATH, "//span[text()[contains(.,'3P-Rate')]]")

    #click all the buttons to change what the table shows
    try:
        PRPG.click()
    except:
        print("PRPG Error")
        pass
    try:
        BPM.click()
    except:
        print("BPM Error")
        pass
    try:
        TS.click()
    except:
        print("TS Error")
        pass
    try:  
        OREB.click()
    except:
        print("OREB Error")
        pass
    try:    
        DREB.click()
    except:
        print("DREB Error")
        pass
    try:    
        AST.click()
    except:
        print("AST Error")
        pass
    try:    
        TOV.click()
    except:
        print("TOS Error")
        pass
    try:    
        BLK.click()
    except:
        print("BLK Error")
        pass
    try:    
        STL.click()
    except:
        print("STL Error")
        pass
    try:    
        THREEPRATE.click()
    except:
        print("THREEPRATE Error")
        pass
    #variable for the table
    bartorvik_table = driver.find_element(By.XPATH, "//table[@style=\"white-space:nowrap;margin:auto;table-layout:fixed\"]")
    bartorvik_table.screenshot("UTC Basketball\\img\\general_team_data\\bartorvik_"+selected_team+"_table.png")

def main(selected_team):
    #gathers player names from ShotQuality and FastScout
    teamSearches.find_players()
    #Initialize folders to sort images
    for i in range(3):
        if path_check(path_names[i]):
            pass
        else:
            os.mkdir(path_names[i])
    #create the folders for each of the players found during the find_players() function
    #ShotQuality Player Folders
    for i in range(len(teamSearches.shot_quality_collection)):
        if path_check("UTC Basketball\img\shot_quality\\"+teamSearches.shot_quality_collection[i]):
            pass
        else:
            os.mkdir("UTC Basketball\\img\\shot_quality\\"+teamSearches.shot_quality_collection[i])
    #FastScout Player Folders
    for i in range(len(teamSearches.fast_scout_collection)):
        if path_check("UTC Basketball\\img\\fast_scout\\"+teamSearches.fast_scout_collection[i]):
            pass
        else:
            os.mkdir("UTC Basketball\\img\\fast_scout\\"+teamSearches.fast_scout_collection[i])
    #Start of ShotQuality Stuff
    #open ShotQuality website and logs in
    open_shot_quality()
    #opens the teams page in ShotQuality
    shot_quality_select_team(selected_team)
    #capture general team stats from ShotQuality
    capture_shot_quality_team_stats(selected_team)
    #Capture specific players stat data and loop through the list of white listed players
    for i in range(len(teamSearches.shot_quality_collection)):
        shot_quality_list = sorted(teamSearches.shot_quality_collection)
        shot_quality_player_page(shot_quality_list[i])
    #End of ShotQuality Stuff
    #Start of FastScout Stuff
    #open fast scout website to the opponents page
    open_fast_scout(selected_team)
    #loops through the players and gets their boxscore scores
    for i in range(len(teamSearches.fast_scout_collection)):
        try:
            capture_fast_scout_image_and_stats(teamSearches.fast_scout_collection[i], selected_team)
        except: 
            print("error finding "+teamSearches.fast_scout_collection[i]+" in capture_fast_scout_box_scores()")
            pass
    #End of FastScout stuff
    open_bartorvik(selected_team)
    capture_bartorvik_stats(selected_team)

main(teamSearches.selected_teams_dictionary_names[0])
