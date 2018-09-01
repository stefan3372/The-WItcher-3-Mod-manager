from src.core.Fetcher import Fetcher
from src.domain.Mod import Mod
from tests.Witcher3TestCase import Witcher3TestCase

TEST_DATA = 'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/TestData'


class FetcherTest(Witcher3TestCase):

    fetcher : Fetcher

    def setUp(self):
        super().setUp()
        self.fetcher = Fetcher()

    def test_IsArchive_correctData(self):
        param_list = ["anything.zip", "anything.rar", "anything.7z", "C:/Program Files/archive.rar"]
        for param in param_list:
            with self.subTest():
                self.assertTrue(self.fetcher.isArchive(param))

    def test_IsArchive_wrongData(self):
        param_list = ["anything.zi", "anything.jpg", ".7z", "C:/Program Files/archive", '']
        for param in param_list:
            with self.subTest():
                self.assertFalse(self.fetcher.isArchive(param))

    def test_IsValidModFolder_correctFolders(self):
        param_list = ["/modValidMod", "/ValidMod"]
        for param in param_list:
            with self.subTest():
                self.assertTrue(self.fetcher.isValidModFolder(TEST_DATA + param))

    def test_IsValidModFolder_wrongFolders(self):
        param_list = ["/../GameData", "/modInvalidMod", "/modValidMod/content", "notExistingFolder", "randomFolder"]
        for param in param_list:
            with self.subTest():
                self.assertFalse(self.fetcher.isValidModFolder(TEST_DATA + param))

    def test_IsMenuFile_correctFiles(self):
        param_list = ["anything.xml", "mod.xml", "file.xml", "zinput.xml"]
        for param in param_list:
            with self.subTest():
                self.assertTrue(self.fetcher.isMenuXmlFile(param))

    def test_IsMenuFile_incorrectFiles(self):
        param_list = [".xml", "", "picture.jpg", "input.xml", "hidden.xm", "file"]
        for param in param_list:
            with self.subTest():
                self.assertFalse(self.fetcher.isMenuXmlFile(param))

    def test_IsTxtOrInputXmlFile_correctFiles(self):
        param_list = ["input.xml", "mod.txt"]
        for param in param_list:
            with self.subTest():
                self.assertTrue(self.fetcher.isTxtOrInputXmlFile(param))

    def test_IsTxtOrInputXmlFile_incorrectFiles(self):
        param_list = ["nothing.xml", "mod.jpg", ".xml", ".txt", "file"]
        for param in param_list:
            with self.subTest():
                self.assertFalse(self.fetcher.isTxtOrInputXmlFile(param))

    def test_RemoveMultiWhiteSpace(self):
        param_list = ["t e s t", "t    e s   t", "t  \te  \n  s  t", "t\n\ne\t\ts\n\tt", "t      e        s      t"]
        for param in param_list:
            with self.subTest():
                self.assertEqual('t e s t', self.fetcher.removeMultiWhiteSpace(param))

    def test_RemoveXmlComments(self):
        val = "<xml><!-- comment --></xml>"
        result = self.fetcher.removeXmlComments(val)
        self.assertEqual("<xml></xml>", result)

    def test_RemoveXmlComments_multiLineComment(self):
        val = "<xml><!-- comment\nsecond line comment --></xml>"
        result = self.fetcher.removeXmlComments(val)
        self.assertEqual("<xml></xml>", result)

    def test_RemoveXmlComments_multipleComments(self):
        val = "<!-- 1 comment --><xml><!-- 2 comment --></xml><!-- 3 comment -->"
        result = self.fetcher.removeXmlComments(val)
        self.assertEqual("<xml></xml>", result)

    def test_RemoveXmlComments_multipleMultiLineComments(self):
        val = "<!-- 1 comment -->\n<xml><!-- 2 comment -->\n</xml><!-- 3 comment -->"
        result = self.fetcher.removeXmlComments(val)
        self.assertEqual("\n<xml>\n</xml>", result)

    def test_fetchDataFromRelevantFolders_correctStructure(self):
        mod = Mod()
