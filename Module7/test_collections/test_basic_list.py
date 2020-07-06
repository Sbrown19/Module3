# Program: Basic List test
# Author: Skyler Brown
# Date: 06/21/2020

import unittest
from unittest.mock import patch
import fun_with_collections.topic1 as topic1


class TestList(unittest.TestCase):
    @patch('module.function', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(topic1.make_list(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
