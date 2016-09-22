"""
*****************************************************
Advent of Code - Day 5

Naughty vs nice strings

Given properties for a "naughty string" and a "nice
string", you need to figure out which strings are
which, upon being given a significant list.

*****************************************************
"""

def Day5():
    vowels = ["a", "e", "i", "o", "u"]
    bad_strings = ["ab", "cd", "pq", "xy"]
    count = 0
    fob = open("/Users/JustinZhou/Documents/Programming/AdventofCode/Day5textinput.txt", "r")
    for line in fob:
        vcount = 0
        nice = True
        double_vowel = False
        for i in range(len(line)):
            if line[i] in vowels:
                vcount += 1
            if line[i:i+2] == line[i]*2:
                double_vowel = True
        for j in range(len(bad_strings)):
            if bad_strings[j] in line:
                nice = False
        if vcount < 3:
            nice = False
        if double_vowel == False:
            nice = False
        if nice == True:
            count += 1
        print str(line)
        print "vowel count: " + str(vcount)
        print "nice or not: " + str(nice)
        print "double vowel: " + str(double_vowel)
        print "count: " + str(count)
    fob.close()
    print count
    return

def Day5Bonus():

    fob = open("/Users/JustinZhou/Documents/Programming/AdventofCode/Day5textinput.txt", "r")
    count = 0
    for line in fob:
        i = 0
        pairs = False
        sandwich = False
        while (sandwich == False or pairs == False) and i < len(line):
            if sandwich == False and i < len(line)-2:
                if line[i] == line[i+2]:
                    sandwich = True
            if pairs == False and i < len(line)-3:
                if line[i:i + 2] in line[i+2:len(line)]:
                    pairs = True
            i += 1
        if pairs == True and sandwich == True:
            count += 1
            print str(count) + " : " + str(line)
    fob.close()
    print "count: " + str(count)
    return




#Day5()
Day5Bonus()
