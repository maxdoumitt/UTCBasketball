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
fast_scout_collection = []



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
        time.sleep(1)
    except:
        pass 


def open_fast_scout():
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
def fast_scout_select_team(chosen_team):
    find_opponent = driver.find_element(By.XPATH, "//span[text()[contains(.,'"+chosen_team+"')]]")
    find_opponent.click()
    wait()

def fast_scout_collect_player_names(i):
    try:
        i=i+1
        player_name_link = driver.find_element(By.XPATH, "//table[@id=\"undefined-boxscore\"]/tbody/tr["+str(i)+"]/td[4]")#/span/a/span/div")
        player_name_complete = player_name_link.text
        i=i-1 
        fast_scout_collection.append(player_name_complete)
        time.sleep(1)
    except:
        pass

#Array of dictionary keys for the teams
teams_dictionary_names = [
    "Chattanooga",
    "VMI",
    "Tennessee Tech",
    "Charleston",
    "Mississippi",
    "Lipscomb",
    "Murray St.",
    "Gardner Webb",
    "Milwaukee",
    "Middle Tennessee",
    "Belmont",
    "Georgia",
    "The Citadel",
    "Mercer",
    "UNC Greensboro",
    "Western Carolina",
    "Samford",
    "Furman",
    "East Tennessee St.",
    "Wofford",
]

#This represents the team(s) the user chose to look at from the drop down menu.
selected_teams_dictionary_names = [
    "Mercer"
]

#teams nested Dictionary

teams = {
    #to add a new team to the program: 
        #copy the code between the arrows, 
        #remove the #'s, 
        #replace info in brackets[] with new teams info.
        #Use the other entries as example 
        #team names ARE CAPS SENSITIVE so make sure to capitolize the same way as it is in the site or it won't work
        #add the [College Name] as an entry in the array above as well
    # ↓
    #"[College Name]" : {
       #"ShotQuality":"[team name on shotquality site]",
       #"FastScout":"[team name on FastScout site]"
       #"Bartorvik":"[team name on Bartorvik site]"
    #},
    # ↑ 
    "Chattanooga" : {
        "ShotQuality":"Chattanooga",
        "FastScout":"UTC Mocs",
        "Bartorvik":"Chattanooga"
    },
    
    "VMI" : {
        "ShotQuality":"VMI",
        "FastScout":"VMI Keydets",
        "Bartorvik":"VMI"
    },

    "Tennessee Tech" : {
        "ShotQuality":"Tennessee Tech",
        "FastScout":"Tennessee Tech Golden Eagles",
        "Bartorvik":"Tennessee Tech"
    },

    "Charleston" : {
       "ShotQuality":"Charleston",
       "FastScout":"Charleston Cougars",
       "Bartorvik":"College of Charleston"
    },

    #"Oakland City Mighty Oaks" : {
       #"ShotQuality":"[team name on shotquality site]",
       #"FastScout":"Oakland City Mighty Oaks",
       #"Bartorvik":"[team name on Bartorvik site]"
    #},

    "Mississippi" : {
       "ShotQuality":"Mississippi",
       "FastScout":"Ole Miss Rebels",
       "Bartorvik":"Mississippi"
    },

    "Lipscomb" : {
       "ShotQuality":"Lipscomb",
       "FastScout":"Lipscomb Bisons",
       "Bartorvik":"Lipscomb"
    },

    "Murray St." : {
       "ShotQuality":"Murray St.",
       "FastScout":"Murray St. Racers",
       "Bartorvik":"Murray St."
    },

    "Gardner Webb" : {
       "ShotQuality":"Gardner Webb",
       "FastScout":"Gardner-Webb Runnin' Bulldogs",
       "Bartorvik":"Gardner Webb"
    },

    "Milwaukee" : {
       "ShotQuality":"Milwaukee",
       "FastScout":"Milwaukee Panthers",
       "Bartorvik":"Milwaukee"
    },

    "Middle Tennessee" : {
       "ShotQuality":"Middle Tennessee",
       "FastScout":"Middle Tennessee Blue Raiders",
       "Bartorvik":"Middle Tennessee"
    },

    "Belmont" : {
       "ShotQuality":"Belmont",
       "FastScout":"Belmont Bruins",
       "Bartorvik":"Belmont"
    },

    "Georgia" : {
       "ShotQuality":"Georgia",
       "FastScout":"Georgia Bulldogs",
       "Bartorvik":"Georgia"
    },

    "The Citadel" : {
       "ShotQuality":"The Citadel",
       "FastScout":"The Citadel Bulldogs",
       "Bartorvik":"The Citadel"
    },

    "Mercer" : {
        "ShotQuality":"Mercer",
       "FastScout":"Mercer Bears",
       "Bartorvik":"Mercer"
    },

    "UNC Greensboro" : {
       "ShotQuality":"UNC Greensboro",
       "FastScout":"UNC Greensboro Spartans",
       "Bartorvik":"UNC Greensboro"
    },

    "Western Carolina" : {
       "ShotQuality":"Western Carolina",
       "FastScout":"Western Carolina Catamounts",
       "Bartorvik":"Western Carolina"
    },

    "Samford" : {
       "ShotQuality":"Samford",
       "FastScout":"Samford Bulldogs",
       "Bartorvik":"Samford"
    },

    "Furman" : {
       "ShotQuality":"Furman",
       "FastScout":"Furman Paladins",
       "Bartorvik":"Furman"
    },

    "East Tennessee St." : {
       "ShotQuality":"East Tennessee St.",
       "FastScout":"ETSU Buccaneers",
       "Bartorvik":"East Tennessee St."
    },

    "Wofford" : {
       "ShotQuality":"Wofford",
       "FastScout":"Wofford Terriers",
       "Bartorvik":"Wofford"
    },

    #"Covenant Scots" : {
       #"ShotQuality":"[team name on shotquality site]",
       #"FastScout":"Covenant Scots",
       #"Bartorvik":"[team name on Bartorvik site]"
    #},  
     
    #"Johnson (TN)" : {
       #"ShotQuality":"[team name on shotquality site]",
       #"FastScout":"Johnson (TN)",
       #"Bartorvik":"[team name on Bartorvik site]"
    #,  
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
        "ShotQuality": [
            "Asher Woods",
            "Sean Conway",
            "Rickey Bradley"
            ],
        "FastScout": [
            "Asher Woods",
            "Sean Conway",
            "Rickey Bradley, Jr."
            ]
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

x = 0

def collect_shot_quality_names():
    for i in range(len(selected_teams_dictionary_names)):
        x = i
        open_shot_quality()
        shot_quality_select_team(teams[selected_teams_dictionary_names[i]]["ShotQuality"])
        for j in range(len(fast_scout_collection)+2): #I know this is not efficient. It does however work. :D 
            shot_quality_collect_player_names(j)
    print("finishedSQ")

def collect_fast_scout_names():
    for i in range(len(selected_teams_dictionary_names)):
        open_fast_scout()
        fast_scout_select_team(teams[selected_teams_dictionary_names[i]]["FastScout"])
        for j in range(25): #I can run the loop less this time because we defined the team length previously. Still adding 3 for a buffer.
            fast_scout_collect_player_names(j)
    print("finishedFS")
    
def find_players():
    collect_fast_scout_names()
    collect_shot_quality_names()


