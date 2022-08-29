

from PyQt5 import QtCore, QtGui, QtWidgets
from sad import*

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(652, 579)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 651, 581))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.img_lbl = QtWidgets.QLabel(Form)
        self.img_lbl.setGeometry(QtCore.QRect(30, 40, 571, 381))
        self.img_lbl.setStyleSheet("image: url(:/img/img.jpg);")
        self.img_lbl.setText("")
        self.img_lbl.setObjectName("img_lbl")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 510, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);\n""border:none;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 510, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(0, 255, 0);\n""border:none;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 510, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(0, 0, 255);\n""border:none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 510, 113, 20))
        self.lineEdit_4.setStyleSheet("border:none;\n""background-color: rgb(200, 200, 200);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(510, 510, 111, 23))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.img_lbl_2 = QtWidgets.QLabel(Form)
        self.img_lbl_2.setGeometry(QtCore.QRect(10, 40, 611, 371))
        self.img_lbl_2.setStyleSheet("background-color: rgb(0, 0, 200,100);")
        self.img_lbl_2.setText("")
        self.img_lbl_2.setObjectName("img_lbl_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.tikla)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Red  (0-255)"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", " Green (0-255)"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", " Blue (0-255)"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", " Transparant (0-255"))
        self.pushButton.setText(_translate("Form", "Ekle"))

    def tikla(self, ekle):
       Red_value = self.lineEdit.text()
       Green_value = self.lineEdit_2.text()
       Blue_value = self.lineEdit_3.text()
       Transparant_value = self.lineEdit_4.text()
       edit = "background-color:rgb("+Red_value+","+Green_value+" ,"+Blue_value+","+Transparant_value+")"
       self.img_lbl_2.setStyleSheet(edit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())