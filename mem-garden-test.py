import unittest
import sys
import timeit
from wordgroup import wordcount

class TestM(unittest.TestCase):
    def setUp(self):
        pass

    def test_1M_file_size(self):
        """
        Test if data structure consumption is greater then 1124KB
        """
        res_word_count = wordcount('1MFile.txt')
        self.assertLess(sys.getsizeof(res_word_count), 1124)

    def test_10M_file_size(self):
        """
        Test if data structure consumption is greater then 2KB
        """
        res_word_count = wordcount('10MFile.txt')
        self.assertLess(sys.getsizeof(res_word_count), 2048)

    def test_100M_file_size(self):
        """
        Test if data structure consumption is greater then 5KB
        """
        res_word_count = wordcount('100MFile.txt')
        self.assertLess(sys.getsizeof(res_word_count), 5120)

    def test_500M_file_size(self):
        """
        Test if data structure consumption is greater then 10KB
        """
        res_word_count = wordcount('500MFile.txt')
        self.assertLess(sys.getsizeof(res_word_count), 10240)

    def test_time_1M_file_size(self):
        """
        Test if execution time is less than 1m for 1M size file
        """
        t = timeit.Timer(stmt="wordcount('1MFile.txt')", setup="from wordgroup import wordcount")
        self.assertLess(t.timeit(number=1), 30)

    def test_time_10M_file_size(self):
        """
        Test if execution time is less than 1m for 1M size file
        """
        t = timeit.Timer(stmt="wordcount('10MFile.txt')", setup="from wordgroup import wordcount")
        self.assertLess(t.timeit(number=1), 60)

    def test_time_100M_file_size(self):
        """
        Test if execution time is less than 1m for 1M size file
        """
        t = timeit.Timer(stmt="wordcount('100MFile.txt')", setup="from wordgroup import wordcount")
        self.assertLess(t.timeit(number=1), 60)
