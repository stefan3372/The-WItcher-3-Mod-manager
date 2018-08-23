import configparser
import ctypes.wintypes

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


class Configuration:
    url = None
    config = None

    def __init__(self, url):
        self.url = url
        self.config = configparser.ConfigParser(allow_no_value=True, delimiters='=')
        self.config.read(url)

    def write(self, space_around_delimiters=True):
        with open(self.url, 'w') as file:
            self.config.write(file, space_around_delimiters)

    def read(self):
        with open(self.url, 'r') as file:
            return file.read()

    def get(self, section, option):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            return ""

    def set(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        self.write()

    def setNoValue(self, section, option):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option)
        self.write()

    def getOptions(self, section):
        if self.config.has_section(section):
            return list(map(lambda x: x[0], self.config.items(section)))
        else:
            return []

    def removeOption(self, section, value):
        if self.config.has_section(section):
            self.config.remove_option(section, value)
        self.write()


class PriorityConfiguration(Configuration):

    def __init__(self, url):
        super().__init__(url)
        self.config.optionxform = str

    def set(self, section, option, value=None):
        if not self.config.has_section(section):
            self.config.add_section(section)
            self.config.set(section, 'enabled', '1')
        self.config.set(section, 'priority', option)
        self.write()

    def get(self, section, option=None):
        if section in self.config.sections():
            return self.config[section]['priority']
        else:
            return None


# def saveWindowSettings(ui, window):
#     setIni(CONTEXT_WINDOW, WINDOW_WIDTH, str(window.width()))
#     setIni(CONTEXT_WINDOW, WINDOW_HEIGHT, str(window.height()))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION0, str(ui.treeWidget.header().sectionSize(0)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION1, str(ui.treeWidget.header().sectionSize(1)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION2, str(ui.treeWidget.header().sectionSize(2)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION3, str(ui.treeWidget.header().sectionSize(3)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION4, str(ui.treeWidget.header().sectionSize(4)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION5, str(ui.treeWidget.header().sectionSize(5)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION6, str(ui.treeWidget.header().sectionSize(6)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION7, str(ui.treeWidget.header().sectionSize(7)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION8, str(ui.treeWidget.header().sectionSize(8)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION9, str(ui.treeWidget.header().sectionSize(9)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION10, str(ui.treeWidget.header().sectionSize(10)))
#     setIni(CONTEXT_WINDOW, WINDOW_SECTION11, str(ui.treeWidget.header().sectionSize(11)))

config = Configuration(CONFIG_FILE)
priority = PriorityConfiguration(PRIORITY_FILE)
