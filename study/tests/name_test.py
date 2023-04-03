
import unittest
import func_name

class NameTest(unittest.TestCase):
    
    def test_first_last_name(self):
        #Имена вида 'Janis Joplin' работают правильно?
        formatted_name = func_name.get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        #Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?
        formatted_name = func_name.get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()