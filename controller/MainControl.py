from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtCore import Qt
import pyperclip
from gtts import gTTS
import requests


languagesCodes = {
	"Tiếng Anh":"en",
	"Tiếng Việt": "vi",
	"Tiếng Nhật": "ja",
	"Tiếng Hàn": "ko",
	"Tiếng Trung": "zh-cn"
}
trans = Translator()

def request_mw(word):
	api_key = "0ce55ada-b016-4ebc-bf6b-0ef882015e5b"
	url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		return None
def data_filter(data, *keys):
	for key in keys:
		if isinstance(data, dict) and key in data:
			data = data[key]
		else:
			return None
	return data

class AppFunction:
	def __init__(self, UI) -> None:
		global wgs
		wgs = UI
		self.widget = QWidget()
		self.init_connect()
		self.init_variable()
		# self.swap_language()

	# Initialization connection
	def init_connect(self):
		wgs.loa1.clicked.connect(lambda: self.audio_page_1())
		wgs.dich.clicked.connect(lambda: self.transFunc())  # Translate when clicked the button using translate(<text>, <lang>)
		wgs.copy1.clicked.connect(lambda: self.copyText()) # Connect to copy button
		# wgs.reverse.clicked.connect(lambda: self.swap_language())
		

	# Initialization variable
	def init_variable(self):
		self.player = QtMultimedia.QMediaPlayer()
	
	def transFunc(self):
		text = trans.translate(wgs.textEdit.toPlainText(), dest=languagesCodes[wgs.combobox.currentText()]).text # Translate and convert text
		wgs.textEdit_2.setText(text)
	
	def copyText(self):
		pyperclip.copy(wgs.textEdit.toPlainText())
		QMessageBox.information(self.widget, "Notice", "Copied!") #QMessageBox first arg must be related to QWidget
		#Alert when copy
	
	def swap_language(self):
		combobox_1_index = wgs.comboBox.currentIndex()
		combobox_2_index = wgs.comboBox_2.currentIndex()
		wgs.comboBox.setCurrentIndex(combobox_2_index)
		wgs.comboBox_2.setCurrentIndex(combobox_1_index)
	
	def audio_page_1(self):
		tts_object = gTTS(text=wgs.textEdit.toPlainText(), lang=languagesCodes[wgs.combobox.currentText()])
		tts_object.save("output.wav")
		# Audio playback
		self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("output.wav")))
		self.player.play()

class Page_2_Function:
	def __init__(self, UI) -> None:
		global wgs
		wgs = UI

		
	def output_data(self):
		response_data = request_mw(wgs.entertext.toPlainText())
		headword = data_filter(response_data[0], "hwi", "hw")
		grammatical_function = data_filter(response_data[0], "fl")
		word_definition = data_filter(response_data[0], "hwi", "shortdef")
		ipa_pronunciation = data_filter(response_data[0], "hwi", "prs", 0, "mw")
		wgs.hello.setText(headword)
		wgs.noun.setText(grammatical_function)
		wgs.definition.setText(word_definition)
		

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			self.output_data()
		
		
	