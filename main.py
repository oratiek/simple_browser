import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

my_app = QApplication(sys.argv)

initurl = "https://www.google.co.jp"

browser = QWebEngineView()
browser.load(QUrl(initurl))
browser.resize(1200,780)
browser.move(100,100)

browser.show()

sys.exit(my_app.exec_())
