from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class addemployee(QWidget):
    def __init__(self):
        super(addemployee, self).__init__()
        self.resize(500,700)
        self.layouts()
        self.setFixedSize(500,700)



    def layouts(self):
        self.vboxx=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.botlayout=QFormLayout()
        #########################################
        self.vboxx.addLayout(self.toplayout,25)
        self.vboxx.addLayout(self.botlayout,75)
        self.setLayout(self.vboxx)
        self.top()
        self.bot()
    def top(self):

        self.icon = QLabel()
        self.icon.setPixmap(QPixmap("icons/user.png"))
        self.icon.setAlignment(Qt.AlignHCenter)
        self.text=QLabel("Add person")
        self.text.setFont(QFont("Times", 25))
        self.toplayout.addWidget(self.text)
        self.toplayout.addWidget(self.icon)
        self.toplayout.setSpacing(15)
        self.toplayout.setAlignment(Qt.AlignHCenter)
    def bot(self):

        self.name = QLabel("Name:")
        self.name.setFont(QFont("Arial",15))
        self.namelinedit= QLineEdit()
        self.namelinedit.setPlaceholderText("Enter your name")
        self.namelinedit.setFont(QFont("Arial",15))
        self.surname = QLabel("Surname:")
        self.surname.setFont(QFont("Arial",15))
        self.surnamelineEdit=QLineEdit()
        self.surnamelineEdit.setPlaceholderText("Enter your surname")
        self.surnamelineEdit.setFont(QFont("Arial",15))
        self.phone = QLabel("Phone:")
        self.phone.setFont(QFont("Arial",15))
        self.phonelineEdit = QLineEdit()
        self.phonelineEdit.setPlaceholderText("Enter your phone number")
        self.phonelineEdit.setFont(QFont("Arial",15))
        self.email = QLabel("Email:")
        self.email.setFont(QFont("Arial",15))
        self.emailineEdit = QLineEdit()
        self.emailineEdit.setFont(QFont("Arial",15))
        self.emailineEdit.setPlaceholderText("Enter your email")
        self.picture = QLabel("Picture:")
        self.picture.setFont(QFont("Arial",15))
        self.picturePushbutton = QPushButton(text='Browse')
        self.picturePushbutton.setFont(QFont("Arial",15))
        self.address=QLabel("Address:")
        self.address.setFont(QFont("Arial",15))
        self.addressText = QTextEdit()
        self.addressText.setFont(QFont("Arial",15))
        self.addpusbutton = QPushButton(text="Add")
        self.addpusbutton.setFont(QFont("Arial",15))
        #######################################################
        self.botlayout.addRow(self.name,self.namelinedit)
        self.botlayout.addRow(self.surname,self.surnamelineEdit)
        self.botlayout.addRow(self.phone,self.phonelineEdit)
        self.botlayout.addRow(self.email,self.emailineEdit)
        self.botlayout.addRow(self.picture,self.picturePushbutton)
        self.botlayout.addRow(self.address,self.addressText)
        self.botlayout.addRow(QLabel(),self.addpusbutton)


























