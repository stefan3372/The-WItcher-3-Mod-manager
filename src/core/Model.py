from typing import List
import os.path as path
import subprocess

from PyQt5.Qt import *

from src.config.Configuration import config
from src.core import Core
from src.util.Util import *
from src.domain import Mod
import xml.etree.ElementTree as XML




class Model:
    ModList: List[Mod] = []

    def openFolder(self, option):
        os.startfile(config.get('PATHS', option))

    def openFile(self, file):
        filename, ext = path.splitext(file)
        if (ext == ".exe" or ext == ".bat"):
            dir, name = path.split(file)
            subprocess.Popen(file, cwd=dir)
        else:
            os.startfile(file)

    def configureMods(self):
        self.modList = {}
        if (path.exists('installed.xml')):
            tree = XML.parse('installed.xml')
            root = tree.getroot()
            for xmlmod in root.findall('mod'):
                mod = Mod()
                mod.populateFromXml(xmlmod)
                self.modList[mod.name] = mod
        self.RefreshList()

    def rename(self):
        selected = self.getSelectedMods()
        if (selected):
            if (len(selected) > 1):
                QMessageBox.critical(self, _translate("MainWindow", "Error"),
                                     _translate("MainWindow", "Select only one mod to rename"))
            else:
                oldname = selected[0]
                newname, ok = QInputDialog.getText(self, _translate("MainWindow", 'Rename'),
                                                   _translate("MainWindow", 'Enter new mod name') + ": ",
                                                   QLineEdit.Normal, oldname)
                if ok:
                    mod = self.modList[oldname]
                    del self.modList[oldname]
                    mod.name = newname
                    self.modList[newname] = mod
                    self.RefreshList()


    def RunTheGame(self):
        try:
            gamepath = config.get('PATHS', 'gamepath')
            dir, name = path.split(gamepath)
            subprocess.Popen([gamepath], cwd=dir)
        except Exception as err:
            self.output(str(err))

    def RunScriptMerger(self):
        try:
            scriptmergerpath = config.get('PATHS', 'scriptmerger')
            if (scriptmergerpath):
                dir, name = path.split(scriptmergerpath)
                subprocess.Popen([scriptmergerpath], cwd=dir)
            else:
                self.ChangeScriptMergerPath()
                scriptmergerpath = config.get('PATHS', 'scriptmerger')
                if (scriptmergerpath):
                    dir, name = path.split(scriptmergerpath)
                    subprocess.Popen([scriptmergerpath], cwd=dir)
        except Exception as err:
            self.output(str(err))



    def InstallMods(self):
        try:
            self.clear()
            file = getFile(config.get('PATHS', 'lastpath'), "*.zip *.rar *.7z")
            if (file != None):
                prgrs = 0
                prgrsmax = len(file)
                for mod in file:
                    prgsbefore = 100 * prgrs / prgrsmax
                    prgsafter = 100 * (prgrs + 1) / prgrsmax
                    Core.installMod(self, mod, prgsbefore, prgsafter)
                    prgrs += 1
                    self.setProgress(100 * prgrs / prgrsmax)
                lastpath, name = path.split(file[0])
                config.set('PATHS', 'lastpath', lastpath)
                self.setProgress(0)
                self.RefreshList()
                if (path.exists("extracted")):
                    files.rmtree("extracted")
                self.AlertRunScriptMerger()
            else:
                self.output(_translate("MainWindow", "Installation canceled"))
        except Exception as err:
            self.setProgress(0)
            self.output(str(err))

    def UninstallMods(self):
        try:
            selected = self.getSelectedMods()
            if (selected):
                clicked = QMessageBox.question(self, _translate("MainWindow", "Confirm"),
                                               _translate("MainWindow", "Are you sure you want to uninstall ")
                                               + str(len(selected)) +
                                               _translate("MainWindow", " selected mods"),
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                if clicked == QMessageBox.Yes:
                    prgrs = 0
                    prgrsmax = len(selected)
                    for modname in selected:
                        try:
                            Core.uninstall(self.modList[modname])
                            del self.modList[modname]
                        except Exception as err:
                            self.output(str(err))
                        prgrs += 1
                        self.setProgress(100 * prgrs / prgrsmax)
                    self.RefreshList()
                    self.setProgress(0)
                    self.AlertRunScriptMerger()
        except Exception as err:
            self.setProgress(0)
            self.output(str(err))
