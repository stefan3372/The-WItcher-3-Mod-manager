from src.model.Key import Key
from tests.Witcher3TestCase import Witcher3TestCase


class TestKey(Witcher3TestCase):

    def test_parseKeyNoAditionalData(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction)')
        self.assertEqual('[TEST]', key.context)
        self.assertEqual('IK_F1', key.key)
        self.assertEqual('myAction', key.action)
        self.assertEqual('keyboard', key.type)

    def test_parseWithDuration(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction,State=Duration,IdleTime=3)')
        self.assertEqual('[TEST]', key.context)
        self.assertEqual('IK_F1', key.key)
        self.assertEqual('myAction', key.action)
        self.assertEqual('3', key.duration)
        self.assertEqual('keyboard', key.type)

    def test_parseWithAxis(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction,State=Axis,Value=0.5)')
        self.assertEqual('[TEST]', key.context)
        self.assertEqual('IK_F1', key.key)
        self.assertEqual('myAction', key.action)
        self.assertEqual('0.5', key.axis)
        self.assertEqual('keyboard', key.type)

    def test_parseControllerKey(self):
        key = Key('[TEST]', 'Pad_Up=(Action=myAction)')
        self.assertEqual('[TEST]', key.context)
        self.assertEqual('Pad_Up', key.key)
        self.assertEqual('myAction', key.action)
        self.assertEqual('controller', key.type)

    def test_parsePS4Key(self):
        key = Key('[TEST]', 'PS4_Up=(Action=myAction)')
        self.assertEqual('[TEST]', key.context)
        self.assertEqual('PS4_Up', key.key)
        self.assertEqual('myAction', key.action)
        self.assertEqual('PS4', key.type)

    def test_printNoDurationNoAxis(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction)')
        self.assertEqual('IK_F1=(Action=myAction)', key.__repr__())

    def test_printWithDuration(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction,State=Duration,IdleTime=3)')
        self.assertEqual('IK_F1=(Action=myAction,State=Duration,IdleTime=3)', key.__repr__())

    def test_printWithAxis(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction,State=Axis,Value=0.5)')
        self.assertEqual('IK_F1=(Action=myAction,State=Axis,Value=0.5)', key.__repr__())

    def test_printWithBothDurationAndAxis(self):
        key = Key('[TEST]', 'IK_F1=(Action=myAction,State=Duration,IdleTime=3)')
        self.assertEqual('IK_F1=(Action=myAction,State=Duration,IdleTime=3)', key.__repr__())
