from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
import pyperclip

languagesCodes = {
    "Tiếng Anh":"en",
    "Tiếng Việt": "vi",
    "Tiếng Nhật": "ja",
    "Tiếng Hàn": "ko",
    "Tiếng Trung": "zh-tw"
}
trans = Translator()
class AppFunction:
    def __init__(self, UI) -> None:
        global wgs
        wgs = UI
        self.widget = QWidget()
        self.init_connect()
        

    def init_connect(self):
        wgs.pushButton.clicked.connect(lambda: self.transFunc())  #Translate when clicked the button using translate(<text>, <lang>)
        wgs.copy.clicked.connect(lambda: self.copyText()) #Connect to copy button

    def transFunc(self):
        text = trans.translate(wgs.textEdit.toPlainText(), dest=languagesCodes[wgs.comboBox_2.currentText()]).text  # Translate and convert text
        wgs.textEdit_2.setText(text)

    def copyText(self):
        pyperclip.copy(wgs.textEdit.toPlainText())
        QMessageBox.information(self.widget, "Notice", "Copied!") #QMessageBox first arg must be related to QWidget
        #Alert when copy


