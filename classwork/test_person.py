import unittest
import person

class MyTestCase(unittest.TestCase):
    def test_that_person_exist(self):
        person.Person("isreal",11)

    def test_that_get_name_return_name(self):
        akerele = person.Person("akerele",12)
        #assert
        self.assertEqual(akerele.get_name(), "akerele")
        funmi = person.Person("funmi", 18)
        self.assertEqual( funmi.get_name(),"funmi")
        #self.assertEqual(funmi.get_name(),"funmi")

    def test_that_get_age_returns_age(self):
        akerele = person.Person("akerele",12)

        #assert
        self.assertEqual( akerele.get_age(),12)
        funmi = person.Person("funmi", 18)
        self.assertEqual( funmi.get_age(),18)

    def test_that_greet_method_returns_greeting_message(self):
        funmi = person.Person("funmi", 18)
        self.assertEqual(funmi.greet(),"Hello funmi")

    def test_that_set_age_returns_a_correct_age(self):
        funmi = person.Person("funmi", 18)
        18self.assertRaises(ValueError, funmi.set_age, -1)


