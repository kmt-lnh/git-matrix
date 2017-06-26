# little pyton script, to schedule github commits, so the contribution
# counter is showing a text message. Basically we want to map a list
# of characters to a list of dates, so that each character yields a series of
# dates, and if i commit on those dates, the commit squares will draw the
# characters.

# we'll need a file with the transcription of characters to a list of lists
# (with zero and one for commint days) and also a way to draw the commit boxes
# to test the file

white_box = "□"
black_box = "■"

#print white_box
#print black_box
print " "
seven = [white_box for i in xrange(0,7)]

#for e in seven:
#    print e

# for easier printing we'll encode the letters column by column... :)
# font is from here https://fontstruct.com/fontstructions/show/847768/5x7_dot_matrix
# = [[],[],[],[],[]]
chartable = {}
chartable['A'] =[[0,0,1,1,1,1,1],[0,1,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,0,0,1,0,0],[0,0,1,1,1,1,1]]
chartable['B'] =[[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[0,1,1,0,1,1,0]]
chartable['C'] =[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,0,0,0,1,0]]
chartable['D'] =[[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]]
chartable['E'] =[[1,1,1,1,1,1,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,0,0,0,1]]
chartable['F'] =[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,0,0,0,0]]
chartable['G'] =[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,1,0,0,1],[0,1,0,1,1,1,1]]
chartable['H'] =[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[1,1,1,1,1,1,1]]
chartable['I'] =[[1,0,0,0,0,0,1],[1,1,1,1,1,1,1],[1,0,0,0,0,0,1]]
chartable['J'] =[[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,0],[1,0,0,0,0,0,0]]
chartable['K'] =[[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[0,1,0,0,0,1,0],[1,0,0,0,0,0,1]]
chartable['L'] =[[1,1,1,1,1,1,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1]]
chartable['M'] =[[1,1,1,1,1,1,1],[0,1,0,0,0,0,0],[0,0,1,1,0,0,0],[0,1,0,0,0,0,0],[1,1,1,1,1,1,1]]
chartable['N'] =[[1,1,1,1,1,1,1],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[1,1,1,1,1,1,1]] 
chartable['O'] =[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[0,1,1,1,1,1,0]]
chartable['P'] =[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[1,0,0,1,0,0,0],[0,1,1,0,0,0,0]]
chartable['Q'] =[[0,1,1,1,1,1,0],[1,0,0,0,0,0,1],[1,0,0,0,1,0,1],[1,0,0,0,0,1,0],[0,1,1,1,1,0,1]]
chartable['R'] =[[1,1,1,1,1,1,1],[1,0,0,1,0,0,0],[1,0,0,1,1,0,0],[1,0,0,1,0,1,0],[0,1,1,0,0,0,1]]
chartable['S'] =[[0,1,1,0,0,1,0],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[1,0,0,1,0,0,1],[0,1,0,0,1,1,0]]
chartable['T'] =[[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0]]
chartable['U'] =[[1,1,1,1,1,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[1,1,1,1,1,1,0]]
chartable['V'] =[[1,1,1,1,1,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[1,1,1,1,1,0,0]]
chartable['W'] =[[1,1,1,1,1,1,0],[0,0,0,0,0,0,1],[0,0,0,1,1,1,0],[0,0,0,0,0,0,1],[1,1,1,1,1,1,0]]
chartable['X'] =[[1,1,0,0,0,1,1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,1,0,1,0,0],[1,1,0,0,0,1,1]]
chartable['Y'] =[[1,1,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,1,1],[0,0,0,1,0,0,0],[1,1,1,0,0,0,0]]
chartable['Z'] =[[1,0,0,0,0,1,1],[1,0,0,0,1,0,1],[1,0,0,1,0,0,1],[1,0,1,0,0,0,1],[1,1,0,0,0,0,1]]
"""
"""
chartable['a'] =[[0,0,0,0,0,1,0],[0,0,1,0,1,0,1],[0,0,1,0,1,0,1],[0,0,1,0,1,0,1],[0,0,0,1,1,1,1]]
"""
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
"""
space = [[0,0,0,0,0,0,0]]


#print len(A + a)
#As = H + space + I + space + space + space + U + space + L + space + A
#printChar(As)

def stringToCharDefList(string,chrTable):
    result = []
    for c in list(string):
        result = result + chrTable[c] + space
    return result

# for testing the display
def boxSub(num):
    if num == 0:
        return " "
    else:
        return "■"


# a chardef is simply [[x]] holding ones and zeroes
def printChar(chardef):
    heigth = len(chardef[0])
    for row in xrange(0,heigth):
        charrow = ''.join([boxSub(x[row]) for x in chardef])
        print charrow



print ""
printChar(stringToCharDefList("FOO",chartable))
