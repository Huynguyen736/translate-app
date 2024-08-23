from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtMultimedia, QtCore
import pyperclip
from gtts import gTTS
import requests
import os, tempfile, time

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

	# Initialization connection
	def init_connect(self):
		wgs.loa1.clicked.connect(lambda: self.audio_page_1())
		wgs.dich.clicked.connect(lambda: self.transFunc())  # Translate when clicked the button using translate(<text>, <lang>)
		wgs.copy1.clicked.connect(lambda: self.copyText()) # Connect to copy button
		wgs.copy2.clicked.connect(lambda: self.copyText())
		wgs.copy2.clicked.connect(lambda: self.request_data())
		wgs.ukloa.clicked.connect(lambda: self.play_UK_audio())
		wgs.usloa.clicked.connect(lambda: self.play_US_audio())
		wgs.find.clicked.connect(lambda: self.output_mw_data())

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
		self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(None)))
		ptext = wgs.textEdit.toPlainText()
		tts_object = gTTS(text=ptext, lang=languagesCodes[wgs.combobox.currentText()])
		audiopath = os.path.join(tempfile.gettempdir(), "output.wav")
		tts_object.save(audiopath)
		self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(audiopath)))
		self.player.play()
		time.sleep(0.1)
		os.remove(audiopath)

	def request_data(self, word):
		url = f'https://www.oxfordlearnersdictionaries.com/definition/english/{word}'
		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
			"Pragma": "no-cache",
			"Accept": "*/*"
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			with open('tra_tu.txt', 'wb') as f:
				f.write(response.text.encode('utf-8')) # Vì cái requests data quá dài nên anh dùng ghi file nhé

	def output_mw_data(self):
		try:
			res_data = request_mw(wgs.entertext.text())
			self.request_data(wgs.entertext.text())
			headword = wgs.entertext.text()
			grammatical_function = res_data[0]["fl"]
			word_def = res_data[0]["shortdef"][0]
			ipa_pronunciation = res_data[0]["hwi"]["prs"][0]["mw"]
			#example_usage = res_text[0]["dt"]["vis"]
			wgs.hello.setText(headword)
			wgs.noun.setText(grammatical_function)
			wgs.pronon_2.setText(ipa_pronunciation)
			wgs.definition.setText(word_def)
			wgs.level.setText("Level " + self.query_wordLevel())
		except Exception as e:
			print(e)

	def query_audio(arg):
		with open('tra_tu.txt', 'r', encoding='utf-8') as f:
			file = f.readlines()
		for line in file:
			if '<div id="entryContent"' in line:
				lst = [i for i in line.split() if "data-src-mp3" in i][:2]
				result = [i.split('=')[1].strip('"') for i in lst]
		return result
	
	def play_UK_audio(self):
		url = self.query_audio()[0]
		self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(url)))
		self.player.play()
		
	def play_US_audio(self):
		url = self.query_audio()[1]
		self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(url)))
		self.player.play()

	def query_wordLevel(arg):
		with open('tra_tu.txt', 'r', encoding='utf-8') as f:
			file = f.readlines()
		for line in file:
			if '<div id="entryContent"' in line:
				for i in line.split():
					if "https://www.oxfordlearnersdictionaries.com/wordlists" in i:
						return (i[-9:-7].upper())