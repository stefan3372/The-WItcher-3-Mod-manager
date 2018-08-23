import os
import subprocess
import unittest
import Configuration

TEST_CONFIG_FILE = 'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Documents/The Witcher 3 Mod Manager/config.ini'
TEST_PRIORITY_FILE = 'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Documents/The Witcher 3/mods.settings'


class Witcher3TestCase(unittest.TestCase):

    def setUp(self):
        self.__resetData()
        self.__setUpPaths()

    def __resetData(self):
        with open(os.devnull, 'w') as FNULL:
            subprocess.call(['resetData.bat'], stdout=FNULL)

    def __setUpPaths(self):
        Configuration.config = Configuration.Configuration(TEST_CONFIG_FILE)
        Configuration.priority = Configuration.Configuration(TEST_PRIORITY_FILE)
