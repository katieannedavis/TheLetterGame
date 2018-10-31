import sys
from PyQt5.QtWidgets import QApplication
import GameFunctions

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = GameFunctions.GameWindow()
    sys.exit(app.exec_())
