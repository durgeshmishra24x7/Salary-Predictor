
# UI_MAIN.PY
################################################################################
# Auther : Durgesh Mishra
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from functools import partial
import sys
from time import strftime
from PyQt5.QtCore import QTimer, QTime

import pandas as pd
from sklearn import linear_model
from word2number import w2n
import math
from num2words import num2words

class Ui_MainWindow(object):

    def __init__(self):
        print("SALARY PREDICTOR WELCOMES YOU")


    # +++++++++++++++++++++++++++++
    def read_excel(self):
        self.path = r"D:\Kaggle_Dataset\HR_dataset_test.csv"
        self.df = pd.read_csv(self.path)
        self.df["Experience"] = self.df["Experience"].fillna("zero")
        self.df.Experience = self.df.Experience.apply(w2n.word_to_num)
        self.median_test_score = math.floor(self.df['Test_score(Out of 10)'].mean())
        self.df['Test_score(Out of 10)'] = self.df['Test_score(Out of 10)'].fillna(self.median_test_score)

    def model_creation(self):
        self.model = linear_model.LinearRegression()
        self.model.fit(self.df[['Experience', 'Test_score(Out of 10)', 'Interview_Score(out of 10)']],
                       self.df['Salary(Rs)'])

        # model_prediction
        self.result=self.model.predict([[int(self.user_input['Employee_exp']),
                                   int(self.user_input['Employee_test_score']),
                                   int(self.user_input['Employee_Interview_scroe'])]])

        self.result_in_word=num2words(int(self.result),lang='en')

        # print(self.model.predict([[int(self.user_input['Employee_exp']),
        #                            int(self.user_input['Employee_test_score']),
        #                            int(self.user_input['Employee_Interview_scroe'])]]))

    # ++++++++++++++++++++++++++++++++++

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.setStyleSheet("background-color: rgb(56, 58, 89);")

        MainWindow.resize(1400, 700)
        self.centralwidget = QWidget(MainWindow)

        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget.setStyleSheet(u"QFrame {	\n"
                                           "background-color: rgb(56, 58, 89);	\n"
                                           "color: rgb(220, 220, 220);\n"
                                           "border-radius: 0px;\n"
                                           "}")

        # rgb(56, 58, 89)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #LOGO
        icon_path=r"D:\GUI's\ML\crystal-ball.png"
        MainWindow.setWindowIcon(QIcon(icon_path))


        title_font = QFont()
        title_font.setFamily(u"Constantia")
        title_font.setPointSize(25)


        # Title
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(title_font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.label_title.setGeometry(QRect(50, 50, 661, 61))
        self.label_title.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_title.move(50, 25)

        # self.verticalLayout.addWidget(self.label_title)
        # self.verticalLayout.setContentsMargins(0, 10, 10, 10)

        font = QFont()
        font.setFamily(u"Constantia")
        font.setPointSize(15)

        self.entry_box_list=[]

        #Employee Name
        self.label1=QLabel(self.centralwidget)
        self.label1.setObjectName(u"label_title")
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setGeometry(QRect(50, 100, 661, 61))
        self.label1.setStyleSheet(u"color: rgb(244,103,68);") #(98, 114, 164)
        self.label1.move(50,90)
        # self.verticalLayout.addWidget(self.label1)

        self.label1_entry_box=QLineEdit(self.centralwidget)
        self.label1_entry_box.setAlignment(Qt.AlignCenter)
        self.label1_entry_box.setGeometry(QRect(50, 50, 200, 40))
        self.label1_entry_box.setStyleSheet(u"color: rgb(255,230,0);")
        self.label1_entry_box.move(280,160)
        self.entry_box_list.append(self.label1_entry_box)

        #Employee Experience
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label_title")
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setGeometry(QRect(50, 150, 661, 61))
        self.label2.setStyleSheet(u"color: rgb(244,103,68);")  # (98, 114, 164)
        self.label2.move(50,210)
        # self.verticalLayout.addWidget(self.label2)

        self.label2_entry_box=QLineEdit(self.centralwidget)
        self.label2_entry_box.setAlignment(Qt.AlignCenter)
        self.label2_entry_box.setGeometry(QRect(50, 50, 200, 40))
        self.label2_entry_box.setStyleSheet(u"color: rgb(255,230,0);")
        self.label2_entry_box.move(280,280)
        self.entry_box_list.append(self.label2_entry_box)

        #Employee Test Score(Out of 10)
        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label_title")
        self.label3.setFont(font)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setGeometry(QRect(50, 200, 661, 61))
        self.label3.setStyleSheet(u"color: rgb(244,103,68);")  # (98, 114, 164)
        self.label3.move(50,330)
        # self.verticalLayout.addWidget(self.label3)

        self.label3_entry_box=QLineEdit(self.centralwidget)
        self.label3_entry_box.setAlignment(Qt.AlignCenter)
        self.label3_entry_box.setGeometry(QRect(50, 50, 200, 40))
        self.label3_entry_box.setStyleSheet(u"color: rgb(255,230,0);")
        self.label3_entry_box.move(280,400)
        self.entry_box_list.append(self.label3_entry_box)

        #Employee_Interview_Score
        self.label4 = QLabel(self.centralwidget)
        self.label4.setObjectName(u"label_title")
        self.label4.setFont(font)
        self.label4.setFrameStyle(QFrame.Sunken)
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setGeometry(QRect(50, 250, 661, 61))
        self.label4.setStyleSheet(u"color: rgb(244,103,68);")  # (98, 114, 164)
        self.label4.move(50,450)

        self.label4_entry_box=QLineEdit(self.centralwidget)
        self.label4_entry_box.setAlignment(Qt.AlignCenter)
        self.label4_entry_box.setGeometry(QRect(50, 50, 200, 40))
        self.label4_entry_box.setStyleSheet(u"color: rgb(255,230,0);")
        self.label4_entry_box.move(280,520)
        self.entry_box_list.append(self.label4_entry_box)

        self.button=QPushButton("Submit 🡺",self.centralwidget)
        self.button.setStyleSheet(u"color: rgb(255,255,255);")
        self.button.move(330,580)
        self.button.clicked.connect(partial(self.submit_btn_action, MainWindow))


        self.img_label = QLabel(self.centralwidget)

        self.pixmap = QPixmap(r"D:\GUI's\ML\p4.png")
        self.img_label.setPixmap(QPixmap(self.pixmap))
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")

        self.img_label.setGeometry(QRect(50, 50, 661, 601))
        self.img_label.move(700, 90)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def submit_btn_action(self,MainWindow):
        self.user_input={}
        self.user_key=['Employee_name','Employee_exp','Employee_test_score','Employee_Interview_scroe']
        for item in range(len(self.entry_box_list)):
            # print(self.user_key[item],'--> ',self.entry_box_list[item].text())
            self.user_input[self.user_key[item]]=self.entry_box_list[item].text()
        print(self.user_input)

        self.read_excel()
        self.model_creation()

        self.msgbox=QMessageBox()
        self.msgbox.setWindowFlags(Qt.FramelessWindowHint)
        # self.msgbox.setAttribute(Qt.WA_TranslucentBackground)
        self.msgbox.setFont(QFont("Cambria", 17, QFont.Bold))

        # self.msgbox.setStyleSheet("border :1px solid green")

        self.msgbox.setStyleSheet(u"color: rgb(255,168,46));")
        # self.msgbox.setStyleSheet("border - radius: 20px;")
        # self.msgbox.setStyleSheet(u"background-color: rgb(56, 58, 89);")

        self.msgbox.setInformativeText(f"PREDICTED SALARY for {self.user_input['Employee_name']} is: ₹ {int(self.result[0])}. \n “{self.result_in_word}” ")
        self.msgbox.move(900,400)
        self.msgbox.show()

    def image(self,MainWindow):
        self.img_label = QLabel(self.centralwidget)

        self.pixmap = QPixmap(r"C:\Users\Lord_Of_Forts\OneDrive\Recorded Videos\Isro_Mars_mission\india.png")
        self.img_label.setPixmap(self.pixmap)
        self.img_label.setGeometry(QRect(50, 50, 661, 601))
        self.img_label.move(700, 100)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SALARY PREDICTOR", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"SALARY PREDICTOR", None))
        self.label1.setText(QCoreApplication.translate("MainWindow",u"Employee Name",None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Employee Experience", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Employee Test Score(Out of 10)", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Employee Interview Score(Out of 10)", None))

