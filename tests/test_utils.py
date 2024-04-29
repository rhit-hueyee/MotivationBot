import sys
sys.path.append('../src')

import unittest
from unittest.mock import patch
from src.main import get_user_id

class TestBotFunctions(unittest.TestCase):
    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_get_user_id(self, mock_dict_reader, mock_open):
        mock_dict_reader.return_value = iter([{'username': 'applause7', 'id': '12345'}])
        user_id = get_user_id('applause7')
        self.assertEqual(user_id, '12345')

if __name__ == '__main__':
    unittest.main()
