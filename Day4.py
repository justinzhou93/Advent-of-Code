"""
*****************************************************
Advent of Code - Day 4

Santa's bitcoins

Santa is trying to crack MD5 code for AdventCoin
mining

*****************************************************
"""

import hashlib

def Day4(StrInput):
    success = False
    i = 0
    while success == False:
        m = hashlib.md5()
        m.update(StrInput + "{}".format(str(i)))
        if m.hexdigest()[0:6] == "000000":
            success = True
            print m.hexdigest()
        i += 1
    print str(i-1)
    return


Day4("iwrupvqb")