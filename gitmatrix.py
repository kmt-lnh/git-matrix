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

# the extra logic in the ifs is just for a bit of "kerning", so that
# we fit into github's 7x52 screen
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



grab = lambda x,y: y if x == 1 else []

def messageToDates(message,startDate,chartable):
    points = list(chain(*stringToCharDefList2("Hello World!",chartable)))
    datelist = [startDate + timedelta(days=x) for x in xrange(0,len(points))]
    return datelist

def printChar2(chardef):
    heigth = len(chardef[0])
    retString = ""
    for row in xrange(0,heigth):
        charrow = ''.join([boxSub(x[row]) for x in chardef])
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
        print printChar2(stringToCharDefList2(message,letters.chartable))
        print ""
        print '* org tree for message "%smessage"' % message
        for e in datelist:
            print "** TODO <%s>" % e.strftime("%Y-%m-%d")
            print "    SCHEDULED: <%s>" % e.strftime("%Y-%m-%d")
    except:
        print 'usage: gitmatrix.py "date" "message"'
        print 'Date should be in "yyyy-mm-dd" format'
        print 'Also, right now the only way to guarantee correct printing is'
        print 'to start on a Sunday. Later this will be amended.'
