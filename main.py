from PyQt5 import QtCore, QtGui, QtWidgets
# from view.uipage1 import Ui_TranslateApp
from view.uipage2 import Ui_TranslateApp
from controller import Page_2_Function

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateApp = QtWidgets.QMainWindow()
    ui = Ui_TranslateApp()
    ui.setupUi(TranslateApp)
    Page_2_Function(ui)
    TranslateApp.show()
    sys.exit(app.exec_())
