from src.model.Key import Key
from tests.Witcher3TestCase import Witcher3TestCase


class TestKey(Witcher3TestCase):

    def test_printNoDurationNoAxis(self):
        key = self.__createKeyMoDurationNoAxis()
        self.assertEqual('IK_F1=(Action=myAction)', key.__repr__())

    def test_printWithDuration(self):
        key = self.__createKeyWithDuration()
        self.assertEqual('IK_F1=(Action=myAction,State=Duration,IdleTime=3)', key.__repr__())

    def test_printWithAxis(self):
        key = self.__createKeyWithAxis()
        self.assertEqual('IK_F1=(Action=myAction,State=Axis,Value=0.5)', key.__repr__())

    def test_printWithBothDurationAndAxis(self):
        key = self.__createKeyWIthBothDurationAndAxis()
        self.assertEqual('IK_F1=(Action=myAction,State=Duration,IdleTime=3)', key.__repr__())

    def __createKeyMoDurationNoAxis(self):
        return Key(
            context='TEST',
            key='IK_F1',
            action='myAction')

    def __createKeyWithDuration(self):
        return Key(
            context='TEST',
            key='IK_F1',
            action='myAction',
            duration='3')

    def __createKeyWithAxis(self):
        return Key(
            context='TEST',
            key='IK_F1',
            action='myAction',
            axis='0.5')

    def __createKeyWIthBothDurationAndAxis(self):
        return Key(
            context='TEST',
            key='IK_F1',
            action='myAction',
            duration='3',
            axis='0.5')
