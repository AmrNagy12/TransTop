from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic
import pyttsx3
import googletrans
import os
import sys
import PyQt5
import playsound2
import gtts

class Ui(QtWidgets.QMainWindow):
                def __init__(self):
                    super(Ui, self).__init__()
                    uic.loadUi('transletor.ui', self)
                    self.show()
                    self.setWindowTitle("Text Translator")
                    self.setFixedSize(630, 450)
                    self.mandelbuttons()
                    self.lang = 'en'
                def mandelbuttons(self):
                    self.pushButton.clicked.connect(self.mandelkompobox)
                    self.pushButton_3.clicked.connect(self.speak)

                def mandelkompobox(self):
                    try:
                        translator = googletrans.Translator()
                        texttolang = self.textEdit.toPlainText()
                        tolangwithnone = self.comboBox_2.currentIndex()
                        

                        if tolangwithnone == 1:
                            translat = translator.translate(texttolang , dest= 'Arabic')
                            self.textEdit_2.setText(str(translat.text))
                            lang = 'ar'

                        elif tolangwithnone == 2:
                            translat = translator.translate(texttolang , dest= 'English')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'en'

                        elif tolangwithnone == 3:
                            translat = translator.translate(texttolang , dest= 'Chinese')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'ch'

                        elif tolangwithnone == 4:
                            translat = translator.translate(texttolang , dest= 'German')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'German'

                        elif tolangwithnone == 5:
                            translat = translator.translate(texttolang , dest= 'Italian')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Italian'

                        elif tolangwithnone == 6:
                            translat = translator.translate(texttolang , dest= 'Japanese')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Japanese'

                        elif tolangwithnone == 7:
                            translat = translator.translate(texttolang , dest= 'Portuguese')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Portuguese'

                        elif tolangwithnone == 8:
                            translat = translator.translate(texttolang , dest= 'Korean')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Korean'

                        elif tolangwithnone == 9:
                            translat = translator.translate(texttolang , dest= 'Russian')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Russian'

                        elif tolangwithnone == 10:
                            translat = translator.translate(texttolang , dest= 'Spanish')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Spanish'

                        elif tolangwithnone == 11:
                            translat = translator.translate(texttolang , dest= 'Dutch')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Dutch'

                        elif tolangwithnone == 12:
                            translat = translator.translate(texttolang , dest= 'French')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'French'

                        elif tolangwithnone == 13:
                            translat = translator.translate(texttolang , dest= 'Indonesian')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Indonesian'

                        elif tolangwithnone == 14:
                            translat = translator.translate(texttolang , dest= 'Thai')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Thai'

                        elif tolangwithnone == 15:
                            translat = translator.translate(texttolang , dest= 'Turkish')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Turkish'

                        elif tolangwithnone == 16:
                            translat = translator.translate(texttolang , dest= 'Vietnamese')
                            self.textEdit_2.setPlainText(str(translat.text))
                            lang = 'Vietnamese'

                    except:
                        QtWidgets.QMessageBox.warning(self, "Translate", "translate Error ,please try later")
                def speak(self):
                    try:
                        gtts.gTTS(text= self.textEdit_2.toPlainText() , lang= self.lang).save("speek.mp3")
                        playsound2.playsound('speek.mp3')
                        os.remove('speek.mp3')
                    except:
                        QtWidgets.QMessageBox.warning(self, "Translate", "translate Error ,please try later")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()