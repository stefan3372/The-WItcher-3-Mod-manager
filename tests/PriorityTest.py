from config.Configuration import Priority
from tests.Witcher3TestCase import Witcher3TestCase, TEST_PRIORITY_FILE


class PriorityTest(Witcher3TestCase):

    def setUp(self):
        super().setUp()
        self.priority = Priority(TEST_PRIORITY_FILE)

    def test_get_priority(self):
        value = self.priority.get('modTest1')
        self.assertEqual('3', value)

    def test_get_wrongSection_none(self):
        value = self.priority.get('modTest4')
        self.assertEqual(None, value)

    def test_set_priority(self):
        self.priority.set('modTest1', '7')
        value = self.priority.get('modTest1')
        self.assertEqual('7', value)

    def test_set_priority_wrongSection(self):
        self.priority.set('modTest4', '7')
        value = self.priority.get('modTest4')
        self.assertEqual('7', value)
