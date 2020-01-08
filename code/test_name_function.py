import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Jenny Nicholson' work?"""
        formatted_name = get_formatted_name('jenny', 'nicholson')
        self.assertEqual(formatted_name, 'Jenny Nicholson')


    def test_first_last_middle_name(self):
        """Do names like Kayleigh Sophia Nicholson work?"""
        formatted_name = get_formatted_name('kayleigh', 'nicholson', 'sophia')
        self.assertEqual(formatted_name, 'Kayleigh Sophia Nicholson')

if __name__ == '__main__':
    unittest.main()