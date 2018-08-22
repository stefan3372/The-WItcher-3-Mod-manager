import configparser
import ctypes.wintypes

config = configparser.ConfigParser(allow_no_value=True, delimiters='=')
priority = configparser.ConfigParser(allow_no_value=True, delimiters='=')
priority.optionxform = str
buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, 5, None, 0, buf)
documents = str(buf.value).replace('\\', '/')

CONFIG_FILE = documents + '/The Witcher 3 Mod Manager/config.ini'
PRIORITY_FILE = documents + '/The Witcher 3/mods.settings'

CONTEXT_WINDOW = 'WINDOW'
WINDOW_SECTION0 = 'section0'
WINDOW_SECTION1 = 'section1'
WINDOW_SECTION2 = 'section2'
WINDOW_SECTION3 = 'section3'
WINDOW_SECTION4 = 'section4'
WINDOW_SECTION5 = 'section5'
WINDOW_SECTION6 = 'section6'
WINDOW_SECTION7 = 'section7'
WINDOW_SECTION8 = 'section8'
WINDOW_SECTION9 = 'section9'
WINDOW_SECTION10 = 'section10'
WINDOW_SECTION11 = 'section11'
WINDOW_HEIGHT = 'height'
WINDOW_WIDTH = 'width'
CONTEXT_PATHS = 'PATHS'
PATHS_GAME = 'gamepath'
PATHS_MODS = 'mod'
PATHS_DLCS = 'dlc'
PATHS_MENU = 'menu'
PATHS_SETTINGS = 'settings'
PATHS_SCRIPT_MERGER = 'scriptmerger'
PATHS_LAST = 'lastpath'
CONTEXT_SETTINGS = 'SETTINGS'
SETTINGS_ALLOW_POPUP = 'allowpopups'
SETTINGS_LANGUAGE = 'language'


def saveWindowSettings(ui, window):
    setIni(CONTEXT_WINDOW, WINDOW_WIDTH, str(window.width()))
    setIni(CONTEXT_WINDOW, WINDOW_HEIGHT, str(window.height()))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION0, str(ui.treeWidget.header().sectionSize(0)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION1, str(ui.treeWidget.header().sectionSize(1)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION2, str(ui.treeWidget.header().sectionSize(2)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION3, str(ui.treeWidget.header().sectionSize(3)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION4, str(ui.treeWidget.header().sectionSize(4)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION5, str(ui.treeWidget.header().sectionSize(5)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION6, str(ui.treeWidget.header().sectionSize(6)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION7, str(ui.treeWidget.header().sectionSize(7)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION8, str(ui.treeWidget.header().sectionSize(8)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION9, str(ui.treeWidget.header().sectionSize(9)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION10, str(ui.treeWidget.header().sectionSize(10)))
    setIni(CONTEXT_WINDOW, WINDOW_SECTION11, str(ui.treeWidget.header().sectionSize(11)))


def initConfig():
    config.read(CONFIG_FILE)
    priority.read(PRIORITY_FILE)


def getIni(section, option):
    if config.has_option(section, option):
        return config.get(section, option)
    else:
        return ""


def setPriority(modfile, value):
    if not priority.has_section(modfile):
        priority.add_section(modfile)
        priority.set(modfile, 'Enabled', '1')
    priority.set(modfile, 'Priority', value)


def setIni(section, option, value):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    iniWrite()


def setIniNoValue(section, value):
    config.set(section, value)
    iniWrite()


def getIniNoValue(section):
    list = []
    for value in config.items(section):
        list.append(value[0])
    return list


def removeIniNoValue(section, value):
    if config.has_section(section):
        config.remove_option(section, value)
    iniWrite()


def iniWrite():
    with open(CONFIG_FILE, 'w') as configfile:
        config.write(configfile)


def getPriority(modfile):
    if (modfile in priority.sections()):
        return priority[modfile]['Priority']
    else:
        return None


def priorityWrite():
    with open(PRIORITY_FILE, 'w') as configfile:
        priority.write(configfile)
    text = priorityRead()
    removeExtraSpaces(text)


def removeExtraSpaces(text):
    with open(PRIORITY_FILE, 'w') as configfile:
        text = text.replace(' = ', '=')
        configfile.write(text)


def priorityRead():
    with open(PRIORITY_FILE, 'r') as configfile:
        text = configfile.read()
    return text
