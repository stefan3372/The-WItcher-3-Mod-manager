import os.path as path

from PyQt5.Qt import QMessageBox

from Util import *


class Mod(object):

    def __init__(self, *args):
        self.name = ''
        self.files = []
        self.dlcs = []
        self.menus = []
        self.xmlkeys = []
        self.usersettings = []
        self.inputsettings = []
        self.hidden = []
        self.enabled = True
        self.date = '-'
        self.priority = None

    def getPriority(self):
        return self.priority if self.priority else '-'

    def setPriority(self, value):
        for data in self.files:
            setPriority(data, value)
        self.priority = str(value)

    def setName(self, name):
        name = self.__removeLeadingModWord(name)
        name = self.__removeVersion(name)
        name = self.__removeExtension(name)
        self.name = name

    def enable(self):
        if self.enabled:
            return
        self.installXmlKeys()
        self.__enableMenus()
        self.__enableDlcs()
        self.__enableData()
        self.enabled = True

    def disable(self):
        if not self.enabled:
            return
        self.uninstallXmlKeys()
        self.__disableMenus()
        self.__disableDlcs()
        self.__disableData()
        self.enabled = False

    def loadPriority(self):
        if not self.priority:
            for data in self.files:
                if (priority.has_section(data)):
                    self.setPriority(priority.get(data, 'Priority'))

    def installXmlKeys(self):
        if (self.xmlkeys):
            text = self.__readFile(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/user.settings")
            text = self.__installXmlKeys(text)
            self.__writeFile(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/user.settings", text)
        if (self.hidden):
            text = self.__readFile(getIni(CONTEXT_PATHS, PATHS_MENU) + "/hidden.xml")
            text = self.__installHiddenXmlKeys(text)
            self.__writeFile(getIni(CONTEXT_PATHS, PATHS_MENU) + "/hidden.xml", text)

    def installInputKeys(self, ui):
        text = self.__readFile(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/input.settings")
        text = self.__InstallInputKeys(text, ui)
        self.__writeFile(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/input.settings", text)

    def __InstallInputKeys(self, inputSettingsFile, ui):
        added = 0
        ask = True
        keep = True
        for key in self.inputsettings:
            contextText, contextName, inputSettingsFile = self.__getContext(key, inputSettingsFile)

            foundkeys = self.__findAlreadyExistingSameKeys(contextText, key)

            if not foundkeys:
                added += 1
                inputSettingsFile = self.__installInputKey(contextName, inputSettingsFile, key)
            else:
                shouldInstallKey = True
                for foundkey in foundkeys:
                    if (foundkey == str(key)):
                        shouldInstallKey = False
                        break
                if shouldInstallKey:
                    for foundkey in foundkeys:
                        temp = Key()
                        temp.populate('', foundkey)
                        if (temp.type == key.type and temp.axis == key.axis and temp.duration == key.duration):
                            shouldInstallKey = False
                            if (ask):
                                msg = ui.MessageRebindedKeys(key, temp)
                                if msg == QMessageBox.SaveAll:
                                    shouldInstallKey = True
                                    break
                                elif msg == QMessageBox.Yes:
                                    keep = True
                                elif msg == QMessageBox.No:
                                    keep = False
                                elif msg == QMessageBox.YesToAll:
                                    ask = False
                                    keep = True
                                elif msg == QMessageBox.NoToAll:
                                    ask = False
                                    keep = False
                                else:
                                    keep = True
                            if (not keep):
                                newcontexttext = contextText.replace(foundkey, str(key))
                                inputSettingsFile = inputSettingsFile.replace(contextText, newcontexttext)
                                contextText = newcontexttext
                    if shouldInstallKey:
                        added += 1
                        inputSettingsFile = re.sub("\[" + contextName + "\]\n", "[" + contextName + "]\n" + str(key) + "\n", inputSettingsFile)
        return inputSettingsFile

    def __installInputKey(self, contextName, inputSettingsFile, key):
        inputSettingsFile = re.sub("\[" + contextName + "\]\n", "[" + contextName + "]\n" + str(key) + "\n",
                                   inputSettingsFile)
        return inputSettingsFile

    def __findAlreadyExistingSameKeys(self, contextText, key):
        if (key.duration or key.axis):
            foundkeys = re.findall(".*Action=" + key.action + ",.*", contextText)
        else:
            foundkeys = re.findall(".*Action=" + key.action + "\)", contextText)
        return foundkeys

    def __getContext(self, key, text):
        contextName = key.context[1:-1]
        context = re.search("\[" + contextName + "\]\n(.+\n)+", text)
        if not context:
            text = '[' + contextName + ']\n\n' + text
            contextText = '[' + contextName + ']\n'
        else:
            contextText = str(context.group(0))
        return contextText, contextName, text

    def installUserSettings(self):
        if (self.usersettings):
            text = ''
            with open(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/user.settings", 'r') as userfile:
                text = userfile.read()
            with open(getIni(CONTEXT_PATHS, PATHS_SETTINGS) + "/user.settings", 'w') as userfile:
                text = self.usersettings[0] + "\n" + text
                userfile.write(text)

    def uninstallXmlKeys(self):
        if (self.xmlkeys):
            text = ''
            null = self.__readFile(text)
            for xml in self.xmlkeys:
                if xml in text:
                    text = text.replace(xml + "\n", '')
            self.__writeFile(text)
        if (self.hidden):
            text = ''
            with open(getIni(CONTEXT_PATHS, PATHS_MENU) + "/hidden.xml", 'r') as userfile:
                text = userfile.read()
            for xml in self.hidden:
                if xml in text:
                    text = text.replace(xml + "\n", '')
            with open(getIni(CONTEXT_PATHS, PATHS_MENU) + "/hidden.xml", 'w') as userfile:
                text = userfile.write(text)

    def __str__(self):
        string = "NAME: " + str(self.name) + "\nENABLED: " + str(
            self.enabled) + "\nPRIORITY: " + self.getPriority() + "\n"
        if (self.files):
            string += "\nDATA:\n"
            for file in self.files:
                string += file + "\n"
        if (self.dlcs):
            string += "\nDLC:\n"
            for dlc in self.dlcs:
                string += dlc + "\n"
        if (self.menus):
            string += "\nMENUS:\n"
            for menu in self.menus:
                string += menu + "\n"
        if (self.xmlkeys):
            string += "\nXML VARIABLES:\n"
            for xml in self.xmlkeys:
                string += xml + "\n"
        if (self.hidden):
            string += "\nHIDDEN XML:\n"
            for xml in self.hidden:
                string += xml + "\n"
        if (self.inputsettings):
            string += "\nINPUT KEYS:\n"
            context = ''
            for key in self.inputsettings:
                if (key.context != context):
                    if (context != ''):
                        string += '\n'
                    context = key.context
                    string += context + '\n'
                string += str(key) + "\n"

        if (self.usersettings):
            string += "\nUSER SETTINGS:\n"
            string += self.usersettings[0] + "\n"
        return string

    def __removeExtension(self, name):
        if (re.search(".*\.(zip|rar)$", name)):
            name = name[:-4]
        elif (re.search(".*\.7z$", name)):
            name = name[:-3]
        return name

    def __removeVersion(self, name):
        lenght = len(name)
        for match in re.finditer(r"-[0-9]+-.+", name):
            lenght = match.span()[0]
        name = name[0:lenght]
        return name

    def __removeLeadingModWord(self, name):
        if (re.match("^mod.*", name)):
            name = name[3:]
        return name

    def __disableData(self):
        for data in self.files:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_MODS) + "/" + data):
                os.rename(getIni(CONTEXT_PATHS, PATHS_MODS) + "/" + data,
                          getIni(CONTEXT_PATHS, PATHS_MODS) + "/~" + data)

    def __disableDlcs(self):
        for dlc in self.dlcs:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_DLCS) + "/" + dlc):
                for subdir, drs, fls in os.walk(getIni(CONTEXT_PATHS, PATHS_DLCS) + "/" + dlc):
                    for file in fls:
                        os.rename(path.join(subdir, file), path.join(subdir, file) + ".disabled")

    def __disableMenus(self):
        for menu in self.menus:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu):
                os.rename(getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu,
                          getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu + ".disabled")

    def __enableData(self):
        for data in self.files:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_MODS) + "/~" + data):
                os.rename(getIni(CONTEXT_PATHS, PATHS_MODS) + "/~" + data,
                          getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + data)

    def __enableDlcs(self):
        for dlc in self.dlcs:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_DLCS) + "/" + dlc):
                for subdir, drs, fls in os.walk(getIni(CONTEXT_PATHS, PATHS_DLCS) + "/" + dlc):
                    for file in fls:
                        if path.exists(subdir + "/" + file):
                            os.rename(subdir + "/" + file, subdir + "/" + file[:-9])

    def __enableMenus(self):
        for menu in self.menus:
            if path.exists(getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu + ".disabled"):
                os.rename(getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu + ".disabled",
                          getIni(CONTEXT_PATHS, PATHS_MENU) + "/" + menu)

    def __installHiddenXmlKeys(self, text):
        for xml in self.hidden:
            if (not xml in text):
                text = text.replace('</VisibleVars>', xml + '\n</VisibleVars>')
        return text

    def __writeFile(self, filename, text):
        with open(filename, 'w') as file:
            file.write(text)

    def __installXmlKeys(self, text):
        for xml in self.xmlkeys:
            if (not xml in text):
                text = text.replace('<!-- [BASE_CharacterMovement] -->',
                                    xml + '\n<!-- [BASE_CharacterMovement] -->')
        return text

    def __readFile(self, filename):
        with open(filename, 'r') as file:
            return file.read()


class Key(object):

    def __init__(self, *args):
        self.context = ''
        self.key = ''
        self.action = ''
        self.duration = ''
        self.axis = ''
        self.type = ''

    def populate(self, context, key):
        self.context = context
        self.key, action = key.split('=(')
        if ("Pad" in self.key):
            self.type = 'controller'
        elif ('PS4' in self.key):
            self.type = 'PS4'
        else:
            self.type = 'keyboard'
        action = action[:-1]
        values = action.split(',')
        self.action = values[0][7:]
        if (len(values) > 1):
            if ("Axis" in values[1]):
                self.axis = values[2][6:]
            elif ("Duration" in values[1]):
                self.duration = values[2][9:]

    def __str__(self):
        str = ""
        str += self.key + "=(Action=" + self.action
        if (self.duration or self.axis):
            if (self.duration):
                str += ",State=Duration,IdleTime=" + self.duration
            else:
                str += ",State=Axis,Value=" + self.axis
        str += ")"
        return str
