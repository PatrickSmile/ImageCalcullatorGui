# -*- coding: utf-8 -*-
"""
@author: patrick.park@epitone.ai
"""

import sys
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import numpy as np
import cv2 as cv
import time
import qimage2ndarray as q2n

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(BASE_DIR + r"\main.ui")[0]

# main gui window class
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # variables
        self.past_x = None
        self.past_y = None
        self.present_x = None
        self.present_y = None

        # QObjects
        self.pb_OpenImage.clicked.connect(self.pb_OpenImageClicked)


    def pb_OpenImageClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.img = cv.imread(fname[0])
        if self.img.ndim > 2:
            self.img = cv.imread(fname[0], cv.IMREAD_GRAYSCALE)
        self.qimg = q2n.array2qimage(self.img, normalize=False)
        self.pixmap = QPixmap.fromImage(self.qimg)
        self.lbl_Image.setPixmap(self.pixmap)
        self.lbl_Image.setContentsMargins(10, 10, 10, 10)
        self.lbl_Image.resize(self.pixmap.width(), self.pixmap.height())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

print('all done')