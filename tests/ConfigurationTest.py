from Configuration import Configuration
from tests.Witcher3TestCase import Witcher3TestCase, TEST_CONFIG_FILE


class ConfigurationTest(Witcher3TestCase):

    def setUp(self):
        super().setUp()
        self.config = Configuration(TEST_CONFIG_FILE)

    def test_readConfiguration(self):
        self.assertEqual(
            self.__readFile(TEST_CONFIG_FILE),
            self.config.read()
        )

    def test_get_correctSection_correctOption_returnNumberAsString(self):
        width = self.config.get('WINDOW', 'width')
        self.assertEqual('1024', width)

    def test_get_correctSction_correctOption_returnPathAsString(self):
        path = self.config.get('PATHS', 'mod')
        self.assertEqual('C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Witcher 3/mods', path)

    def test_get_correctSection_wrongOption_emptyResult(self):
        language = self.config.get('WINDOW', 'language')
        self.assertEqual('', language)

    def test_get_wrongSection_wrongOptinon_emptyResult(self):
        language = self.config.get('LANGUAGE', 'lanugage')
        self.assertEqual('', language)

    def test_set_correctSection_correctOption_setNumber(self):
        self.config.set('WINDOW', 'width', '100')
        width = self.config.get('WINDOW', 'width')
        self.assertEqual('100', width)

    def test_set_correctSection_correctOption_setPath(self):
        self.config.set('PATHS', 'mod', 'C:/something/test')
        path = self.config.get('PATHS', 'mod')
        self.assertEqual('C:/something/test', path)

    def test_set_correctSection_notExistingOption(self):
        self.config.set('WINDOW', 'language', 'english')
        language = self.config.get('WINDOW', 'language')
        self.assertEqual('english', language)

    def test_set_notExistingSection_notExistionOption(self):
        self.config.set('TEST', 'test', '123')
        test = self.config.get('TEST', 'test')
        self.assertEqual('123', test)

    def test_getOptions_correctSection(self):
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'menu', 'settings', 'scriptmerger'], options)

    def test_getOptions_wrongSection(self):
        options = self.config.getOptions('SOMETHING')
        self.assertEqual([], options)

    def test_setNoValue_correctSection_correctOption(self):
        self.config.setNoValue('PATHS', 'test')
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'menu', 'settings', 'scriptmerger', 'test'], options)

    def test_setNoValue_correctSection_existingOption(self):
        self.config.setNoValue('PATHS', 'mod')
        value = self.config.get('PATHS', 'mod')
        self.assertEqual(None, value)

    def test_setNoValue_wrongSection_wrongOption(self):
        self.config.setNoValue('TEST', 'test')
        value = self.config.get('TEST', 'test')
        self.assertEqual(None, value)

    def test_removeOption_correctSection_correctOption_noValue(self):
        self.config.setNoValue('PATHS', 'test')
        self.config.removeOption('PATHS', 'test')
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'menu', 'settings', 'scriptmerger'], options)

    def test_removeOption_correctSection_correctOption_emptyValue(self):
        self.config.removeOption('PATHS', 'scriptmerger')
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'menu', 'settings'], options)

    def test_removeOption_correctSection_correctOption_withValue(self):
        self.config.removeOption('PATHS', 'menu')
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'settings', 'scriptmerger'], options)

    def test_removeOption_correctSection_wrongOption(self):
        self.config.removeOption('PATHS', 'test')
        options = self.config.getOptions('PATHS')
        self.assertEqual(['gamepath', 'mod', 'dlc', 'menu', 'settings', 'scriptmerger'], options)

    def test_removeOption_wrongSection_wrongOption(self):
        self.config.removeOption('TEST', 'test')
        self.test_readConfiguration()

    def test_write(self):
        self.config.set('TEST', 'test', 'test')
        self.config.write()
        file = self.__readFile(TEST_CONFIG_FILE)
        self.assertIn("[TEST]\ntest = test", file)

    def __readFile(self, url):
        with open(url, 'r') as file:
            return file.read()