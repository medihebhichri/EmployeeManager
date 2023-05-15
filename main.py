import os.path
import sqlite3

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import addemployee
from  PIL import Image
defaultimage="user.png"
con = sqlite3.connect('employees.db')
cur=con.cursor()
class window(QWidget):
    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(300,100,1000,800)
        ##################################################
        ############### QLAYOUT HORIZONTAL   #############
        Hbox = QHBoxLayout()
        self.setLayout(Hbox)
        ##########################################################################
        ############### two layouts (1-form layout 2-vbox) #############
        self.formlayout=QFormLayout()
        vbox=QVBoxLayout()


        ##########################################################################
        ############## pushbutton box ###########################################
        Pushbox=QHBoxLayout()
        self.add=QPushButton(text="Add")
        self.delete=QPushButton(text="delete")
        self.update=QPushButton(text="update")
        Pushbox.addWidget(self.add,25)
        Pushbox.addWidget(self.delete,25)
        Pushbox.addWidget(self.update,25)
        ########################################################################
        #################add icon and table ################################
        self.label=QLabel()
        self.label.setPixmap(QPixmap("icons/user.png"))
        self.label.setAlignment(Qt.AlignHCenter)
        self.viconandtable=QVBoxLayout()
        self.viconandtable.addWidget(self.label,30)
        self.viconandtable.addLayout(self.formlayout,70)

        Hbox.addLayout(self.viconandtable,40)
        Hbox.addLayout(vbox, 60)

        #########################################################################
        ############### Qtable widget #########################################
        self.tablewidget = QListWidget()
        self.tablewidget.setFont(QFont("Arial",15))


        ########################################################################
        #######################################################################
        vbox.addWidget(self.tablewidget)
        vbox.addLayout(Pushbox)
        #####################################################################
        ##################### form layout ##################################

        name=QLabel(text="Name:")
        name.setFont(QFont("Times",15))
        Surname = QLabel(text="Surname:")
        Surname.setFont(QFont("Times",15))
        phone = QLabel(text="Phone:")
        phone.setFont(QFont("Times",15))
        Email = QLabel(text="Email:")
        Email.setFont(QFont("Times",15))
        Address = QLabel(text="Address:")
        Address.setFont(QFont("Times",15))
        self.emplo=addemployee.addemployee()
        #################################################
        self.emplo.picturePushbutton.clicked.connect(self.uploadImage)
        self.emplo.addpusbutton.clicked.connect(self.addEmployee)
        self.add.clicked.connect(self.showwidget)
        self.getemployees()
        self.DisplayfirstRecord()
        self.tablewidget.itemClicked.connect(self.singleclick)
        self.delete.clicked.connect(self.deleteEmployee)
    def getemployees(self):
        query="SELECT id,name,surname FROM employees"
        employees =cur.execute(query).fetchall()
        for employee in employees:
            self.tablewidget.addItem(str(employee[0]+1)+"-"+employee[1]+" "+employee[2])
    def DisplayfirstRecord(self):
        query="SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee =cur.execute(query).fetchone()
        print(employee)
        img = QLabel()
        name=QLabel(employee[1])
        name.setFont(QFont("Arial",15))
        surname = QLabel(employee[2])
        surname.setFont(QFont("Arial",15))
        phone = QLabel(employee[3])
        phone.setFont(QFont("Arial",15))
        email = QLabel(employee[4])
        email.setFont(QFont("Arial",15))
        address=QLabel(employee[6])
        address.setFont(QFont("Arial",15))
        nametitle=QLabel("name:")
        nametitle.setFont(QFont("Arial",17))
        surnametitle=QLabel("surname:")
        surnametitle.setFont(QFont("Arial",17))
        phonetitle=QLabel("phone:")
        phonetitle.setFont(QFont("Arial",17))
        emailtitle=QLabel("email:")
        emailtitle.setFont(QFont("Arial",17))
        addresstile=QLabel("address:")
        addresstile.setFont(QFont("Arial",17))
        self.label.setPixmap(QPixmap("images/"+employee[5]))
        self.formlayout.addRow(nametitle,name)
        self.formlayout.addRow(surnametitle,surname)
        self.formlayout.addRow(phonetitle, phone)
        self.formlayout.addRow(emailtitle,email)
        self.formlayout.addRow(addresstile,address)
        self.formlayout.setSpacing(30)


    def singleclick(self):
        for i in reversed(range(self.formlayout.count())):
            widget=self.formlayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()




        employee=self.tablewidget.currentItem().text()
        id=employee.split("-")[0]
        id=int(id)
        id=id-1
        id=str(id)

        query="SELECT * FROM employees WHERE ID=?"
        employee=cur.execute(query,(id,)).fetchone()


        name = QLabel(employee[1])
        name.setFont(QFont("Arial", 15))
        surname = QLabel(employee[2])
        surname.setFont(QFont("Arial", 15))
        phone = QLabel(employee[3])
        phone.setFont(QFont("Arial", 15))
        email = QLabel(employee[4])
        email.setFont(QFont("Arial", 15))
        address = QLabel(employee[6])
        address.setFont(QFont("Arial", 15))
        nametitle = QLabel("name:")
        nametitle.setFont(QFont("Arial", 17))
        surnametitle = QLabel("surname:")
        surnametitle.setFont(QFont("Arial", 17))
        phonetitle = QLabel("phone:")
        phonetitle.setFont(QFont("Arial", 17))
        emailtitle = QLabel("email:")
        emailtitle.setFont(QFont("Arial", 17))
        addresstile = QLabel("address:")
        addresstile.setFont(QFont("Arial", 17))
        self.label.setPixmap(QPixmap("images/" + employee[5]))
        self.formlayout.addRow(nametitle, name)
        self.formlayout.addRow(surnametitle, surname)
        self.formlayout.addRow(phonetitle, phone)
        self.formlayout.addRow(emailtitle, email)
        self.formlayout.addRow(addresstile, address)
        self.formlayout.setSpacing(30)

    def  showwidget(self):
        self.emplo.show()
        self.close()
    def uploadImage(self):
        global defaultimage
        size=(128,128)
        self.filename,ok = QFileDialog.getOpenFileName(self,'upload Image','','Image Files (*.png *.jpg)' )
        print(self.filename)
        if ok:
            defaultimage = os.path.basename(self.filename)

            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("images/{}".format(defaultimage))
    def addEmployee(self):
        name=self.emplo.namelinedit.text()
        surname= self.emplo.surnamelineEdit.text()
        phone=self.emplo.phonelineEdit.text()
        email=self.emplo.emailineEdit.text()
        img=defaultimage
        address=self.emplo.addressText.toPlainText()
        print(img)
        print(name)
        print(img)
        print(phone)
        print(email)

        if (name and surname and phone !=""):
            try:
                query="INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information(self,"success","Person has been added")
                self.emplo.close()
                self.main = window()
                self.main.show()

            except:
                QMessageBox.information(self,"warning","Person has not been added!")

        else:
            QMessageBox.information(self, "warning", "Fields can not be empty!")
    def deleteEmployee(self):

        person=self.tablewidget.currentItem().text()
        print(person)

        id = person.split("-")[0]
        id = int(id)
        id = id - 1
        id = str(id)
        mbox=QMessageBox.question(self,"warning","Are you sure you want to delete this person?",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if mbox == QMessageBox.Yes:
            try:
                query="DELETE FROM employees WHERE id=?"
                cur.execute(query,(id,))
                con.commit()
                self.close()
                self.main=window()
                self.main.show()
            except:
                QMessageBox.information(self,"Warning!!!","Person has not been deleted")





















app = QApplication(sys.argv)
win =  window()
win.show()
sys.exit(app.exec_())