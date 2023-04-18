from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from PIL import Image
import datetime
from datetime import date
import os
import teamSearches

#Instance Variables
chatt_blue = HexColor('#2f5597')
opp_red = HexColor('#c80404')
year = datetime.date.today().year
lastyear = year-1

#Check if the path, specified by the parameter, exists
def path_check(path):
    return os.path.exists(path)

#Common Imported Variables
today_date = date.today()

number_of_players = len(teamSearches.fast_scout_collection)


offense_items = [
    "Depth:",
    "Play Style:",
    "Pace:",
    "Efficiency:",
    "Shot Making:",
    "Shot Volume:",
    "Shot Selection:"
]

defense_items = [
    "Scheme:",
    "Pace:",
    "Efficiency:"
]

filename = "Textless Pregame Report "+str(today_date)+".pdf"
c = canvas.Canvas(filename)
form = c.acroForm
c.setTitle(filename)

#Creates Cover Page
def cover_page(opponent_name):
    #Writes the header
    c.setFont("Helvetica-Bold", 46)
    c.setFillColor(colors.black)
    c.drawCentredString(300, 730, "Chattanooga vs")
    c.drawCentredString(300, 685, opponent_name) 
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(300, 650, "Game #") #Input Game Number
    c.drawCentredString(300, 610, "Date") #Input Game Date
    #input UTC Image
    c.drawInlineImage("UTC Basketball\\boiler_plates\\Chattanooga.png", 200, 385, 200, 200)
    #Write Vs
    c.drawCentredString(300, 360, "vs")
    #input Opponent Image
    c.drawInlineImage("UTC Basketball\img\general_team_data\\"+opponent_name+"_logo_image.png", 200, 135, 200, 200)
    

#Creates the Overview Page
def overview_page(opponent_name):
    #inputs UTC Image
    c.drawInlineImage("UTC Basketball\\boiler_plates\\Chattanooga.png", 275, 775, 50, 50)
    #Overview Text Box
    c.setFillColor(chatt_blue)
    c.rect(50, 715, 495, 50, 0, 1)
    c.setFont("Helvetica", 38)
    c.setFillColor(colors.white)
    c.drawCentredString(300, 730, "Overview")
    #Prompts for coach, records, and SoCon Standing
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(120, 680, "Head Coach:")
    c.drawString(120, 660, str(lastyear)+" Record:")
    c.drawString(120, 640, str(year)+" Record:")
    c.drawString(120, 620, "SoCon Standing:")
    #Text Field Inputs for the prompts
    #Scout Report Text Box
    c.setFillColor(chatt_blue)
    c.rect(110, 570, 370, 15, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 10)
    c.drawCentredString(300, 575, "Scouting Report")
    #Inputs the teams General Stats from Shot Quality
    c.drawInlineImage("UTC Basketball\img\general_team_data\shot_quality_"+opponent_name+"_stats.png", 110, 420, 370, 150)
    #What We Must Do To Win Text Box
    c.setFillColor(chatt_blue)
    c.rect(50, 360, 495, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 370, "What We Must Do To Win")
    #Creates a Slew of Text Boxes for the Winning Strategies to be written
    
def opponent_offense_page(opponent_name):
    #Opponent Offense Text Box
    c.setFillColor(opp_red)
    c.rect(50, 760, 495, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 770, opponent_name+" Offense") #Input Enemy Team Name
    #makes the first 7 Prompts and Text Field Inputs
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    hite = 730
    for i in range(len(offense_items)):
        c.drawString(75, hite, offense_items[i]) 
        hite-=30
    #Shot Profile Prompts and Text Field Inputs
    c.drawString(75, 470, "Shot Profile:")
    #Summary Prompt and Text Field Inputs
    c.drawString(75, 285, "Summary:")

    
        
def opponent_defense_page(opponent_name):
    #Opponent Defense Text Box
    c.setFillColor(opp_red)
    c.rect(50, 760, 495, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 770, opponent_name+" Defense") #Input Enemy Team Name
    #makes the first 3 Prompts and Text Field Inputs
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 14)
    hite = 730
    #Shot Profile Prompts and Text Field Inputs
    c.drawString(75, 610, "Shot Profile:")
    #Summary Prompt and Text Field Inputs
    hite = 490
    c.drawString(75, hite, "Summary:")
    #Their Opponent Shot Chart Text Box
    c.setFillColor(opp_red)
    c.rect(175, 210, 250, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 220, "Their Opponents:") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\\boiler_plates\\shot_chart_boiler_plate.png", 175, 25, 250, 185)

def shooting_page(opponent_name):
    #Shooting Text Box
    c.setFillColor(opp_red)
    c.rect(50, 760, 495, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 770, "Shooting")
    #input team stats table
    c.drawInlineImage("UTC Basketball\img\general_team_data\\bartorvik_"+opponent_name+"_table.png", 75, 610, 450, 140)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(75, 580, "Notes:")
    #Opponent Shot Chart Text Box
    c.setFillColor(opp_red)
    hite = 400
    c.rect(175, hite, 250, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, hite+10, "Season Shot Chart") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\\boiler_plates\\shot_chart_boiler_plate.png", 175, 215, 250, 185)

def player_page(box_score, image, table, stats, name, table_sizes):
    c.drawInlineImage(box_score, 75, 600, 500, 150)
    img = Image.open(image)
    c.drawInlineImage(image, 75, 730, img.width/1.5, img.height/1.5)
    #c.drawInlineImage(image, 75, 730, 70, 75)
    c.drawInlineImage(table, table_sizes[0], table_sizes[1], table_sizes[2], table_sizes[3])
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 20)
    c.drawString(200, 760, name)
    #Scouting Report Text Box
    c.setFillColor(opp_red)
    c.rect(340, 520, 180, 20, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawString(375, 525, "Scouting Report")
    #input Scouting Report Image. Change the sizing depending on the size.
    pil_stats = Image.open(stats)
    if pil_stats.height > 680:
        c.drawInlineImage(stats, 260, 310, 340, 210)
    elif pil_stats.height > 550:
        c.drawInlineImage(stats, 260, 330, 340, 190)
    elif pil_stats.height > 500:
        c.drawInlineImage(stats, 260, 350, 340, 170)
    elif pil_stats.height > 350:
        c.drawInlineImage(stats, 260, 390, 340, 130)
    else: 
        c.drawInlineImage(stats, 260, 440, 340, 80)
    #white boxes to block out excess from scouting report image
    c.setFillColor(colors.white)
    c.rect(190, 200, 150, 350, 0, 1)
    c.rect(520, 200, 150, 350, 0, 1)
    #Shot Chart Text Box
    c.setFillColor(opp_red)
    c.rect(95, 520, 170, 20, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawString(140, 525, "Shot Chart") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\\boiler_plates\\shot_chart_boiler_plate.png", 95, 365, 170, 155)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(75, 330, "Color:")
    c.drawString(75, 300, "Notables:")
    c.drawString(75, 230, "Bottom Line:")

def createPDF(team_name):
    cover_page(team_name)
    c.showPage()
    overview_page(team_name)
    c.showPage()
    opponent_offense_page(team_name)
    c.showPage()
    opponent_defense_page(team_name)
    c.showPage()
    shooting_page(team_name)
    c.showPage()
    for i in range(len(teamSearches.fast_scout_collection)):
        player_name = teamSearches.fast_scout_collection[i]
        if path_check("UTC Basketball\\img\\"+player_name+"\\"+player_name+"_fast_scout_box_score.png"):
            fast_scout_box_score = "UTC Basketball\\img\\"+player_name+"\\"+player_name+"_fast_scout_box_score.png"
        else:
            fast_scout_box_score = "UTC Basketball\\boiler_plates\\boiler_plate_fast_scout_box_score.png"
        if path_check("UTC Basketball\\img\\"+player_name+"\\"+player_name+"_fast_scout_image.png"): 
            fast_scout_image = "UTC Basketball\\img\\"+player_name+"\\"+player_name+"_fast_scout_image.png"
        else: 
            fast_scout_image = "UTC Basketball\\boiler_plates\\boiler_plate_fast_scout_image.png"
        if path_check("UTC Basketball\\img\\"+player_name+"\\shot_quality_player_stats_table.png"):
            shot_quality_player_stats_table = "UTC Basketball\\img\\"+player_name+"\\shot_quality_player_stats_table.png"
            table_dimensions = [25, 540, 600, 90]
        else:
            shot_quality_player_stats_table = "UTC Basketball\\boiler_plates\\boiler_plate_shot_quality_player_stats_table.png"
            table_dimensions = [100, 570, 400, 60]
        if path_check("UTC Basketball\\img\\"+player_name+"\\shot_quality_player_stats.png"):
            shot_quality_player_stats = "UTC Basketball\\img\\"+player_name+"\\shot_quality_player_stats.png"
        else:
            shot_quality_player_stats = "UTC Basketball\\boiler_plates\\boiler_plate_shot_quality_player_stats.png"

        player_page(fast_scout_box_score, fast_scout_image, shot_quality_player_stats_table, shot_quality_player_stats, player_name, table_dimensions)
        c.showPage()
    c.save()
