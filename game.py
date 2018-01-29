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
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen()
        self.initUI()

    def initUI(self):
        
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())