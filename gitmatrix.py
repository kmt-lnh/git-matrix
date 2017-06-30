# -*- coding: utf-8 -*-

# little pyton script, to schedule github commits, so the contribution
# counter is showing a text message. Basically we want to map a list
# of characters to a list of dates, so that each character yields a series of
# dates, and if i commit on those dates, the commit squares will draw the
# characters.

import sys
import letters
from itertools import chain
from datetime import date,timedelta


def charToDisplay(num):
    """
    Auxiliary function to test the dotmatrix message to be printed.
    '@' is used as it fills out the space the most.
    """
    if num == 0:
        return " "
    else:
        return "@"

def stringToCharDefList(string,chrTable):
    """
    Generic routine to turn a string into a list of columns (also lists)
    that together draw a the string in question. The size of the matrix
    is deteremined by the character definitions in chrTable.
    """
    result = []
    for c in list(string):
        result = result + chrTable[c] + chrTable[' ']
    return result

def stringToCharDefListKerning(string,chrTable):
    """
    Github specific routine to turn a string into a list of columns (also lists)
    that together draw a the string in question. The size of the matrix is 
    deteremined by the character definitions in chrTable. There are extra rules
    to save space, so that more characters fit into a smaller space.
    """
    result = []
    strlist = list(string)
    for e,c in enumerate(strlist):
        if e+1 < len(strlist) and (strlist[e+1] == "l" or strlist[e+1] == " ") :
            result = result + chrTable[c]
        else:
            result = result + chrTable[c] + chrTable[' ']
    return result

# just a combinator to puncture one list with an other
puncture = lambda x,y: y if x == 1 else []

def messageToDates(message,startDate,chartable):
    """
    Given a message to print and a start date, this function returns a 
    flat list of dates when there should be counted github activity, so
    that the activity chart displays the expected message. One list is used
    to "puncture" an other.
    """
    points       = list(chain(*stringToCharDefListKerning("Hello World!",chartable)))
    datelist     = [startDate + timedelta(days=x) for x in xrange(0,len(points))]
    filteredList = [e for e in filter(lambda x: x != [],map(puncture,points,datelist))]
    return filteredList

def chardefToASCIIArt(chardef):
    """
    Given a character definition list, this function returns a string
    holding an ASCII art showing the resulting collection of pixels.
    """
    heigth = len(chardef[0])
    retString = ""
    for row in xrange(0,heigth):
        charrow = ''.join([charToDisplay(x[row]) for x in chardef])
        retString = retString + '\n' + charrow
    return retString


if __name__ == "__main__":
    try:
        YMD = map(int,sys.argv[1].split("-"))
        message = sys.argv[2]
        startDate = date(YMD[0],YMD[1],YMD[2])
        datelist = messageToDates(message,startDate,letters.chartable)
        print 'Org headlines for "%s" starting on %s' % (message,sys.argv[1])
        print ""
        print "The message will look like this:"
        print chardefToASCIIArt(stringToCharDefListKerning(message,letters.chartable))
        print ""
        print '* org tree for message "%s"' % message
        for e in datelist:
            print "** TODO commit on %s" % e.strftime("%Y-%m-%d")
            print "    SCHEDULED: <%s 11:00>" % e.strftime("%Y-%m-%d")
    except:
        print 'usage: gitmatrix.py "date" "message"'
        print 'Date should be in "yyyy-mm-dd" format'
        print 'Also, right now the only way to guarantee correct printing is'
        print 'to start on a Sunday. Later this will be amended.'
