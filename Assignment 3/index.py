from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pymysql as MySQLdb
from PyQt5.uic import loadUiType
import cryptography

ui, _ = loadUiType('design.ui')
# login, _ = loadUiType('login.ui')
#
# class Login(QWidget, login):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setupUi(self)

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Record)

    ################################################
    ######### Record Management #########################

    def Record(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='d33ps3curity', db='foundation_day_management')
        self.cur = self.db.cursor()
        performance_no = self.lineEdit_6.text()
        performance_type = self.comboBox.currentText()
        batch_year = self.comboBox_2.currentText()
        no_of_member = self.lineEdit_3.text()
        judges_marks = self.lineEdit_4.text()
        self.cur.execute('''
         INSERT INTO performance_records (performance_no, performance_type, no_of_member, batch_year, marks_by_judges)
         VALUES (%s, %s, %s, %s, %s)
         ''',(performance_no, performance_type, no_of_member, batch_year, judges_marks))
        self.db.commit()
        self.statusBar().showMessage('New Record Added')
        self.db.close()

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

