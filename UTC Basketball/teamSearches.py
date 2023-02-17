#gathering necessary team and player information
import logins
#general imports
import time
import os
#Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select



#website links
fast_scout_login = "https://id.fastmodelsports.com/authorize?response_type=token&client_id=sxeeft0umTGiqwU4-scout&redirect_uri=https%3A%2F%2Ffastscout.fastmodelsports.com"
shot_quality_login = "https://shotquality.com/login"
#Sets Chrome as web browser (Install Chrome & Chromium)
driver = webdriver.Chrome()
#Let the page load for a few seconds
def wait():
    time.sleep(5)

shot_quality_collection = []
fast_scout_player_name_array = ["John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe","John Doe"]



def open_shot_quality():
    #Goes to the ShotQuality Website
    driver.get(shot_quality_login)
    #Checks if "ShotQuality" is in the title to varify we are in the right place
    assert "ShotQuality" in driver.title 
    #Load page
    #maximizes browser
    try:
        driver.maximize_window()
    except:
        pass
    #Find the locations of necessary LOGIN page items
    wait()
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
    search_bar_init.send_keys(teams[chosen_team]["ShotQuality"])
    #Clicks the FIRST search result when team name is written in
    content_box = driver.find_element(By.XPATH, "//span[@class=\"search-results__text\"]")
    content_box.click()
    #click the team link to open their stats page
    team_link = driver.find_element(By.LINK_TEXT, teams[chosen_team]["ShotQuality"])
    team_link.click()
    wait()
            
#if anyone python literate reads this just know that I am well aware how inefficient this code is.
#I cannot be bothered to spend any more time trying to get the index of the html list to limit the loop so I will just brute force my way thorugh with try/except.
#efficiency is not currently the ultimate goal 
def shot_quality_collect_player_names(i):
    try:
        #adjusts for the index differences between python and the html that exists for some reason.
        i=i+1
        #gets the XPATH for the list item of the player name specified by the index of the loop
        player_name_link = driver.find_element(By.XPATH, "//table[@class=\"table playerStats\"]/tbody/tr["+str(i)+"]/td[1]/a")
        #sets the player's name as a temp variable
        player_name_complete = player_name_link.text
        #adjusts back. don't think this is necessary but I'm leaving it just in case
        i=i-1
        #appends that above temp variable to the array of ShotQuality player names.
        shot_quality_collection.append(player_name_complete)
        shot_quality_player_name_array = sorted(shot_quality_collection)
        time.sleep(1)
    except:
        print("Player Names done being collected. index = "+str(len(shot_quality_collection)))
        pass



#Array of dictionary keys for the teams
teams_dictionary_names = [
    "Chattanooga",
    "VMI",
    "Tennessee Tech"
]

#teams nested Dictionary

teams = {
    #to add a new team to the program: 
        #copy the code between the arrows, 
        #remove the #'s, 
        #replace info in brackets[] with new teams info.
        #Use the other entries as example 
        #add the [College Name] as an entry in the array above as well
    # ↓
    #"[College Name]" : {
       #"ShotQuality":"[team name on shotquality site]",
       #"FastScout":"[team name on FastScout site]"
    #},
    # ↑ 
    "Chattanooga" : {
        "ShotQuality":"Chattanooga",
        "FastScout":"UTC Mocs"
    },
    
    "VMI" : {
        "ShotQuality":"VMI",
        "FastScout":"VMI Keydets"
    },

    "Tennessee Tech" : {
        "ShotQuality":"Tennessee Tech",
        "FastScout":"Tennessee Tech Golden Eagles"
    }
}

#players nested dictionary
players = {
    "Chattanooga" : {
        "ShotQuality":{
            "John Doe": "John Doe", 
            "John Doe2": "John Doe2"
            },
        "FastScout":{
            "John Doe": "John Doe",
            "John Doe2": "John Doe2"
            }
    },
    
    "VMI" : {
        "ShotQuality":{
            "Asher Woods": "Asher Woods",
            "Sean Conway": "Sean Conway",
            "Rickey Bradley": "Rickey Bradley"
            },
        "FastScout":
            {"Asher Woods": "Asher Woods",
            "Sean Conway": "Sean Conway",
            "Rickey Bradley": "Rickey Bradley, Jr."
            }
    }, 

    "Tennessee Tech" : {
        "ShotQuality":{
            "John Doe": "John Doe", 
            "John Doe2": "John Doe2"
            },
        "FastScout":{
            "John Doe": "John Doe",
            "John Doe2": "John Doe2"
            }
    }
}

def find_players():
    for i in range(len(teams_dictionary_names)):
        open_shot_quality()
        shot_quality_select_team(teams_dictionary_names[i])
        for i in range(25):
            shot_quality_collect_player_names(i)
            print(shot_quality_player_name_array)
            print(shot_quality_player_name_array)
            print(shot_quality_player_name_array)
            print(shot_quality_player_name_array)   

find_players()
time.sleep(20)

