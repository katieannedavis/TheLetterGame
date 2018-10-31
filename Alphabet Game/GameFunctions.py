from GameBoard import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
import pygame


class GameWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.initUI()
        self.intro()

    def initUI(self):
        ExitGame = QAction(QIcon("exit.png"), "&Exit", self)
        ExitGame.setStatusTip("Quit game")
        ExitGame.triggered.connect(self.exit_clicked)

        menubar = self.menuBar()
        menubar.addAction(ExitGame)

    def exit_clicked(self):
        say = "Goodbye"
        Speech.__init__(say)
        quit()

    def intro(self):
        pygame.mixer.init(frequency=200000, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.load('letters/hello.mp3')
        pygame.mixer.music.play(0)

    def keyPressEvent(self, e):
        font_size = "300px"
        if e.key() == Qt.Key_A:
            letter = "A"
            font_color = "rgb(68, 252, 218)"
            back_color = "rgb(244, 65, 143)"

        elif e.key() == Qt.Key_B:
            letter = "B"
            font_color = "rgb(204, 26, 26)"
            back_color = "rgb(33, 99, 18)"
        elif e.key() == Qt.Key_C:
            letter = "C"
            font_color = "rgb(114, 19, 70)"
            back_color = "rgb(132, 178, 186)"
        elif e.key() == Qt.Key_D:
            letter = "D"
            font_color = "rgb(149, 168, 173)"
            back_color = "rgb(255, 157, 0)"
        elif e.key() == Qt.Key_E:
            letter = "E"
            font_color = "rgb(40, 31, 73)"
            back_color = "rgb(255, 119, 119)"
        elif e.key() == Qt.Key_F:
            letter = "F"
            font_color = "rgb(255, 255, 255)"
            back_color = "rgb(54, 132, 49)"
        elif e.key() == Qt.Key_G:
            letter = "G"
            font_color = "rgb(255, 51, 51)"
            back_color = "rgb(255, 255, 57)"
        elif e.key() == Qt.Key_H:
            letter = "H"
            font_color = "rgb(217, 217, 217)"
            back_color = "rgb(51, 51, 255)"
        elif e.key() == Qt.Key_I:
            letter = "I"
            font_color = "rgb(153, 102, 51)"
            back_color = "rgb(77, 255, 77)"
        elif e.key() == Qt.Key_J:
            letter = "J"
            font_color = "rgb(255, 255, 57)"
            back_color = "rgb(51, 51, 255)"
        elif e.key() == Qt.Key_K:
            letter = "K"
            font_color = "rgb(255, 255, 255)"
            back_color = "rgb(153, 102, 51)"
        elif e.key() == Qt.Key_L:
            letter = "L"
            font_color = "rgb(255, 80, 80)"
            back_color = "rgb(77, 255, 77)"
        elif e.key() == Qt.Key_M:
            letter = "M"
            font_color = "rgb(0, 0, 0)"
            back_color = "rgb(255, 51, 51)"
        elif e.key() == Qt.Key_N:
            letter = "N"
            font_color = "rgb(51, 51, 255)"
            back_color = "rgb(153, 102, 51)"
        elif e.key() == Qt.Key_O:
            letter = "O"
            font_color = "rgb(255, 80, 80)"
            back_color = "rgb(0, 0, 77)"
        elif e.key() == Qt.Key_P:
            letter = "P"
            font_color = "rgb(217, 217, 217)"
            back_color = "rgb(51, 51, 255)"
        elif e.key() == Qt.Key_Q:
            letter = "Q"
            font_color = "rgb(255, 51, 51)"
            back_color = "rgb(0, 0, 0)"
        elif e.key() == Qt.Key_R:
            letter = "R"
            font_color = "rgb(255, 0, 0)"
            back_color = "rgb(0, 0, 153)"
        elif e.key() == Qt.Key_S:
            letter = "S"
            font_color = "rgb(51, 51, 255)"
            back_color = "rgb(217, 217, 217)"
        elif e.key() == Qt.Key_T:
            letter = "T"
            font_color = "rgb(0, 0, 0)"
            back_color = "rgb(112, 194, 133)"
        elif e.key() == Qt.Key_U:
            letter = "U"
            font_color = "rgb(77, 255, 77)"
            back_color = "rgb(0, 0, 153)"
        elif e.key() == Qt.Key_V:
            letter = "V"
            font_color = "rgb(153, 102, 51)"
            back_color = "rgb(255, 255, 255)"
        elif e.key() == Qt.Key_W:
            letter = "W"
            font_color = "#F0FFFF"
            back_color = "#228B22"
        elif e.key() == Qt.Key_X:
            letter = "X"
            font_color = "rgb(217, 217, 217)"
            back_color = "rgb(51, 51, 255)"
        elif e.key() == Qt.Key_Y:
            letter = "Y"
            font_color = "rgb(255, 255, 57)"
            back_color = "rgb(0, 0, 0)"
        elif e.key() == Qt.Key_Z:
            letter = "Z"
            font_color = "rgb(112, 194, 133)"
            back_color = "rgb(217, 217, 217)"
        elif e.key() == Qt.Key_Escape:
            letter = "Goodbye"
            quit()
        else:
            letter = "Not a letter."
            font_color = "black"
            font_size = "100px"
            back_color = "white"
        self.screen(letter, font_color, back_color, font_size)
        Speech.__init__(letter)

    def screen(self, text, font, back, size):
        self.Letter_Label.setText(text)
        self.setStyleSheet("""
            QMainWindow {
                background-color: """ + back + """;
            }
            QLabel {
                color: """ + font + """;
                font-size: """ + size + """;
            }
            """)


class Speech:
    def __init__(text):
        if text == 'Goodbye':
            pygame.mixer.music.load('letters/goodbye.mp3')
        elif text == 'Not a letter.':
            pygame.mixer.music.load('letters/NotALetter.mp3')
        else:
            pygame.mixer.music.load('letters/'+text+'.mp3')
        pygame.mixer.music.play(0)
