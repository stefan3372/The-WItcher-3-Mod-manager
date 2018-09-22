import configparser
import ctypes.wintypes
import os
import re
import shutil as files
import sys
import xml.etree.ElementTree as XML
from distutils import dir_util as dirs

from PyQt5.QtCore import QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QTreeView, QHBoxLayout, QPlainTextEdit

config = configparser.ConfigParser(allow_no_value=True, delimiters='=')
priority = configparser.ConfigParser(allow_no_value=True, delimiters='=')
priority.optionxform = str
buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
documents = str(buf.value).replace('\\', '/')


def initconfig():
    config.read('config.ini')
    priority.read(documents + '/The Witcher 3/mods.settings')


def getini(section, option):
    if (config.has_option(section, option)):
        return config.get(section, option)
    else:
        return ""


def getpriority(modfile):
    if (modfile in priority.sections()):
        return priority[modfile]['Priority']
    else:
        return None


def setpriority(modfile, value):
    if (priority.has_section(modfile) == False):
        priority.add_section(modfile)
        priority.set(modfile, 'Enabled', '1')
    priority.set(modfile, 'Priority', value)


def setini(section, option, value):
    if (config.has_section(section) == False):
        config.add_section(section)
    config.set(section, option, value)
    iniwrite()


def setininovalue(section, value):
    config.set(section, value)
    iniwrite()


def getininovalue(section):
    list = []
    for value in config.items(section):
        list.append(value[0])
    return list


def removeininovalue(section, value):
    if (config.has_section(section)):
        config.remove_option(section, value)
    iniwrite()


def iniwrite():
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def savewindowsettings(ui, window):
    setini('WINDOW', 'width', str(window.width()))
    setini('WINDOW', 'height', str(window.height()))
    setini('WINDOW', 'section0', str(ui.treeWidget.header().sectionSize(0)))
    setini('WINDOW', 'section1', str(ui.treeWidget.header().sectionSize(1)))
    setini('WINDOW', 'section2', str(ui.treeWidget.header().sectionSize(2)))
    setini('WINDOW', 'section3', str(ui.treeWidget.header().sectionSize(3)))
    setini('WINDOW', 'section4', str(ui.treeWidget.header().sectionSize(4)))
    setini('WINDOW', 'section5', str(ui.treeWidget.header().sectionSize(5)))
    setini('WINDOW', 'section6', str(ui.treeWidget.header().sectionSize(6)))
    setini('WINDOW', 'section7', str(ui.treeWidget.header().sectionSize(7)))
    setini('WINDOW', 'section8', str(ui.treeWidget.header().sectionSize(8)))
    setini('WINDOW', 'section9', str(ui.treeWidget.header().sectionSize(9)))
    setini('WINDOW', 'section10', str(ui.treeWidget.header().sectionSize(10)))
    setini('WINDOW', 'section11', str(ui.treeWidget.header().sectionSize(11)))


def prioritywrite():
    with open(documents + '/The Witcher 3/mods.settings', 'w') as configfile:
        priority.write(configfile)
    text = ''
    with open(documents + '/The Witcher 3/mods.settings', 'r') as configfile:
        text = configfile.read()
    with open(documents + '/The Witcher 3/mods.settings', 'w') as configfile:
        text = text.replace(' = ', '=')
        configfile.write(text)


def restart_program():
    iniwrite()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def copyfolder(src, dest):
    if (not os.path.exists(dest)):
        files.copytree(src, dest)
    else:
        dirs.copy_tree(src, dest)


class FileDialog(QFileDialog):
    def __init__(self, *args):
        super(FileDialog, self).__init__(*args)
        self.setOption(QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QFileDialog.ExistingFiles)
        self.tree = self.findChild(QTreeView)
        self.resize(800, 800)
        self.selectedFiles = None
        self.exec_()

    def accept(self):
        inds = self.tree.selectionModel().selectedRows(0)
        self.selectedFiles = []
        for i in inds:
            self.selectedFiles.append(str(self.directory().absolutePath()) + "/" + str(i.data()))
        self.close()


def getFile(directory="", extensions="", title="Select Files or Folders"):
    return FileDialog(None, title, str(directory), str(extensions)).selectedFiles


def indent(elem, level=0):
    i = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def saveXML(modlist):
    root = XML.Element('installed')
    for mod in modlist.values():
        root = mod.writeToXml(root)
    indent(root)
    tree = XML.ElementTree(root)
    tree.write('installed.xml')


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


class Ui_Details(object):

    def setupUi(self, Details, text):
        Details.setObjectName("Details")
        Details.resize(700, 800)
        self.horizontalLayout = QHBoxLayout(Details)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(Details)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText(text)
        self.plainTextEdit.setReadOnly(True)
        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Details)
        QMetaObject.connectSlotsByName(Details)

    def retranslateUi(self, Details):
        _translate = QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Details"))


def getIcon(str):
    icon = QIcon()
    icon.addFile('res/' + str)
    return icon


def getKey(item):
    return item[1]


def isData(name):
    return re.match(r"^(~|)mod.+$", name)
