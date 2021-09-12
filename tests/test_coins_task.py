import unittest

from coins_task import __version__
from coins_task import split_on_coins


class TestCoinsSplitter(unittest.TestCase):
    def test_coin_splitter(self):
        assert split_on_coins(12, [1, 2, 5]) == [5, 5, 2]
        assert split_on_coins(13, [1, 2, 5]) == [5, 5, 2, 1]
        assert split_on_coins(32, [6, 8, 1]) == [8, 8, 8, 8]
        assert split_on_coins(3, [1]) == [1, 1, 1]
        assert split_on_coins(999, []) == []
