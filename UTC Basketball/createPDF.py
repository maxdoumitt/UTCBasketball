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

#filename = teamSearches.selected_teams_dictionary_names[0]+" Document"
filename = "team_name Document.pdf" #Input Opponent Team Name
#opponent_name = teamSearches.selected_teams_dictionary_names[0]
offense_items = [
    "Depth:",
    "Play Style:",
    "Pace:",
    "Efficiency:",
    "Shot Making:",
    "Shot Volume:",
    "Shot Selection:"
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
    c.drawCentredString(300, 685, "VMI") 
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(300, 650, "Game #") #Input Game Number
    c.drawCentredString(300, 610, "Date") #Input Game Date
    #input UTC Image
    c.drawInlineImage("UTC Basketball\img\Chattanooga.png", 200, 385, 200, 200)
    #Write Vs
    c.drawCentredString(300, 360, "vs")
    #input Opponent Image
    c.drawInlineImage("UTC Basketball\img\general_team_data\VMI_logo_image.png", 200, 135, 200, 200)
    

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
    c.drawInlineImage("UTC Basketball\img\general_team_data\shot_quality_VMI_stats.png", 110, 420, 370, 150)
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
    c.drawCentredString(300, 770, "VMI Offense") #Input Enemy Team Name
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


def main():
    cover_page()
    c.showPage()
    overview_page()
    c.showPage()
    opponent_offense_page()
    c.save()

main()