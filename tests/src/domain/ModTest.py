from src.domain.Key import Key
from src.domain.Mod import Mod
from tests.Witcher3TestCase import Witcher3TestCase


class TestMod(Witcher3TestCase):

    def setUp(self):
        super().setUp()
        self.mod = self.__createMod()

    def test_setName_regular(self):
        self.mod.name = "Test"
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWord(self):
        self.mod.name = "modTest"
        self.assertEqual("Test", self.mod.name)

    def test_setName_version(self):
        self.mod.name = "testfile-2608-v4-0-u1"
        self.assertEqual("testfile", self.mod.name)

    def test_setName_zipExtension(self):
        self.mod.name = "testfile.zip"
        self.assertEqual("testfile", self.mod.name)

    def test_setName_rarExtension(self):
        self.mod.name = "testfile.rar"
        self.assertEqual("testfile", self.mod.name)

    def test_setName_7zExtension(self):
        self.mod.name = "testfile.7z"
        self.assertEqual("testfile", self.mod.name)

    def test_setName_modWordAndVersion(self):
        self.mod.name = "modTest-2608-v4-0-u1"
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWordAndExtension(self):
        self.mod.name = "modTest.zip"
        self.assertEqual("Test", self.mod.name)

    def test_setName_extensionAndVersion(self):
        self.mod.name = "Test-2608-v4-0-u1.zip"
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWordAndExtensionAndVersion(self):
        self.mod.name = "modTest-2608-v4-0-u1.zip"
        self.assertEqual("Test", self.mod.name)

    def test_getPriority_NoPrioritySet(self):
        self.assertEqual("-", self.mod.priority)

    def test_getPriority_PriorityHasBeenSet(self):
        self.mod._priority = '3'
        self.assertEqual("3", self.mod.priority)

    def test_setPriority(self):
        self.mod.priority = "3"
        self.assertEqual('3', self.mod.priority)

    def test_setPriority_wrongInput(self):
        try:
            self.mod.priority = "sdfdjsfk"
            self.fail()
        except:
            pass

    def __createMod(self):
        return Mod(
            _name='testmod',
            files=['modTest1', 'modTest2', 'modTest3'],
            dlcs=['dlcTest1', 'dlcTest2'],
            menus=['textmod.xml', 'configtest.xml'],
            usersettings='[modTest]\nfmedMaxHoursPerMinute=60\nfmedHoursPerMinutePerSecond=10\nfmedUseTimescale=false\nfmedSpawnCampfire=false\nfmedDoNotDespawnCampfire=false\nfmedHotkeyBehavior=0\n',
            xmlkeys=[
                '< Var builder = "Input" id = "TestAction" displayName = "TestAction0" displayType = "INPUTPC" actions = "TestAction" / >',
                '< Var builder = "Input" id = "TestAction" displayName = "TestAction1" displayType = "INPUTPC" actions = "TestAction" / >',
                '< Var builder = "Input" id = "TestAction" displayName = "TestAction2" displayType = "INPUTPC" actions = "TestAction" / >',
                '< Var builder = "Input" id = "TestAction" displayName = "TestAction3" displayType = "INPUTPC" actions = "TestAction" / >',
                '< Var builder = "Input" id = "TestAction" displayName = "TestAction4" displayType = "INPUTPC" actions = "TestAction" / >'],
            hiddenkeys=[
                '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
                '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
                '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
                '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
                '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />'],
            inputsettings=[
                Key('TEST', 'IK_F0', 'Action0', '1', '', 'keyboard'),
                Key('TEST', 'IK_F1', 'Action1', '1', '', 'keyboard'),
                Key('TEST', 'IK_F2', 'Action2', '1', '', 'keyboard'),
                Key('TEST', 'IK_F3', 'Action3', '1', '', 'keyboard'),
                Key('TEST', 'IK_F4', 'Action4', '1', '', 'keyboard'),
                Key('TEST', 'IK_F5', 'Action5', '1', '', 'keyboard'),
                Key('TEST', 'IK_F6', 'Action6', '1', '', 'keyboard'),
                Key('TEST', 'IK_F7', 'Action7', '1', '', 'keyboard'),
                Key('TEST', 'IK_F8', 'Action8', '1', '', 'keyboard'),
                Key('TEST', 'IK_F9', 'Action9', '1', '', 'keyboard')
            ]
        )
