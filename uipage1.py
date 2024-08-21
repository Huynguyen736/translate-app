# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view2.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslateApp(object):
    def setupUi(self, TranslateApp):
        TranslateApp.setObjectName("TranslateApp")
        TranslateApp.resize(1280, 720)
        TranslateApp.setMinimumSize(QtCore.QSize(1, 1))
        TranslateApp.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        TranslateApp.setFont(font)
        TranslateApp.setAutoFillBackground(False)
        TranslateApp.setStyleSheet("background-color: rgb(159, 199, 240);")
        TranslateApp.setProperty("fa", "")
        self.centralwidget = QtWidgets.QWidget(TranslateApp)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(500, -10, 331, 81))
        self.name.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name.setFont(font)
        self.name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 110, 851, 241))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 2px solid rgb(255, 255, 255); \n"
"    border-radius: 20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 390, 851, 271))
        self.textEdit_2.setStyleSheet("QTextEdit {\n"
"    border: 2px solid rgb(255, 255, 255); \n"
"    border-radius: 20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.loa1 = QtWidgets.QPushButton(self.centralwidget)
        self.loa1.setGeometry(QtCore.QRect(960, 290, 61, 51))
        self.loa1.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/louder.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/louder - Copy.png);\n"
"}")
        self.loa1.setText("")
        self.loa1.setObjectName("loa1")
        self.copy2 = QtWidgets.QPushButton(self.centralwidget)
        self.copy2.setGeometry(QtCore.QRect(910, 600, 51, 51))
        self.copy2.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/copy.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/copy - Copy.png);\n"
"}")
        self.copy2.setText("")
        self.copy2.setObjectName("copy2")
        self.dich = QtWidgets.QPushButton(self.centralwidget)
        self.dich.setGeometry(QtCore.QRect(1080, 330, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.dich.setFont(font)
        self.dich.setStyleSheet("background-color: rgb(74, 136, 199);")
        self.dich.setObjectName("dich")
        self.combobox = QtWidgets.QComboBox(self.centralwidget)
        self.combobox.setGeometry(QtCore.QRect(1070, 210, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.combobox.setFont(font)
        self.combobox.setStyleSheet("QComboBox {\n"
"    \n"
"    background-color: rgb(74, 136, 199);\n"
"    border-radius: 15px\n"
"}")
        self.combobox.setObjectName("combobox")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.loa2 = QtWidgets.QPushButton(self.centralwidget)
        self.loa2.setGeometry(QtCore.QRect(960, 600, 61, 51))
        self.loa2.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/louder.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/louder - Copy.png);\n"
"}")
        self.loa2.setText("")
        self.loa2.setObjectName("loa2")
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
        self.copy1 = QtWidgets.QPushButton(self.centralwidget)
        self.copy1.setGeometry(QtCore.QRect(910, 290, 51, 51))
        self.copy1.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/copy.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/copy - Copy.png);\n"
"}")
        self.copy1.setText("")
        self.copy1.setObjectName("copy1")
        TranslateApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TranslateApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        TranslateApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TranslateApp)
        self.statusbar.setObjectName("statusbar")
        TranslateApp.setStatusBar(self.statusbar)

        self.retranslateUi(TranslateApp)
        QtCore.QMetaObject.connectSlotsByName(TranslateApp)

    def retranslateUi(self, TranslateApp):
        _translate = QtCore.QCoreApplication.translate
        TranslateApp.setWindowTitle(_translate("TranslateApp", "TranslateApp"))
        TranslateApp.setWhatsThis(_translate("TranslateApp", "<html><head/><body><p align=\"center\">wfeawefwaefwaefawef</p></body></html>"))
        self.name.setText(_translate("TranslateApp", "Translate App"))
        self.textEdit.setHtml(_translate("TranslateApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("TranslateApp", "Enter text"))
        self.dich.setText(_translate("TranslateApp", "Dịch"))
        self.combobox.setItemText(0, _translate("TranslateApp", "Tiếng Anh"))
        self.combobox.setItemText(1, _translate("TranslateApp", "Tiếng Việt"))
        self.combobox.setItemText(2, _translate("TranslateApp", "Tiếng Trung"))
        self.combobox.setItemText(3, _translate("TranslateApp", "Tiếng Nhật"))
        self.combobox.setItemText(4, _translate("TranslateApp", "Tiếng Hàn"))
        self.page1.setText(_translate("TranslateApp", "1"))
        self.page2.setText(_translate("TranslateApp", "2"))
from view import new_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateApp = QtWidgets.QMainWindow()
    ui = Ui_TranslateApp()
    ui.setupUi(TranslateApp)
    TranslateApp.show()
    sys.exit(app.exec_())
