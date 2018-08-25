import os
import subprocess
import unittest
from config.Configuration import Configuration
import config

TEST_DOCUMENTS = 'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Documents'

class Witcher3TestCase(unittest.TestCase):

    def setUp(self):
        self.__resetData()
        self.__setUpPaths()

    def __resetData(self):
        with open(os.devnull, 'w') as FNULL:
            subprocess.call(['resetData.bat'], stdout=FNULL)

    def __setUpPaths(self):
        config.data = Configuration(TEST_DOCUMENTS)
