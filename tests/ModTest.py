from model.Mod import Mod
from model.Key import Key
from tests.Witcher3TestCase import Witcher3TestCase


class TestModClass(Witcher3TestCase):

    def setUp(self):
        super().setUp()
        self.__createMod()

    def test_setName_regular(self):
        self.mod.setName("Test")
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWord(self):
        self.mod.setName("modTest")
        self.assertEqual("Test", self.mod.name)

    def test_setName_version(self):
        self.mod.setName("test-2608-v4-0-u1")
        self.assertEqual("test", self.mod.name)

    def test_setName_zipExtension(self):
        self.mod.setName("test.zip")
        self.assertEqual("test", self.mod.name)

    def test_setName_rarExtension(self):
        self.mod.setName("test.rar")
        self.assertEqual("test", self.mod.name)

    def test_setName_7zExtension(self):
        self.mod.setName("test.7z")
        self.assertEqual("test", self.mod.name)

    def test_setName_modWordAndVersion(self):
        self.mod.setName("modTest-2608-v4-0-u1")
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWordAndExtension(self):
        self.mod.setName("modTest.zip")
        self.assertEqual("Test", self.mod.name)

    def test_setName_extensionAndVersion(self):
        self.mod.setName("Test-2608-v4-0-u1.zip")
        self.assertEqual("Test", self.mod.name)

    def test_setName_modWordAndExtensionAndVersion(self):
        self.mod.setName("modTest-2608-v4-0-u1.zip")
        self.assertEqual("Test", self.mod.name)

    def test_getPriority_NoPrioritySet(self):
        self.assertEqual("-", self.mod.getPriority())

    def test_getPriority_PriorityHasBeenSet(self):
        self.mod.priority = '3'
        self.assertEqual("3", self.mod.getPriority())

    def test_setPriority(self):
        self.mod.setPriority("3")
        self.assertEqual('3', self.mod.getPriority())

    def test_setPriority_wrongInput(self):
        try:
            self.mod.setPriority("sdfdjsfk")
            self.fail()
        except:
            pass

    def test_disable(self):
        pass

    def test_enable(self):
        pass

    def load_priority(self):
        pass

    def __createMod(self):
        self.mod = Mod()
        self.mod.name = 'testmod'
        self.mod.files = ['modTest1', 'modTest2', 'modTest3']
        self.mod.dlcs = ['dlcTest1', 'dlcTest2']
        self.mod.menus = ['textmod.xml', 'configtest.xml']
        for i in range(0, 10):
            key = Key()
            key.context = '[TESTCONTEXT]'
            key.key = 'IK_F' + str(i)
            key.action = 'TESTACTION' + str(i)
            key.duration = '1'
            key.axis = ''
            key.type = 'keyboard'
            self.mod.inputsettings.append(key)
        self.mod.usersettings = [
            '[modTest]\nfmedMaxHoursPerMinute=60\nfmedHoursPerMinutePerSecond=10\nfmedUseTimescale=false\nfmedSpawnCampfire=false\nfmedDoNotDespawnCampfire=false\nfmedHotkeyBehavior=0\n']
        self.mod.xmlkeys = [
            '< Var builder = "Input" id = "TestAction" displayName = "TestAction" displayType = "INPUTPC" actions = "TestAction" / >',
            '< Var builder = "Input" id = "TestAction" displayName = "TestAction" displayType = "INPUTPC" actions = "TestAction" / >',
            '< Var builder = "Input" id = "TestAction" displayName = "TestAction" displayType = "INPUTPC" actions = "TestAction" / >',
            '< Var builder = "Input" id = "TestAction" displayName = "TestAction" displayType = "INPUTPC" actions = "TestAction" / >',
            '< Var builder = "Input" id = "TestAction" displayName = "TestAction" displayType = "INPUTPC" actions = "TestAction" / >'        ]
        self.mod.hidden = [
            '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
            '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
            '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
            '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />',
            '<Var builder="Input" id="Test" displayName="Test" displayType="INPUTPC" actions="Test" />'        ]
