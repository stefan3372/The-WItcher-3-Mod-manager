import ctypes
import os.path as path

from config.Configuration import config
from util.Util import *

if __name__ == "__main__":

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
    documents = str(buf.value).replace('\\', '/')

    app = QtWidgets.QApplication(sys.argv)

    language = config.get('SETTINGS', 'language')
    if (language and path.exists("translations/" + language)):
        translator = QtCore.QTranslator()
        translator.load("translations/" + language)
        app.installTranslator(translator)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setWindowIcon(getIcon("w3a.ico"))
    MainWindow.show()

    ret = app.exec_()
    saveWindowSettings(ui, MainWindow)
    iniWrite()
    saveXML(ui.modList)

    sys.exit(ret)
