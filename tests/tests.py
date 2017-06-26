# -*- coding: utf-8 -*-

# run tests here with "$ python -m unittest tests"

import unittest
from letters import *
from dotmatrix import *


class TestDotMatrix(unittest.TestCase):

    def test_helloWorld(self):
        testString = "\n" + \
                     "@  @     @@ @@        @   @          @@      @ @ \n" + \
                     "@  @      @  @        @   @           @      @ @ \n" + \
                     "@  @  @@  @  @   @@   @   @  @@  @ @  @   @@ @ @ \n" + \
                     "@@@@ @  @ @  @  @  @  @ @ @ @  @ @@ @ @  @  @@ @ \n" + \
                     "@  @ @@@@ @  @  @  @  @ @ @ @  @ @    @  @   @ @ \n" + \
                     "@  @ @    @  @  @  @  @ @ @ @  @ @    @  @   @   \n" + \
                     "@  @  @@ @@@@@@  @@    @ @   @@  @   @@@  @@@@ @ " 
        
        compStr = printChar2(stringToCharDefList2("Hello World!",chartable))
        self.assertEqual(testString,compStr)
        
if __name__ == '__main__':
    unittest.main()