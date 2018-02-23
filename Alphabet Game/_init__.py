#! /usr/bin/env python3
# -*- coding:utf-8 -*-
#####################################################################

# katieannedavis                            MIT-license

# Title: The Alphabet Game                  Version: 1.0
# Date: 1/28/2018                           Language: python3
#
# Description: A child's keyboard game where if a letter
# is pressed the letter is sounded out and a picture of the
# letter is shown.
######################################################################

import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gtts import gTTS
from playsound import playsound
import tkinter


# Game introduction card
class TitleCard(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'The Letter Game'
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.left = width/3.5
        self.top = height/5
        self.width = 500
        self.height = 500
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)

        pixmap = QImage('ABC Sloth.jpg')
        self.resize(pixmap.width(),pixmap.height())
        palette = QPalette()
        palette.setBrush(10, QBrush(pixmap))
        self.setPalette(palette)

        btn = QPushButton('The Letter Game \n Press to Play', self)
        btn.clicked.connect(self.playInstructions)
        btn.clicked.connect(self.close)

        #btn.resize(btn.sizeHint())
        btn.move(20,400)

        self.setStyleSheet("""
                    QPushButton {
                        background-color: #008CBA;
                        border: 2px solid #A0522D;
                        border-radius: 8px;
                        color: white;
                        font-size: 24px;
                        padding: 12px 28px;
                    }
                    """)

        self.show()



    def playInstructions(self):
        playsound("instructions.mp3")


# Get child's name and say hello
# Input window for text to be sent to Gtts to make into .mp3 then played upon
# okay button press.
class HelloChild(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window)
        self.title = "What's Your Name"
        self.setWindowIcon(QIcon('letter_game_icon.png'))
        root = tkinter.Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.left = width / 3.5
        self.top = height / 5
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getText()
        self.show()


    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Welcome", "What is your name?", QLineEdit.Normal, "")
        self.setStyleSheet("""
            QInputDialog {
                background-color: #008CBA;
                border: 2px solid #A0522D;
                border-radius: 8px;
                color: black;
                font-size: 24px;
                padding: 12px 28px;
                }
                    """)
        if okPressed and text != '':
            tts = gTTS(text="Hello "+ text + ", Would you like to play a game?", lang='en-us')
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove("hello.mp3")
        else:
            tts = gTTS(text="Hello You-Who-Must-Remain-UnNamed, Would you like to play a game?", lang='en-us')
            tts.save("hello.mp3")
            playsound("hello.mp3")
            os.remove("hello.mp3")


# Main Window
class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        self.initUI()

    def initUI(self):
        mainMenu = self.menuBar()
        exitButton = QAction(QIcon('exit.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        mainMenu.addAction(exitButton)
        self.show()

        self.ui = HelloChild()
        self.ui.show()

        self.ui = TitleCard()
        self.ui.show()



    def keyPressEvent(self, event):
        letter = event.key()
        if letter == Qt.Key_A:
            playsound("sound/a.mp3")
            choice = "A"
            # colors background: black font: white
            textColor = "#FFFFFF"
            textBackground = "#000000"
        if letter == Qt.Key_B:
            playsound("sound/b.mp3")
            choice = "B"
            # colors background: navy font: gold
            textColor = "#FFD700"
            textBackground = "#000080"
        if letter == Qt.Key_C:
            playsound("sound/c.mp3")
            choice = "C"
            # colors background: dark green font: yellow
            textColor = "#FFFF00"
            textBackground = "#4B0082"
        if letter == Qt.Key_D:
            playsound("sound/d.mp3")
            choice = "D"
            # colors background: orange red font: light cyan
            textColor = "#E0FFFF"
            textBackground = "#FF4500"
        if letter == Qt.Key_E:
            playsound("sound/e.mp3")
            choice = "E"
            # colors background: orange red font: light cyan
            textColor = "#000000"
            textBackground = "#FFEBCD"
        if letter == Qt.Key_F:
            playsound("sound/f.mp3")
            choice = "F"
            # colors background: indigo font: thistle
            textColor = "#D8BFD8"
            textBackground = "#4B0082"
        if letter == Qt.Key_G:
            playsound("sound/g.mp3")
            choice = "G"
            # colors background: lemon chiffon font: deep pink
            textColor = "#FFFACD"
            textBackground = "#BC8F8F"
        if letter == Qt.Key_H:
            playsound("sound/h.mp3")
            choice = "H"
            # colors background: saddle brown font: light yellow
            textColor = "#FFFFE0"
            textBackground = "#708090"
        if letter == Qt.Key_I:
            playsound("sound/i.mp3")
            choice = "I"
            # colors background: fuchsia font: navy
            textColor = "#ADD8E6"
            textBackground = "#FF00FF"
        if letter == Qt.Key_J:
            playsound("sound/j.mp3")
            choice = "J"
            # colors background: yellow font: teal
            textColor = "#008080"
            textBackground = "#FFFF00"
        if letter == Qt.Key_K:
            playsound("sound/k.mp3")
            choice = "K"
            # colors background: fuchsia font: maroon
            textColor = "#800000"
            textBackground = "#FF00FF"
        if letter == Qt.Key_L:
            playsound("sound/l.mp3")
            choice = "L"
            # colors background: red font: midnight blue
            textColor = "#191970"
            textBackground = "#FF0000"
        if letter == Qt.Key_M:
            playsound("sound/m.mp3")
            choice = "M"
            # colors background: salmon font: dark green
            textColor = "#006400"
            textBackground = "#FA8072"
        if letter == Qt.Key_N:
            playsound("sound/n.mp3")
            choice = "N"
            # colors background: dark slate gray font: lime
            textColor = "#00FF00"
            textBackground = "#2F4F4F"
        if letter == Qt.Key_O:
            playsound("sound/o.mp3")
            choice = "O"
            # colors background: light cyan font: chocolate
            textColor = "#D2691E"
            textBackground = "#E0FFFF"
        if letter == Qt.Key_P:
            playsound("sound/p.mp3")
            choice = "P"
            # colors background: rosy brown font: indigo
            textColor = "#4B0082"
            textBackground = "#BC8F8F"
        if letter == Qt.Key_Q:
            playsound("sound/q.mp3")
            choice = "Q"
            # colors background: dark magenta font: pale golden rod
            textColor = "#EEE8AA"
            textBackground = "#8B008B"
        if letter == Qt.Key_R:
            playsound("sound/r.mp3")
            choice = "R"
            # colors background: silver font: orange red
            textColor = "#FF4500"
            textBackground = "#C0C0C0"
        if letter == Qt.Key_S:
            playsound("sound/s.mp3")
            choice = "S"
            # colors background: yellow font: teal
            textColor = "#008080"
            textBackground = "#FFFF00"
        if letter == Qt.Key_T:
            playsound("sound/t.mp3")
            choice = "T"
            # colors background: powder blue font: red
            textColor = "#FF000"
            textBackground = "#B0E0E6"
        if letter == Qt.Key_U:
            playsound("sound/u.mp3")
            choice = "U"
            # colors background: dodger blue font: deep pink
            textColor = "#FF1493"
            textBackground = "#1E90FF"
        if letter == Qt.Key_V:
            playsound("sound/v.mp3")
            choice = "V"
            # colors background: antique white font: black
            textColor = "#000000"
            textBackground = "#FAEBD7"
        if letter == Qt.Key_W:
            playsound("sound/w.mp3")
            choice = "W"
            # colors background: forest green font: azure
            textColor = "#F0FFFF"
            textBackground = "#228B22"
        if letter == Qt.Key_X:
            playsound("sound/x.mp3")
            choice = "X"
            # colors background: dark red font: chart refuse
            textColor = "#7FFF00"
            textBackground = "#8B0000"
        if letter == Qt.Key_Y:
            playsound("sound/y.mp3")
            choice = "Y"
            # colors background: orange red font: light sea green
            textColor = "#20B2AA"
            textBackground = "#FFA07A"
        if letter == Qt.Key_Z:
            playsound("sound/z.mp3")
            choice = "Z"
            # colors background: indigo font: wheat
            textColor = "#008080"
            textBackground = "#4B0082"
        if letter == Qt.Key_Escape:
            self.close()
        displayLetter = QLabel(choice)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        displayLetter.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(displayLetter, 0, 0)
        self.setStyleSheet("""
            QMainWindow {
                background-color: """+textBackground+""";
            }
            QLabel {
                color: """ +textColor+ """;
                font-size: 400px;
                font-family: "OCR A Std", monospace;
                font-weight: 800px;
            }
            """)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = GameBoard()

    sys.exit(app.exec_())