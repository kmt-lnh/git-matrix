# -*- coding: utf-8 -*-

# run tests here with "$ python -m unittest -v tests.tests"

import unittest

from letters import *
from gitmatrix import *
from datetime import date,timedelta

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

    def test_filteredDates(self):
        testMessage = "Hello World!"
        startDate = date(2017,06,25)
        points = list(chain(*stringToCharDefList2(testMessage,chartable)))
        datelist = [startDate + timedelta(days=x) for x in xrange(0,len(points))]
        listToPrint = messageToDates(testMessage,startDate,chartable)
        self.assertNotEqual(len(datelist),len(listToPrint))
        
if __name__ == '__main__':
    unittest.main()
