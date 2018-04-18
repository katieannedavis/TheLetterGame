import sys
from PyQt5.QtWidgets import QApplication
import GameFunctions

app = QApplication(sys.argv)

game = GameFunctions.GameWindow()

sys.exit(app.exec_())