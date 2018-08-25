from src import config
from tests.Witcher3TestCase import Witcher3TestCase, TEST_DOCUMENTS


class ConfigurationTest(Witcher3TestCase):

    def test_readConfiguration(self):
        self.assertEqual(
            self.__readFile(TEST_DOCUMENTS + "/The Witcher 3 Mod Manager/config.ini"),
            config.data.read())

    def test_get_correctSection_correctOption_returnNumberAsString(self):
        width = config.data.get('WINDOW', 'width')
        self.assertEqual('1024', width)

    def test_get_mods(self):
        path = config.data.mods
        self.assertEqual('C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Witcher 3/mods', path)

    def test_get_menus(self):
        path = config.data.menu
        self.assertEqual(
            'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Witcher 3/bin/config/r4game/user_config_matrix/pc',
            path)

    def test_get_dlc(self):
        path = config.data.dlc
        self.assertEqual('C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Witcher 3/dlc', path)

    def test_get_scriptmerger(self):
        path = config.data.scriptmerger
        self.assertEqual('C:/Projects/The-WItcher-3-Mod-manager/scriptmerger.exe', path)

    def test_get_game(self):
        path = config.data.game
        self.assertEqual('C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Witcher 3', path)

    def test_get_settings(self):
        path = config.data.settings
        self.assertEqual(TEST_DOCUMENTS + "/The Witcher 3", path)

    def test_get_configuration(self):
        path = config.data.configuration
        self.assertEqual(TEST_DOCUMENTS + "/The Witcher 3 Mod Manager", path)

    def test_get_correctSection_wrongOption_emptyResult(self):
        language = config.data.get('WINDOW', 'language')
        self.assertEqual('', language)

    def test_get_wrongSection_wrongOptinon_emptyResult(self):
        language = config.data.get('LANGUAGE', 'lanugage')
        self.assertEqual('', language)

    def test_set_correctSection_correctOption_setNumber(self):
        config.data.set('WINDOW', 'width', '100')
        width = config.data.get('WINDOW', 'width')
        self.assertEqual('100', width)

    def test_set_correctSection_correctOption_setPath(self):
        config.data.set('PATHS', 'mod', 'C:/something/test')
        path = config.data.get('PATHS', 'mod')
        self.assertEqual('C:/something/test', path)

    def test_set_correctSection_notExistingOption(self):
        config.data.set('WINDOW', 'language', 'english')
        language = config.data.get('WINDOW', 'language')
        self.assertEqual('english', language)

    def test_set_notExistingSection_notExistionOption(self):
        config.data.set('TEST', 'test', '123')
        test = config.data.get('TEST', 'test')
        self.assertEqual('123', test)

    def test_getOptions_correctSection(self):
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game', 'scriptmerger'], options)

    def test_getOptions_wrongSection(self):
        options = config.data.getOptions('SOMETHING')
        self.assertEqual([], options)

    def test_setNoValue_correctSection_correctOption(self):
        config.data.setOption('PATHS', 'test')
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game', 'scriptmerger', 'test'], options)

    def test_setNoValue_correctSection_existingOption(self):
        config.data.setOption('PATHS', 'mod')
        value = config.data.get('PATHS', 'mod')
        self.assertEqual(None, value)

    def test_setNoValue_wrongSection_wrongOption(self):
        config.data.setOption('TEST', 'test')
        value = config.data.get('TEST', 'test')
        self.assertEqual(None, value)

    def test_removeOption_correctSection_correctOption_noValue(self):
        config.data.setOption('PATHS', 'test')
        config.data.removeOption('PATHS', 'test')
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game', 'scriptmerger'], options)

    def test_removeOption_correctSection_correctOption_emptyValue(self):
        config.data.removeOption('PATHS', 'scriptmerger')
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game'], options)

    def test_removeOption_correctSection_correctOption_withValue(self):
        config.data.removeOption('PATHS', 'menu')
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game', 'scriptmerger'], options)

    def test_removeOption_correctSection_wrongOption(self):
        config.data.removeOption('PATHS', 'test')
        options = config.data.getOptions('PATHS')
        self.assertEqual(['game', 'scriptmerger'], options)

    def test_removeOption_wrongSection_wrongOption(self):
        config.data.removeOption('TEST', 'test')
        self.test_readConfiguration()

    def test_write(self):
        config.data.set('TEST', 'test', 'test')
        config.data.write()
        file = self.__readFile(TEST_DOCUMENTS + "/The Witcher 3 Mod Manager/config.ini")
        self.assertIn("[TEST]\ntest = test", file)

    def test_get_priority(self):
        value = config.data.getPriority('modTest1')
        self.assertEqual('3', value)

    def test_get_wrongSection_none(self):
        value = config.data.getPriority('modTest4')
        self.assertEqual(None, value)

    def test_set_priority(self):
        config.data.setPriority('modTest1', '7')
        value = config.data.getPriority('modTest1')
        self.assertEqual('7', value)

    def test_set_priority_wrongSection(self):
        config.data.setPriority('modTest4', '7')
        value = config.data.getPriority('modTest4')
        self.assertEqual('7', value)

    def test_get_getAllowPopups(self):
        value = config.data.allowpopups
        self.assertEqual("1", value)

    def test_set_getAllowPopups(self):
        config.data.allowpopups = "0"
        value = config.data.allowpopups
        self.assertEqual("0", value)

    def test_get_language(self):
        value = config.data.language
        self.assertEqual("English.qm", value)

    def test_set_language(self):
        config.data.allowpopups = "Srpski.qm"
        value = config.data.allowpopups
        self.assertEqual("Srpski.qm", value)

    def test_setDefaultWindow(self):
        config.data.setDefaultWindow()
        self.assertEqual(config.data.get('WINDOW', 'width'), '1024')
        self.assertEqual(config.data.get('WINDOW', 'height'), '720')
        self.assertEqual(config.data.get('WINDOW', 'section0'), '60')
        self.assertEqual(config.data.get('WINDOW', 'section1'), '200')
        self.assertEqual(config.data.get('WINDOW', 'section2'), '50')
        self.assertEqual(config.data.get('WINDOW', 'section3'), '39')
        self.assertEqual(config.data.get('WINDOW', 'section4'), '39')
        self.assertEqual(config.data.get('WINDOW', 'section5'), '39')
        self.assertEqual(config.data.get('WINDOW', 'section6'), '39')
        self.assertEqual(config.data.get('WINDOW', 'section7'), '45')
        self.assertEqual(config.data.get('WINDOW', 'section8'), '39')
        self.assertEqual(config.data.get('WINDOW', 'section9'), '50')
        self.assertEqual(config.data.get('WINDOW', 'section10'), '45')
        self.assertEqual(config.data.get('WINDOW', 'section11'), '120')

    def __readFile(self, url):
        with open(url, 'r') as file:
            return file.read()
