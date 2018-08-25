import os
import re
import shutil as files
import sys
from distutils import dir_util as dirs

from PyQt5 import QtWidgets, QtCore, QtGui


def restart_program():
    iniWrite()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def copyfolder(src, dest):
    if (not os.path.exists(dest)):
        files.copytree(src, dest)
    else:
        dirs.copy_tree(src, dest)


class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        super(FileDialog, self).__init__(*args)
        self.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.tree = self.findChild(QtWidgets.QTreeView)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Details)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Details)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText(text)
        self.plainTextEdit.setReadOnly(True)
        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Details)
        QtCore.QMetaObject.connectSlotsByName(Details)

    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Details"))


def getIcon(str):
    icon = QtGui.QIcon()
    icon.addFile('res/' + str)
    return icon


def getKey(item):
    return item[1]


def isData(name):
    return re.match(r"^(~|)mod.+$", name)
