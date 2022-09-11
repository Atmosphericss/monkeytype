import sys, time

from PyQt5 import QtWebEngineWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl, QThread, pyqtSignal
from bs4 import BeautifulSoup
from pypresence import Presence



class Worker(QThread):
    result = pyqtSignal(str)

    def run(self):
        self.keepRunning = True
        while self.keepRunning:
            res = 'check'
            self.result.emit(res)
            time.sleep(5)

    def stop(self):
        self.keepRunning = False
        self.wait()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowIcon(QIcon('monkeytype.png'))
        self.setWindowTitle('monkeytype')
        self.setCentralWidget(WebView())
        self.show()

#This class will stop JS errors being written to the console main.py was launched from
class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        pass

class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.temp_wpm = ''
        self.loadFinished.connect(self._load_finished)
        self.worker = Worker()
        self.worker.result.connect(self.resultReceived)
        page = WebEnginePage(self)
        self.setPage(page)
        self.load(QUrl("https://www.monkeytype.com"))


    def _load_finished(self, result):
        if result:

            self.start()
        else:
            print("Page failed to load")


    def to_html(self):
        try:
            html = self.page().toHtml(self.handler)
        except:
            pass


    def handler(self, data):
        self.html = data
        soup = BeautifulSoup(self.html, 'html.parser')
        livewpm = soup.find('div', {'id': 'liveWpm'})
        livewpm = livewpm.string
        wpm = soup.find('div', {'class': 'bottom'})
        wpm = wpm.string
        # print(f'WPM:{wpm}    LIVE:{livewpm}')
        if wpm != '-' and wpm != self.temp_wpm:
            RPC.update(state=f"Just got {wpm} wpm!", large_image='monkeytype', small_image='monkeytype',
                       details='Aping out on monkeytype.com 🐒')
            self.temp_wpm = wpm
        elif wpm == '-' and (livewpm == '123' or livewpm == '0') and wpm == self.temp_wpm:
            RPC.update(state=f"Messing around in the menus", large_image='monkeytype', small_image='monkeytype',
                       details='Aping out on monkeytype.com 🐒')
        else:
            RPC.update(state=f"Currently typing at {livewpm} wpm", large_image='monkeytype', small_image='monkeytype',
                       details='Aping out on monkeytype.com 🐒')



    def start(self):
        if not self.worker.isRunning():
            self.worker.start()

    def stop(self):
        self.worker.stop()

    def resultReceived(self, result):
        self.to_html()


if __name__ == '__main__':
    RPC = Presence('984565344465219694')
    RPC.connect()
    RPC.update(state="Just loaded MTDesktop", large_image='monkeytype', small_image='monkeytype',
               details='Aping out on monkeytype.com 🐒')
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

