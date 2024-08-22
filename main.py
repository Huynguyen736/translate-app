from PyQt5 import QtCore, QtGui, QtWidgets
from view.view import Ui_TranslateApp
from view.uipage2 import Ui_TranslateApp2
from controller import AppFunction

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateApp = QtWidgets.QMainWindow()
    ui = Ui_TranslateApp()
    ui2 = Ui_TranslateApp2()
    ui.setupUi(TranslateApp)
    AppFunction(ui, ui2)
    TranslateApp.show()
    sys.exit(app.exec_())