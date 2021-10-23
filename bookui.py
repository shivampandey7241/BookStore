from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.l1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)
        self.ln1 = QtWidgets.QLineEdit(Form)
        self.ln1.setObjectName("ln1")
        self.gridLayout.addWidget(self.ln1, 0, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")

        self.btn1.clicked.connect(self.findprice)

        self.gridLayout.addWidget(self.btn1, 0, 2, 1, 1)
        self.l2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 1, 0, 1, 1)
        self.ln2 = QtWidgets.QLineEdit(Form)
        self.ln2.setObjectName("ln2")
        self.gridLayout.addWidget(self.ln2, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.l3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 3, 0, 1, 1)
        self.ln3 = QtWidgets.QLineEdit(Form)
        self.ln3.setObjectName("ln3")
        self.gridLayout.addWidget(self.ln3, 3, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")

        self.btn2.clicked.connect(self.findtotal)

        self.gridLayout.addWidget(self.btn2, 3, 2, 1, 1)
        self.l4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.gridLayout.addWidget(self.l4, 4, 0, 1, 1)
        self.ln4 = QtWidgets.QLineEdit(Form)
        self.ln4.setObjectName("ln4")
        self.gridLayout.addWidget(self.ln4, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l1.setText(_translate("Form", "Book Title :"))
        self.btn1.setText(_translate("Form", "FIND PRICE"))
        self.l2.setText(_translate("Form", "Price :"))
        self.l3.setText(_translate("Form", "Quantity :"))
        self.btn2.setText(_translate("Form", "FIND TOTAL"))
        self.l4.setText(_translate("Form", "Total :"))



    def findprice(self):
        import sqlite3
        db=sqlite3.connect("booksui.db")
        cur=db.cursor()
        ttl=self.ln1.text()

        sql="SELECT * FROM bone WHERE title='"+ttl+"'"
        cur=db.cursor()
        cur.execute(sql)
        rec=cur.fetchone()
        if rec!=None:
            print (rec)
            self.pr=rec[3]
            self.ln2.setText(str(self.pr))
        else:
            print ("Title Not Found")
    def findtotal(self):
        self.qty=float(self.ln3.text())
        ttl=self.pr*self.qty
        self.ln4.setText(str(ttl))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
