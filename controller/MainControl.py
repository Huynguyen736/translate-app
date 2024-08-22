from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtCore import Qt
import pyperclip
from gtts import gTTS
import requests
import os, time
import threading
import json


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

class AppFunction:
	def __init__(self, UI) -> None:
		global wgs
		wgs = UI
		self.widget = QWidget()
		self.init_connect()
		self.init_variable()
		self.output_mw_data()
		# self.swap_language()

	# Initialization connection
	def init_connect(self):
		wgs.loa1.clicked.connect(lambda: self.audio_page_1())
		wgs.dich.clicked.connect(lambda: self.transFunc())  # Translate when clicked the button using translate(<text>, <lang>)
		wgs.copy1.clicked.connect(lambda: self.copyText()) # Connect to copy button
		wgs.copy2.clicked.connect(lambda: self.copyText())
		wgs.copy2.clicked.connect(lambda: self.request_data())
		wgs.find.clicked.connect(lambda: self.output_mw_data())
		wgs.entertext.returnPressed.connect(lambda: self.output_mw_data())
	

	# Initialization variable
	def init_variable(self):
		self.player = QtMultimedia.QMediaPlayer()
	
	# Function define
	def transFunc(self):
		text = trans.translate(wgs.textEdit.toPlainText(), dest=languagesCodes[wgs.combobox.currentText()]).text # Translate and convert text
		wgs.textEdit_2.setText(text)
	
	def copyText(self):
		pyperclip.copy(wgs.textEdit.toPlainText())
		QMessageBox.information(self.widget, "Notice", "Copied!") #QMessageBox first arg must be related to QWidget
		#Alert when copy
	
	def audio_page_1(self):
		try:
			ptext = wgs.textEdit.toPlainText()
			print(ptext)
			tts_object = gTTS(text=ptext, lang=languagesCodes[wgs.combobox.currentText()])
			tts_object.save("output.wav")
			# Audio playback
			self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("output.wav")))
			self.player.play()
		except:
			os.remove("output.wav")
			time.sleep(0.01)

		
	def request_data(self):
		url = f'https://www.oxfordlearnersdictionaries.com/definition/english/hello_1'
		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
			"Pragma": "no-cache",
			"Accept": "*/*"
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			with open('tra_tu.txt', 'wb') as f:
				f.write(response.text.encode('utf-8'))  # Vì cái requests data quá dài nên anh dùng ghi file nhé

	def output_mw_data(self):
		try:
			res_data = request_mw(wgs.entertext.text())
			headword = wgs.entertext.text()
			grammatical_function = res_data[0]["fl"]
			for definitions in res_data[0]["shortdef"]:
				wgs.def_text.setText(definitions)
			ipa_pronunciation = res_data[0]["hwi"]["prs"][0]["mw"]
			#example_usage = res_text[0]["dt"]["vis"]
			wgs.hello.setText(headword)
			wgs.noun.setText(grammatical_function)
			wgs.pronon_2.setText(ipa_pronunciation)
		except Exception as e:
			print(e)
		

