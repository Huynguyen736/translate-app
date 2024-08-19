from googletrans import Translator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtMultimedia, QtCore
import pyperclip
from gtts import gTTS
import os, sys

#import pydub
#from pydub.playback import play
#import time
#import pygame
#import wave
#import pyaudio

languagesCodes = {
	"Tiếng Anh":"en",
	"Tiếng Việt": "vi",
	"Tiếng Nhật": "ja",
	"Tiếng Hàn": "ko",
	"Tiếng Trung": "zh-cn"
}
trans = Translator()
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class AppFunction:
	def __init__(self, UI) -> None:
		global wgs
		wgs = UI
		self.widget = QWidget()
		self.init_connect()
		self.swap_language()
	
	def init_connect(self):
		wgs.loa.clicked.connect(lambda: self.audio_page_1())
		wgs.pushButton.clicked.connect(lambda: self.transFunc())  #Translate when clicked the button using translate(<text>, <lang>)
		wgs.copy.clicked.connect(lambda: self.copyText()) #Connect to copy button
		wgs.reverse.clicked.connect(lambda: self.swap_language())
	
	def transFunc(self):
		text = trans.translate(wgs.textEdit.toPlainText(), dest=languagesCodes[wgs.comboBox_2.currentText()]).text # Translate and convert text
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
		try:
			tts_object = gTTS(text=wgs.textEdit.toPlainText(), lang=languagesCodes[wgs.comboBox.currentText()])
			tts_object.save("output.wav")
			# Audio playback (didn't work)
			filename = os.path.join(CURRENT_DIR, "output.wav")
			QtMultimedia.QSound.play(filename)
			
		
		except Exception as e:
			print(f"An error occurred: {e}")

