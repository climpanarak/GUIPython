from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(289, 550)
        MainWindow.setMaximumSize(QtCore.QSize(300, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.submit())
        self.submitButton.setGeometry(QtCore.QRect(10, 460, 81, 41))
        self.submitButton.setObjectName("submitButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clearPressed())
        self.clearButton.setGeometry(QtCore.QRect(190, 460, 81, 41))
        self.clearButton.setObjectName("clearButton")
        self.billCalculator = QtWidgets.QLabel(self.centralwidget)
        self.billCalculator.setGeometry(QtCore.QRect(70, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.billCalculator.setFont(font)
        self.billCalculator.setObjectName("billCalculator")
        self.label_Food = QtWidgets.QLabel(self.centralwidget)
        self.label_Food.setGeometry(QtCore.QRect(21, 61, 25, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Food.setFont(font)
        self.label_Food.setObjectName("label_Food")
        self.label_Dessert = QtWidgets.QLabel(self.centralwidget)
        self.label_Dessert.setGeometry(QtCore.QRect(20, 140, 40, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Dessert.setFont(font)
        self.label_Dessert.setObjectName("label_Dessert")
        self.Foodline = QtWidgets.QLineEdit(self.centralwidget)
        self.Foodline.setGeometry(QtCore.QRect(70, 60, 161, 20))
        self.Foodline.setObjectName("Foodline")
        self.Drinkline = QtWidgets.QLineEdit(self.centralwidget)
        self.Drinkline.setGeometry(QtCore.QRect(70, 100, 161, 20))
        self.Drinkline.setObjectName("Drinkline")
        self.Dessertline = QtWidgets.QLineEdit(self.centralwidget)
        self.Dessertline.setGeometry(QtCore.QRect(70, 140, 161, 20))
        self.Dessertline.setObjectName("Dessertline")
        self.OutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.OutputLabel.setGeometry(QtCore.QRect(30, 240, 231, 201))
        self.OutputLabel.setText("")
        self.OutputLabel.setObjectName("OutputLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 180, 170, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TipTen = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TipTen.setFont(font)
        self.TipTen.setObjectName("TipTen")
        self.gridLayout.addWidget(self.TipTen, 0, 1, 1, 1)
        self.Tipfift = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Tipfift.setFont(font)
        self.Tipfift.setObjectName("Tipfift")
        self.gridLayout.addWidget(self.Tipfift, 0, 2, 1, 1)
        self.label_Tip = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tip.setFont(font)
        self.label_Tip.setObjectName("label_Tip")
        self.gridLayout.addWidget(self.label_Tip, 0, 0, 1, 1)
        self.TipTwen = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.TipTwen.setFont(font)
        self.TipTwen.setObjectName("TipTwen")
        self.gridLayout.addWidget(self.TipTwen, 0, 3, 1, 1)
        self.label_Drink = QtWidgets.QLabel(self.centralwidget)
        self.label_Drink.setGeometry(QtCore.QRect(20, 100, 32, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Drink.setFont(font)
        self.label_Drink.setObjectName("label_Drink")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.TipTen.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitButton.setText(_translate("MainWindow", "SUBMIT"))
        self.clearButton.setText(_translate("MainWindow", "CLEAR"))
        self.billCalculator.setText(_translate("MainWindow", "BILL CALCULATOR"))
        self.label_Food.setText(_translate("MainWindow", "Food"))
        self.label_Dessert.setText(_translate("MainWindow", "Dessert"))
        self.TipTen.setText(_translate("MainWindow", "10%"))
        self.Tipfift.setText(_translate("MainWindow", "15%"))
        self.label_Tip.setText(_translate("MainWindow", "Tip"))
        self.TipTwen.setText(_translate("MainWindow", "20%"))
        self.label_Drink.setText(_translate("MainWindow", "Drink"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())