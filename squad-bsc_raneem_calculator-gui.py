# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(248, 326)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_pm = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.pluse_minus_it())
        self.Button_pm.setGeometry(QtCore.QRect(10, 240, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.Button_pm.setFont(font)
        self.Button_pm.setObjectName("Button_pm")
        self.dec_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.do_it())
        self.dec_Button.setGeometry(QtCore.QRect(130, 240, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.dec_Button.setFont(font)
        self.dec_Button.setObjectName("dec_Button")
        self.equal_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.math_it())
        self.equal_Button.setGeometry(QtCore.QRect(190, 240, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.equal_Button.setFont(font)
        self.equal_Button.setObjectName("equal_Button")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("0"))
        self.Button_0.setGeometry(QtCore.QRect(70, 240, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("2"))
        self.Button_2.setGeometry(QtCore.QRect(70, 190, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("1"))
        self.Button_1.setGeometry(QtCore.QRect(10, 190, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("3"))
        self.Button_3.setGeometry(QtCore.QRect(130, 190, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.plus_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("+"))
        self.plus_Button.setGeometry(QtCore.QRect(190, 190, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.plus_Button.setFont(font)
        self.plus_Button.setObjectName("plus_Button")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("4"))
        self.Button_4.setGeometry(QtCore.QRect(10, 140, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("5"))
        self.Button_5.setGeometry(QtCore.QRect(70, 140, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("6"))
        self.Button_6.setGeometry(QtCore.QRect(130, 140, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.min_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("-"))
        self.min_Button.setGeometry(QtCore.QRect(190, 140, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        self.min_Button.setFont(font)
        self.min_Button.setObjectName("min_Button")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("8"))
        self.Button_8.setGeometry(QtCore.QRect(70, 90, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("7"))
        self.Button_7.setGeometry(QtCore.QRect(10, 90, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("9"))
        self.Button_9.setGeometry(QtCore.QRect(130, 90, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.X_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("*"))
        self.X_Button.setGeometry(QtCore.QRect(190, 90, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.X_Button.setFont(font)
        self.X_Button.setObjectName("X_Button")
        self.mod_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("%"))
        self.mod_button.setGeometry(QtCore.QRect(10, 40, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.mod_button.setFont(font)
        self.mod_button.setObjectName("mod_button")
        self.C_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("c"))
        self.C_Button.setGeometry(QtCore.QRect(70, 40, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.C_Button.setFont(font)
        self.C_Button.setObjectName("C_Button")
        self.b_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.remove_it())
        self.b_button.setGeometry(QtCore.QRect(130, 40, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.b_button.setFont(font)
        self.b_button.setObjectName("b_button")
        self.divide_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda :self.press_it("/"))
        self.divide_Button.setGeometry(QtCore.QRect(190, 40, 45, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.divide_Button.setFont(font)
        self.divide_Button.setObjectName("divide_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 248, 17))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def do_it(self):
        screen = self.label.text()
        if screen[-1]==".":
            pass
        else:
            self.label.setText(f'{screen}.')

    def remove_it(self):
        screen = self.label.text()
        screen = screen[:-1]
        self.label.setText(screen)

    def pluse_minus_it(self):
        screen = self.label.text()
        if "-" in screen:
            self.label.setText(screen.replace("-",""))
        else:
            self.label.setText(f'-{screen}')

    def math_it(self):
        screen = self.label.text()
        try:
            answer = eval(screen)
            self.label.setText(str(answer))
        except:
            self.label.setText("error")


    def press_it(self, pressed):
        if pressed == "c":
            self.label.setText("0")
        else:
            if self.label.text() == "0":
                 self.label.setText("")
            self.label.setText(f'{self.label.text()}{pressed}')

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "calculator"))
        self.Button_pm.setText(_translate("mainWindow", "+/-"))
        self.dec_Button.setText(_translate("mainWindow", "."))
        self.equal_Button.setText(_translate("mainWindow", "="))
        self.Button_0.setText(_translate("mainWindow", "0"))
        self.Button_2.setText(_translate("mainWindow", "2"))
        self.Button_1.setText(_translate("mainWindow", "1"))
        self.Button_3.setText(_translate("mainWindow", "3"))
        self.plus_Button.setText(_translate("mainWindow", "+"))
        self.Button_4.setText(_translate("mainWindow", "4"))
        self.Button_5.setText(_translate("mainWindow", "5"))
        self.Button_6.setText(_translate("mainWindow", "6"))
        self.min_Button.setText(_translate("mainWindow", "-"))
        self.Button_8.setText(_translate("mainWindow", "8"))
        self.Button_7.setText(_translate("mainWindow", "7"))
        self.Button_9.setText(_translate("mainWindow", "9"))
        self.X_Button.setText(_translate("mainWindow", "x"))
        self.mod_button.setText(_translate("mainWindow", "%"))
        self.C_Button.setText(_translate("mainWindow", "c"))
        self.b_button.setText(_translate("mainWindow", "<<"))
        self.divide_Button.setText(_translate("mainWindow", "/"))
        self.label.setText(_translate("mainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

