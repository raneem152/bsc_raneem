from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton,QFileDialog,QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUI("image.ui",self)

        self.button = self.findChild(QPushButton,"pushButton")
        self.label= self.findChild(QLabel,"label")
        self.button.clicked.connect(self.clicker)

        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self,"open file","C:\\Users\\7zl2oom\\Desktop\\giu\\gui_images","All files(*.png)")
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
