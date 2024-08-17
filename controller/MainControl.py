from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
import pyperclip
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

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


    def swap_language(self):
        combobox_1_index = wgs.comboBox.currentIndex()
        combobox_2_index = wgs.comboBox_2.currentIndex()
        wgs.comboBox.setCurrentIndex(combobox_2_index)
        wgs.comboBox_2.setCurrentIndex(combobox_1_index)


    def audio_page_1(self):
        textedit_docs = wgs.textEdit.document()
        tts_content = textedit_docs.toPlainText()
        print(tts_content)
        tts_language = wgs.comboBox.currentData()
        print(tts_language)
        tts_object = gTTS(text="Hello World", lang="en")
        file_path = "output.mp3"
        tts_object.save(file_path)
        audio = AudioSegment.from_mp3(file_path)
        play(audio)

