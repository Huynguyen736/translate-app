# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uipage2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Page2(object):
    def setupUi(self, TranslateApp):
        TranslateApp.setObjectName("TranslateApp")
        TranslateApp.resize(1292, 720)
        font = QtGui.QFont()
        font.setItalic(True)
        TranslateApp.setFont(font)
        TranslateApp.setStyleSheet("background-color: rgb(159, 199, 240);")
        self.centralwidget = TranslateApp
        self.centralwidget.setObjectName("centralwidget")
        self.entertext = QtWidgets.QLineEdit(self.centralwidget)
        self.entertext.setGeometry(QtCore.QRect(170, 27, 1071, 49))
        self.entertext.setStyleSheet("QLineEdit {\n"
"    border-radius: 20px;\n"
"    background-color: rgb(228, 239, 251);\n"
"    padding-left: 70px;\n"
"    padding-right: 20px;\n"
"}\n"
"")
        self.entertext.setObjectName("entertext")
        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(180, 30, 51, 41))
        self.find.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(228, 239, 251);\n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/search.png);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/search - Copy.png);\n"
"}")
        self.find.setText("")
        self.find.setObjectName("find")
        self.micro = QtWidgets.QPushButton(self.centralwidget)
        self.micro.setGeometry(QtCore.QRect(1190, 32, 41, 41))
        self.micro.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(228, 239, 251);\n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/mic (2).png);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/mic (2) - Copy.png);\n"
"}")
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.hello = QtWidgets.QLabel(self.centralwidget)
        self.hello.setGeometry(QtCore.QRect(160, 80, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Public Sans Black")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.hello.setFont(font)
        self.hello.setObjectName("hello")
        self.noun = QtWidgets.QLabel(self.centralwidget)
        self.noun.setGeometry(QtCore.QRect(440, 120, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(15)
        font.setItalic(True)
        self.noun.setFont(font)
        self.noun.setObjectName("noun")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(170, 180, 1101, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.level = QtWidgets.QLabel(self.centralwidget)
        self.level.setGeometry(QtCore.QRect(170, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cabin Condensed SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.level.setFont(font)
        self.level.setObjectName("level")
        self.uk = QtWidgets.QLabel(self.centralwidget)
        self.uk.setGeometry(QtCore.QRect(190, 250, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.uk.setFont(font)
        self.uk.setObjectName("uk")
        self.us = QtWidgets.QLabel(self.centralwidget)
        self.us.setGeometry(QtCore.QRect(190, 290, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.us.setFont(font)
        self.us.setObjectName("us")
        self.ukloa = QtWidgets.QPushButton(self.centralwidget)
        self.ukloa.setGeometry(QtCore.QRect(230, 244, 41, 41))
        self.ukloa.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/loa_xanh.png);\n"
"}\n"
"QPushButton:hover {\n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/loa_xanh copy.png);\n"
"}")
        self.ukloa.setText("")
        self.ukloa.setObjectName("ukloa")
        self.pronon1 = QtWidgets.QLabel(self.centralwidget)
        self.pronon1.setGeometry(QtCore.QRect(290, 253, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pronon1.setFont(font)
        self.pronon1.setObjectName("pronon1")
        self.pronon_2 = QtWidgets.QLabel(self.centralwidget)
        self.pronon_2.setGeometry(QtCore.QRect(290, 294, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pronon_2.setFont(font)
        self.pronon_2.setObjectName("pronon_2")
        self.definition = QtWidgets.QLabel(self.centralwidget)
        self.definition.setGeometry(QtCore.QRect(170, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.definition.setFont(font)
        self.definition.setObjectName("definition")
        self.def_text = QtWidgets.QLabel(self.centralwidget)
        self.def_text.setGeometry(QtCore.QRect(310, 320, 961, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.def_text.setFont(font)
        self.def_text.setObjectName("def_text")
        self.example = QtWidgets.QLabel(self.centralwidget)
        self.example.setGeometry(QtCore.QRect(170, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.example.setFont(font)
        self.example.setObjectName("example")
        self.example_text = QtWidgets.QLabel(self.centralwidget)
        self.example_text.setGeometry(QtCore.QRect(200, 410, 1001, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.example_text.setFont(font)
        self.example_text.setObjectName("example_text")
        self.example_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.example_text_2.setGeometry(QtCore.QRect(200, 450, 1021, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.example_text_2.setFont(font)
        self.example_text_2.setObjectName("example_text_2")
        self.example_text_3 = QtWidgets.QLabel(self.centralwidget)
        self.example_text_3.setGeometry(QtCore.QRect(200, 500, 1031, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.example_text_3.setFont(font)
        self.example_text_3.setObjectName("example_text_3")
        self.circle1 = QtWidgets.QLabel(self.centralwidget)
        self.circle1.setGeometry(QtCore.QRect(130, 377, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle1.setFont(font)
        self.circle1.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle1.setObjectName("circle1")
        self.circle2 = QtWidgets.QLabel(self.centralwidget)
        self.circle2.setGeometry(QtCore.QRect(130, 420, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle2.setFont(font)
        self.circle2.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle2.setObjectName("circle2")
        self.circle3 = QtWidgets.QLabel(self.centralwidget)
        self.circle3.setGeometry(QtCore.QRect(130, 459, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle3.setFont(font)
        self.circle3.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle3.setObjectName("circle3")
        self.Synonyms = QtWidgets.QLabel(self.centralwidget)
        self.Synonyms.setGeometry(QtCore.QRect(170, 550, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Synonyms.setFont(font)
        self.Synonyms.setObjectName("Synonyms")
        self.Antonyms = QtWidgets.QLabel(self.centralwidget)
        self.Antonyms.setGeometry(QtCore.QRect(800, 550, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.Antonyms.setFont(font)
        self.Antonyms.setObjectName("Antonyms")
        self.circle4 = QtWidgets.QLabel(self.centralwidget)
        self.circle4.setGeometry(QtCore.QRect(160, 560, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle4.setFont(font)
        self.circle4.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle4.setObjectName("circle4")
        self.circle5 = QtWidgets.QLabel(self.centralwidget)
        self.circle5.setGeometry(QtCore.QRect(160, 600, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle5.setFont(font)
        self.circle5.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle5.setObjectName("circle5")
        self.syntext = QtWidgets.QLabel(self.centralwidget)
        self.syntext.setGeometry(QtCore.QRect(250, 590, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.syntext.setFont(font)
        self.syntext.setObjectName("syntext")
        self.syntext_2 = QtWidgets.QLabel(self.centralwidget)
        self.syntext_2.setGeometry(QtCore.QRect(250, 640, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.syntext_2.setFont(font)
        self.syntext_2.setObjectName("syntext_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(790, 560, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.antext = QtWidgets.QLabel(self.centralwidget)
        self.antext.setGeometry(QtCore.QRect(880, 600, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.antext.setFont(font)
        self.antext.setObjectName("antext")
        self.circle7 = QtWidgets.QLabel(self.centralwidget)
        self.circle7.setGeometry(QtCore.QRect(790, 600, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle7.setFont(font)
        self.circle7.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle7.setObjectName("circle7")
        self.circle6 = QtWidgets.QLabel(self.centralwidget)
        self.circle6.setGeometry(QtCore.QRect(790, 560, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(61)
        self.circle6.setFont(font)
        self.circle6.setStyleSheet("QLabel {\n"
"    padding-left: 27px;\n"
"}")
        self.circle6.setObjectName("circle6")
        self.antext_2 = QtWidgets.QLabel(self.centralwidget)
        self.antext_2.setGeometry(QtCore.QRect(880, 630, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.antext_2.setFont(font)
        self.antext_2.setObjectName("antext_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 20, 51, 641))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 360, 141, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.page1 = QtWidgets.QPushButton(self.centralwidget)
        self.page1.setGeometry(QtCore.QRect(20, 140, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.page1.setFont(font)
        self.page1.setObjectName("page1")
        self.page2 = QtWidgets.QPushButton(self.centralwidget)
        self.page2.setGeometry(QtCore.QRect(20, 480, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.page2.setFont(font)
        self.page2.setObjectName("page2")
        self.usloa = QtWidgets.QPushButton(self.centralwidget)
        self.usloa.setGeometry(QtCore.QRect(230, 290, 41, 31))
        self.usloa.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/loa_do.png);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/resource/drive-download-20240818T010916Z-001/loa_do copy.png);\n"
"}")
        self.usloa.setText("")
        self.usloa.setObjectName("usloa")
        self.entertext.raise_()
        self.circle5.raise_()
        self.micro.raise_()
        self.hello.raise_()
        self.noun.raise_()
        self.line_3.raise_()
        self.uk.raise_()
        self.us.raise_()
        self.ukloa.raise_()
        self.pronon1.raise_()
        self.pronon_2.raise_()
        self.definition.raise_()
        self.def_text.raise_()
        self.example_text.raise_()
        self.find.raise_()
        self.example_text_2.raise_()
        self.example_text_3.raise_()
        self.circle4.raise_()
        self.Synonyms.raise_()
        self.syntext.raise_()
        self.syntext_2.raise_()
        self.label_19.raise_()
        self.antext.raise_()
        self.circle7.raise_()
        self.circle6.raise_()
        self.Antonyms.raise_()
        self.antext_2.raise_()
        self.page1.raise_()
        self.page2.raise_()
        self.level.raise_()
        self.circle3.raise_()
        self.circle2.raise_()
        self.circle1.raise_()
        self.example.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.usloa.raise_()
        self.menubar = QtWidgets.QMenuBar(TranslateApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1292, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(TranslateApp)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(TranslateApp)
        QtCore.QMetaObject.connectSlotsByName(TranslateApp)

    def retranslateUi(self, TranslateApp):
        _translate = QtCore.QCoreApplication.translate
        TranslateApp.setWindowTitle(_translate("TranslateApp", "MainWindow"))
        self.entertext.setPlaceholderText(_translate("TranslateApp", "Nhập vào đây"))
        self.hello.setText(_translate("TranslateApp", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#3c33a5;\">Hello</span></p></body></html>"))
        self.noun.setText(_translate("TranslateApp", "noun"))
        self.level.setText(_translate("TranslateApp", "Level A1"))
        self.uk.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-weight:600; color:#3180ff;\">UK</span></p></body></html>"))
        self.us.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-weight:600; color:#bc0000;\">US</span></p></body></html>"))
        self.pronon1.setText(_translate("TranslateApp", "/heˈləʊ/"))
        self.pronon_2.setText(_translate("TranslateApp", "/heˈloʊ/"))
        self.definition.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#2f2b61;\">Definition</span></p></body></html>"))
        self.def_text.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; color:#093a7c;\">used when </span><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">meeting</span><span style=\" font-size:14pt; color:#093a7c;\"> or </span><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">greeting</span><span style=\" font-size:14pt; color:#093a7c;\"> someone</span></p></body></html>"))
        self.example.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#2f2b61;\">Example</span></p><p><br/></p></body></html>"))
        self.example_text.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; color:#093a7c;\">Hello Paul. I haven\'t seen you for ages</span></p></body></html>"))
        self.example_text_2.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; color:#093a7c;\">say hello I just thought I\'d call by and say hello</span></p></body></html>"))
        self.example_text_3.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; color:#093a7c;\">I know her vaguely - we\'ve exchanged hellos a few times</span></p><p><span style=\" font-size:14pt; color:#093a7c;\"/></p></body></html>"))
        self.circle1.setText(_translate("TranslateApp", "."))
        self.circle2.setText(_translate("TranslateApp", "."))
        self.circle3.setText(_translate("TranslateApp", "."))
        self.Synonyms.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-weight:600; color:#2f2b61;\">Synonyms</span></p></body></html>"))
        self.Antonyms.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-weight:600; color:#2f2b61;\">Antonyms</span></p><p><span style=\" font-weight:600; color:#2f2b61;\"><br/></span></p></body></html>"))
        self.circle4.setText(_translate("TranslateApp", "."))
        self.circle5.setText(_translate("TranslateApp", "."))
        self.syntext.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">greeting</span></p></body></html>"))
        self.syntext_2.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">remembrance</span></p><p><br/></p></body></html>"))
        self.label_19.setText(_translate("TranslateApp", "."))
        self.antext.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">goodbye</span></p><p><br/></p></body></html>"))
        self.circle7.setText(_translate("TranslateApp", "."))
        self.circle6.setText(_translate("TranslateApp", "."))
        self.antext_2.setText(_translate("TranslateApp", "<html><head/><body><p><span style=\" font-size:14pt; text-decoration: underline; color:#093a7c;\">solong</span></p></body></html>"))
        self.page1.setText(_translate("TranslateApp", "1"))
        self.page2.setText(_translate("TranslateApp", "2"))
from . import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateApp = QtWidgets.QMainWindow()
    ui = Ui_Page2()
    ui.setupUi(TranslateApp)
    TranslateApp.show()
    sys.exit(app.exec_())
