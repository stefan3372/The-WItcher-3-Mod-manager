import ctypes
import os.path as path
from src import config
from src.config.Configuration import Configuration
from src.gui import Ui_MainWindow

from src.util.Util import *


def __getDocuments():
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
    return str(buf.value).replace('\\', '/')


def __translateToChosenLanguage():
    language = config.data.language
    if (language and path.exists("translations/" + language)):
        translator = QtCore.QTranslator()
        translator.load("translations/" + language)
        app.installTranslator(translator)


if __name__ == "__main__":
    documents = __getDocuments()
    config.data = Configuration(documents)
    app = QtWidgets.QApplication(sys.argv)
    __translateToChosenLanguage()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setWindowIcon(getIcon("w3a.ico"))
    MainWindow.show()

    ret = app.exec_()
    config.data.saveWindowSettings(ui, MainWindow)
    config.data.write()
    saveXML(ui.modList)

    sys.exit(ret)
