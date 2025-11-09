import unittest
from unittest.mock import patch
from src.main import prompt_user_name

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['Alice'])
    def test_prompt_user_name(self, mock_input):
        with patch('builtins.print') as mock_print:
            prompt_user_name()
            mock_print.assert_called_once_with("Hello, Alice!")


## Not working

if __name__ == '__main__':
    unittest.main()
