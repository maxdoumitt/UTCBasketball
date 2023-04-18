#PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


team_list = [
    "Select Team",
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

class Window(QMainWindow):

    

    def __init__(self):
        super().__init__()
        #sets title of window at top left of window
        self.setWindowTitle('UTC Basketball')
        #setting geometry
        self.setGeometry(400, 600, 600, 400)
        self.setFixedSize(600, 400)
        # set app icon    
        self.setWindowIcon(QtGui.QIcon("UTC Basketball\\boiler_plates\\Chattanooga.png"))
        tray_icon = QSystemTrayIcon(QtGui.QIcon("UTC Basketball\\boiler_plates\\Chattanooga.png"), parent=self)
        tray_icon.setToolTip("UTC Men's Basketball")
        tray_icon.show()
        #sets the location of the window when its opened
        self.move(300,300)
        #calling method
        self.UiComponents()
        #showing all widgets
        self.show()

    def UiComponents(self): 
        #creating a combo box widget to select a team
        self.team_combo_box = QComboBox(self)
        #setting ComboBox geometry
        self.team_combo_box.setGeometry(210,150,200,50)
        #list of opposing basketball teams
        #inputs values from team_list as selections in dropdown menu
        self.team_combo_box.addItems(team_list)
        #define run button
        run_button = QPushButton("Run Program", self)
        run_button.setGeometry(260, 250, 100, 30)
        print(self.team_combo_box.count())
        #adds action to run_button
        run_button.pressed.connect(self.find)
        #create label
        self.label = QLabel(self)
        #setting geometry of label
        self.label.setGeometry(245,200,200,30)


    def find(self):
        #finding current index of team_combo_box
        team_index = self.team_combo_box.currentIndex()
        if team_index == 0:
            self.label.setText("Please Select a Team")
        else:
            #showing content on the screen though label
            self.label.setText("Index: "+str(team_index))
            #sets chosen team as the target team
            from scrapeData import main , test_pdf
            #main(team_list[team_index])
            #for testing pdf changes
            test_pdf(team_list[team_index])
            #closes window when run button is clicked
            self.close()


#creates the application object (every application needs this)
app = QApplication(sys.argv)
#create application window
window = Window()
#start the app
sys.exit(app.exec_())