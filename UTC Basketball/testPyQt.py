#PyQt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        #sets title of window at top left of window
        self.setWindowTitle('UTC Basketball')
        #setting geometry
        self.setGeometry(400,400,400,400)
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
        self.team_combo_box.setGeometry(200,150,120,30)
        #list of opposing basketball teams
        team_list = ["Select Team","VMI Keydets","TTU Golden Eagles"]
        #inputs values from team_list as selections in dropdown menu
        self.team_combo_box.addItems(team_list)
        #define run button
        run_button = QPushButton("Run Program", self)
        print(self.team_combo_box.count())
        #adds action to run_button
        run_button.pressed.connect(self.find)
        #create label
        self.label = QLabel(self)
        #setting geometry of label
        self.label.setGeometry(200,200,200,30)

    def find(self):
        #finding current index of team_combo_box
        team_index = self.team_combo_box.currentIndex()
        #showing content on the screen though label
        self.label.setText("Index: "+str(team_index))


#creates the application object (every application needs this)
app = QApplication(sys.argv)
#create application window
window = Window()
#start the app
sys.exit(app.exec_())