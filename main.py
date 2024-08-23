from PyQt5 import QtCore, QtGui, QtWidgets
from view.view import Ui_TranslateApp
from controller import AppFunction


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = Ui_TranslateApp()
	AppFunction(ui.ui)
	ui.show()
	sys.exit(app.exec_())

