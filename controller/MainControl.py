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
        self.showTranslate()
        self.copyText()
        
    
    def showTranslate(self):
        wgs.pushButton.clicked.connect(lambda: wgs.textEdit_2.setText(trans.translate(wgs.textEdit.toPlainText(), dest=languagesCodes[wgs.comboBox_2.currentText()]).text)) 
        #Translate when clicked the button using translate(<text>, <lang>)
        
    def copyText(self):
        wgs.copy.clicked.connect(lambda: pyperclip.copy(wgs.textEdit.toPlainText()))
        wgs.copy.clicked.connect(lambda: QMessageBox.information(self.widget, "Notice", "Copied!")) #QMessageBox first arg must be related to QWidget
        #Alert when copy


