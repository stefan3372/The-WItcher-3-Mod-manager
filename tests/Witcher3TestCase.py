import os
import subprocess
import unittest
from src.config.Configuration import Configuration
from src import config

TEST_DOCUMENTS = 'C:/Projects/The-WItcher-3-Mod-manager/tests/MockData/GameData/Documents'

class Witcher3TestCase(unittest.TestCase):

    def setUp(self):
        self.__resetData()
        self.__setUpPaths()

    def __resetData(self):
        with open(os.devnull, 'w') as FNULL:
            subprocess.call(['C:\\Projects\\The-WItcher-3-Mod-manager\\tests\\resetData.bat'], stdout=FNULL)

    def __setUpPaths(self):
        config.data = Configuration(TEST_DOCUMENTS)
