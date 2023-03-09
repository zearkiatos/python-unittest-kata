import unittest
import datetime
from src.model.Person import Person


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(name="Alejandra", year=25)
        self.person2 = Person(name="Diego", year=22)
        self.person3 = Person(name="Alejandra", year=25)
        self.person4 = Person(name="Diana", year=25)
        self.group = [self.person1, self.person2, self.person3]

    def test_constructor(self):
        self.assertEqual(self.person1.get_name(), 'Alejandra')
        self.assertEqual(self.person1.get_year(), 25)

    def test_birth_year(self):
        self.assertEqual(self.person1.calculate_birth_day(
            True), datetime.datetime.now().year - 25)
        self.assertNotEqual(self.person1.calculate_birth_day(
            False), datetime.datetime.now().year - 25)
        self.assertEqual(self.person1.calculate_birth_day(
            False), datetime.datetime.now().year - 25 + 1)
        self.assertNotEqual(self.person1.calculate_birth_day(
            True), datetime.datetime.now().year - 25 + 1)

    def test_assign(self):
        self.person2.set_year(28)
        self.person2.set_name("Felipe")

        self.assertFalse(self.person2.get_name() == "Diego")
        self.assertFalse(self.person2.get_year() == 22)
        self.assertTrue(self.person2.get_name() == "Felipe")
        self.assertTrue(self.person2.get_year() == 28)

    def test_objects_equals(self):
        new_person = self.person1

        self.assertIsNot(self.person1, self.person3)
        self.assertIs(self.person1, new_person)
