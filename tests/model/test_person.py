import unittest
import datetime
from faker import Faker
from src.model.Person import Person
from src.Community.base import Session, engine, Base


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.data_factory = Faker()
        self.data = []
        self.people = []
        for i in range(0, 10):
            self.data.append(
                (self.data_factory.name(), self.data_factory.random_number()))
            self.people.append(Person(name=self.data[-1][0], year=self.data[-1][-1]))
        self.session = Session()
        self.person1 = Person(name="Alejandra", year=25)
        self.person2 = Person(name="Diego", year=22)
        self.person3 = Person(name="Alejandra", year=25)
        self.person4 = Person(name="Diana", year=25)
        self.group = [self.person1, self.person2, self.person3]

    def tearDown(self):
        self.session.query(Person).delete()
        self.session.commit()
        self.session.close()

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

    def test_element_in_group(self):
        self.assertIn(self.person3, self.group)
        self.assertNotIn(self.person4, self.group)

    def test_class_instance(self):
        self.assertIsInstance(self.person1, Person)
        self.assertNotIsInstance(self.group, Person)

    def test_store(self):
        self.person1.store()
        person = self.session.query(Person).filter(
            Person.name == 'Alejandra' and Person.year == 25).first()

        self.assertEqual(person.get_name(), 'Alejandra')
        self.assertEqual(person.get_year(), 25)

    def test_find(self):
        self.session.add(self.person2)
        self.session.commit()

        person = Person("", 0)
        person.find('Diego', 22)

        self.assertEqual(person.get_name(), 'Diego')
        self.assertEqual(person.get_year(), 22)

    def test_constructor_random(self):
        for person, dat in zip(self.people, self.data):
            self.assertEqual(person.get_name(), dat[0])
            self.assertEqual(person.get_year(), dat[-1])

    def test_birth_year_random(self):
        for person, dat in zip(self.people, self.data):
            self.assertEqual(person.calculate_birth_day(
                True), datetime.datetime.now().year - dat[-1])

    def test_assign_random(self):
        original_data = (self.data_factory.name(), self.data_factory.random_number())
        test_person = Person(name=original_data[0], year=original_data[-1])
        new_data = (self.data_factory.name(), self.data_factory.random_number())
        while new_data[0] == original_data[0] or new_data[-1] == original_data[-1]:
            new_data = (self.data_factory.name(), self.data_factory.random_number())
        test_person.set_name(new_data[0])
        test_person.set_year(new_data[-1])

        self.assertFalse(test_person.get_name() == original_data[0])
        self.assertFalse(test_person.get_year() == original_data[-1])
        self.assertTrue(test_person.get_name() == new_data[0])
        self.assertTrue(test_person.get_year() == new_data[-1])

    def test_objects_equals_random(self):
        new_person = self.people[-1]

        self.assertIsNot(new_person, self.people[0])
        self.assertIs(new_person, self.people[-1])

    def test_element_in_group_random(self):
        self.assertIsInstance(self.people[0], Person)
        self.assertNotIsInstance(self.people, Person)

    def test_store_random(self):
        self.people[0].store()

        self.session = Session()
        person = self.session.query(Person).filter(
            Person.name == self.data[0][0] and Person.year == self.data[0][1]).first()

        self.assertEqual(person.get_name(), self.data[0][0])
        self.assertEqual(person.get_year(), self.data[0][-1])

    def test_find_random(self):
        self.session = Session()
        self.session.add(self.people[0])
        self.session.commit()
        self.session.close()

        person = Person("", 0)
        person.find(self.data[0][0], self.data[0][-1])

        self.assertEqual(person.get_name(), self.data[0][0])
        self.assertEqual(person.get_year(), self.data[0][-1])
