import unittest
from city_functions import get_city_details


class DetailsTestCase(unittest.TestCase):
    """Test whether our function works as it should"""

    def test_city_country(self):
        """Do names like 'Nairobi Kenya' work"""
        full_details = get_city_details('nairobi', 'kenya')
        self.assertEqual(full_details, 'Nairobi Kenya')


unittest.main()
