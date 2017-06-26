# -*- coding: utf-8 -*-

# little pyton script, to schedule github commits, so the contribution
# counter is showing a text message. Basically we want to map a list
# of characters to a list of dates, so that each character yields a series of
# dates, and if i commit on those dates, the commit squares will draw the
# characters.

import letters
from itertools import chain
from datetime import date,timedelta

# for testing the display
def boxSub(num):
    if num == 0:
        return " "
    else:
        return "@"

def stringToCharDefList(string,chrTable):
    result = []
    for c in list(string):
        result = result + chrTable[c] + chrTable[' ']
    return result

def stringToCharDefList2(string,chrTable):
    result = []
    strlist = list(string)
    for e,c in enumerate(strlist):
        if e+1 < len(strlist) and (strlist[e+1] == "l" or strlist[e+1] == " ") :
            result = result + chrTable[c]
        else:
            result = result + chrTable[c] + chrTable[' ']
    return result



# a chardef is simply [[x]] holding ones and zeroes
# must return a collection of rows for printing, or
# one gigantic string with newlines
def printChar(chardef):
    heigth = len(chardef[0])
    for row in xrange(0,heigth):
        charrow = ''.join([boxSub(x[row]) for x in chardef])
        print charrow

# printChar(stringToCharDefList2("Hello World!",chartable))


# points = list(chain(*stringToCharDefList2("Hello World!",chartable)))

# has to start on sunday
# today = date.today()
# startDate = date(2017,6,25) # this is an incoming arg from the cmdline
# datelist = [startDate + timedelta(days=x) for x in xrange(0,len(points))]
# format string is: date.strftime("%Y-%m-%d")

grab = lambda x,y: y if x == 1 else []

# for e in filter(lambda x: x != [],map(grab,points,datelist)):
#     print e




# this is no good - i want to test the printchar function!
def printChar2(chardef):
    heigth = len(chardef[0])
    retString = ""
    for row in xrange(0,heigth):
        charrow = ''.join([boxSub(x[row]) for x in chardef])
        retString = retString + '\n' + charrow
    return retString

#print list(testString)
#print list(testChar(stringToCharDefList2("Hello World!",chartable)))

# print testString
# print testChar(stringToCharDefList2("Hello World!",chartable))
# print testChar(stringToCharDefList2("M x butterfly",chartable))

# print testString == testChar(stringToCharDefList2("Hello World!",chartable))
