import config
from tests.Witcher3TestCase import Witcher3TestCase, TEST_DOCUMENTS


class ConfigurationTest(Witcher3TestCase):

    def test_readConfiguration(self):
        self.assertEqual(
            self.__readFile(TEST_DOCUMENTS + "/The Witcher 3 Mod Manager/config.ini"),
            config.data.read()
        )

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

    def __readFile(self, url):
        with open(url, 'r') as file:
            return file.read()
