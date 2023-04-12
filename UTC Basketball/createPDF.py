from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase import pdfform
import datetime
#import teamSearches

#Instance Variables
chatt_blue = HexColor('#2f5597')
opp_red = HexColor('#c80404')
year = datetime.date.today().year
lastyear = year-1

#Common Imported Variables
#filename = teamSearches.selected_teams_dictionary_names[0]+" Document"
filename = "team_name Document.pdf" #Input Opponent Team Name
#opponent_name = teamSearches.selected_teams_dictionary_names[0]
opponent_name = "VMI"
number_of_players = 5


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


c = canvas.Canvas(filename)
form = c.acroForm
c.setTitle(filename)

#Creates Cover Page
def cover_page():
    #Writes the header
    c.setFont("Helvetica-Bold", 46)
    c.setFillColor(colors.black)
    c.drawCentredString(300, 730, "Chattanooga vs")
    c.drawCentredString(300, 685, opponent_name) 
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(300, 650, "Game #") #Input Game Number
    c.drawCentredString(300, 610, "Date") #Input Game Date
    #input UTC Image
    c.drawInlineImage("UTC Basketball\img\Chattanooga.png", 200, 385, 200, 200)
    #Write Vs
    c.drawCentredString(300, 360, "vs")
    #input Opponent Image
    c.drawInlineImage("UTC Basketball\img\general_team_data\\"+opponent_name+"_logo_image.png", 200, 135, 200, 200)
    

#Creates the Overview Page
def overview_page():
    #inputs UTC Image
    c.drawInlineImage("UTC Basketball\img\Chattanooga.png", 275, 775, 50, 50)
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
    form.textfield("Text Field", colors.white, colors.white, colors.black, x = 210, y = 676, width = 200, height = 20, fontSize = 14 )
    form.textfield("Text Field", colors.white, colors.white, colors.black, x = 210, y = 656, width = 200, height = 20, fontSize = 14 )
    form.textfield("Text Field", colors.white, colors. white, colors.black, x = 210, y = 636, width = 200, height = 20, fontSize = 14 )
    form.textfield("Text Field", colors.white, colors.white, colors.black, x = 235, y = 616, width = 175, height = 20, fontSize = 14 )
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
    hite = 320
    while(hite>30):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 100, y = hite, width = 400, height = 20, fontSize = 14 )
        hite-=20
    
def opponent_offense_page():
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
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = hite-5, width = 400, height = 20, fontSize = 14 )
        hite-=30
    #Shot Profile Prompts and Text Field Inputs
    c.drawString(75, 470, "Shot Profile:")
    for i in range(8): 
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = 465-20*i, width = 400, height = 20, fontSize = 14 )
    #Summary Prompt and Text Field Inputs
    c.drawString(75, 285, "Summary:")
    hite = 285
    while(hite>30):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = hite-5, width = 400, height = 20, fontSize = 14 )
        hite-=20
    
        
def opponent_defense_page():
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
    for i in range(len(defense_items)):
        c.drawString(75, hite, defense_items[i]) 
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = hite-5, width = 400, height = 20, fontSize = 14 )
        hite-=30
    #Shot Profile Prompts and Text Field Inputs
    c.drawString(75, 610, "Shot Profile:")
    for i in range(5): 
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = 605-20*i, width = 400, height = 20, fontSize = 14 )
    #Summary Prompt and Text Field Inputs
    hite = 490
    c.drawString(75, hite, "Summary:")
    for i in range(12):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 180, y = hite-5, width = 400, height = 20, fontSize = 14 )
        hite-=20
    #Their Opponent Shot Chart Text Box
    c.setFillColor(opp_red)
    c.rect(175, 210, 250, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, 220, "Their Opponents:") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\img\\boiler_plates\shot_chart_boiler_plate.png", 175, 25, 250, 185)

def shooting_page():
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
    hite = 580
    for i in range(6):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 130, y = hite-5, width = 400, height = 20, fontSize = 14 )
        hite-=20
    #Opponent Shot Chart Text Box
    c.setFillColor(opp_red)
    hite = 400
    c.rect(175, hite, 250, 30, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(300, hite+10, "Season Shot Chart") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\img\\boiler_plates\shot_chart_boiler_plate.png", 175, 215, 250, 185)

player_name = "Player Name"
def player_page():
    c.drawInlineImage("UTC Basketball\img\\fast_scout\DJ Nussbaum\DJ Nussbaum_fast_scout_box_score.png", 75, 600, 500, 150)
    c.drawInlineImage("UTC Basketball\img\\boiler_plates\\boiler_plate_fast_scout_image.png", 75, 730, 55, 75)
    c.drawInlineImage("UTC Basketball\img\shot_quality\Asher Woods\Asher Woods_shot_quality_player_stats_table.png", 25, 540, 600, 90)
    #Shot Chart Text Box
    c.setFillColor(opp_red)
    c.rect(95, 520, 170, 20, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawString(140, 525, "Shot Chart") 
    #input shot Chart Image
    c.drawInlineImage("UTC Basketball\img\\boiler_plates\shot_chart_boiler_plate.png", 95, 365, 170, 155)
    #Scouting Report Text Box
    c.setFillColor(opp_red)
    c.rect(340, 520, 180, 20, 0, 1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica", 16)
    c.drawString(375, 525, "Scouting Report")
    #input Scouting Report Image
    c.drawInlineImage("UTC Basketball\img\\boiler_plates\\boiler_plate_shot_quality_player_stats.png", 340, 310, 180, 210)
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(75, 330, "Color:")
    hite = 330
    form.textfield("Text Field", colors.white, colors.white, colors.black, x = 150, y = hite-5, width = 180, height = 20, fontSize = 14 )
    c.drawString(75, 300, "Notables:")
    hite = 300
    for i in range(3):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 150, y = hite-5, width = 180, height = 20, fontSize = 14 )
        hite-=20
    c.drawString(75, 230, "Bottom Line:")
    hite = 230
    for i in range(3):
        form.textfield("Text Field", colors.white, colors.white, colors.black, x = 150, y = hite-5, width = 180, height = 20, fontSize = 14 )
        hite-=20

def main():
    cover_page()
    c.showPage()
    overview_page()
    c.showPage()
    opponent_offense_page()
    c.showPage()
    opponent_defense_page()
    c.showPage()
    shooting_page()
    c.showPage()
    #for i in range(number_of_players):
        #player_page(fast_scout_box_score, fast_scout_image, shot_quality_player_stats_table, shot_quality_player_stats)
    c.save()

main()