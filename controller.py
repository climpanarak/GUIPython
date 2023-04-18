from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.submitButton.clicked.connect(lambda: self.submit())

    def clearPressed(self):
        sender = self.sender()
        if sender == self.clearButton:
            self.Foodline.setText('')
            self.Drinkline.setText('')
            self.Dessertline.setText('')
            self.OutputLabel.setText('')
            self.TipTen.setChecked(True)
        else:
            error_message = "Food, drink and dessert\nneed to be numeric e.g. 10.25\nnot $10.25"
            self.OutputLabel.setText(error_message)
            self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)

    def submit(self):
        food = self.Foodline.text()
        drink = self.Drinkline.text()
        dessert = self.Dessertline.text()

        if food == '' and drink == '' and dessert == '':
            error_message = "Food, drink and dessert\nneed to be numeric e.g. 10.25\nnot $10.25"
            self.OutputLabel.setText(error_message)
            self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
            return

        if food == '':
            food = '0'
        if drink == '':
            drink = '0'
        if dessert == '':
            dessert = '0'

        try:
            food = float(food)
            drink = float(drink)
            dessert = float(dessert)

            subtotal = food + drink + dessert
            tax = subtotal * 0.1
            if self.TipTen.isChecked():
                tip = (subtotal + tax) * 0.1
            if self.Tipfift.isChecked():
                tip = (subtotal + tax) * 0.15
            if self.TipTwen.isChecked():
                tip = (subtotal + tax) * 0.20
            total = subtotal + tax + tip

            summary_text = "<center><b>SUMMARY</b></center>\n\n"
            summary_text += f"<pre>Food:      ${food:.2f}\nDrink:     ${drink:.2f}\nDessert:   ${dessert:.2f}\n\nTax:       ${tax:.2f}\nTip:       ${tip:.2f}\n\nTOTAL:     ${total:.2f}</pre>"

            self.OutputLabel.setText(summary_text)
            self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        except ValueError:
            error_message = "Food, drink and dessert\nneed to be numeric e.g. 10.25\nnot $10.25"
            self.OutputLabel.setText(error_message)
            self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
