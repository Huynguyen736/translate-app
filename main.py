from PyQt5 import QtCore, QtGui, QtWidgets
from view.view import Ui_TranslateApp
from controller import AppFunction

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateApp = QtWidgets.QMainWindow()
    ui = Ui_TranslateApp()
    ui.setupUi(TranslateApp)
    AppFunction(ui)
    TranslateApp.show()
    sys.exit(app.exec_())