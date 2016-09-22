"""
*****************************************************
Advent of Code - Day 6

Probably a Fire Hazard

Which lights are lit up, given instructions for a
lights decorating contest?

*****************************************************
"""

def Day6():

    grid = [[0] * 1000 for k in range(1000)]

    fob = open("/Users/JustinZhou/Documents/Programming/AdventofCode/Day6textinput.txt", "r")
    count = 0

    for line in fob:
        instr = line.split()
        if instr[0] == "turn":
            if instr[1] == "on":
                x1 = int(instr[2].split(',')[0])
                y1 = int(instr[2].split(',')[1])
                x2 = int(instr[4].split(',')[0])
                y2 = int(instr[4].split(',')[1])
                for i in range(x2 - x1 + 1):
                    for j in range(y2 - y1 + 1):
                        tempx = x1 + i
                        tempy = y1 + j
                        grid[tempx][tempy] = 1
            if instr[1] == "off":
                x1 = int(instr[2].split(',')[0])
                y1 = int(instr[2].split(',')[1])
                x2 = int(instr[4].split(',')[0])
                y2 = int(instr[4].split(',')[1])
                for i in range(x2 - x1 + 1):
                    for j in range(y2 - y1 + 1):
                        grid[x1 + i][y1 + j] = 0
        if instr[0] == "toggle":
            x1 = int(instr[1].split(',')[0])
            y1 = int(instr[1].split(',')[1])
            x2 = int(instr[3].split(',')[0])
            y2 = int(instr[3].split(',')[1])
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    if grid[x1 + i][y1 + j] == 0:
                        grid[x1 + i][y1 + j] = 1
                    else:
                        grid[x1 + i][y1 + j] = 0
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == 1:
                count += 1
    print count
    return

def Day6Bonus():
    grid = [[0] * 1000 for k in range(1000)]

    fob = open("/Users/JustinZhou/Documents/Programming/AdventofCode/Day6textinput.txt", "r")
    count = 0

    for line in fob:
        instr = line.split()
        if instr[0] == "turn":
            if instr[1] == "on":
                x1 = int(instr[2].split(',')[0])
                y1 = int(instr[2].split(',')[1])
                x2 = int(instr[4].split(',')[0])
                y2 = int(instr[4].split(',')[1])
                for i in range(x2 - x1 + 1):
                    for j in range(y2 - y1 + 1):
                        grid[x1 + i][y1 + j] += 1
            if instr[1] == "off":
                x1 = int(instr[2].split(',')[0])
                y1 = int(instr[2].split(',')[1])
                x2 = int(instr[4].split(',')[0])
                y2 = int(instr[4].split(',')[1])
                for i in range(x2 - x1 + 1):
                    for j in range(y2 - y1 + 1):
                        if grid[x1 + i][y1 + j] > 0:
                            grid[x1 + i][y1 + j] -= 1
        if instr[0] == "toggle":
            x1 = int(instr[1].split(',')[0])
            y1 = int(instr[1].split(',')[1])
            x2 = int(instr[3].split(',')[0])
            y2 = int(instr[3].split(',')[1])
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    grid[x1 + i][y1 + j] += 2
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            count += grid[a][b]
    print count
    return

#Day6()
Day6Bonus()