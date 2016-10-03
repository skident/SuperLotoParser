#!/usr/bin/python
# -*- coding: cp1251 -*-

import glob


class CsvParser:
    statistics = dict()
    raw_lines = []
    combinations = dict()

    def __init__(self):
        for x in range(0,10):
            self.statistics[x] = 0


        # print(self.statistics)


    def load(self, filename, balls_count = 3):
        f = open(filename, 'r', encoding='cp1251')
        # s = f.readline()
        # print(f)

        start_pos = 4

        for line in f:
            # values = sorted([int(x) for x in line.split(';')[4:10]])
            # values = sorted(values)
            # print(values)

            # print(line.split(';')[4:7])

            # for x in line.split(';')[4:10]:

            numbers = sorted(line.split(';')[start_pos:start_pos+balls_count])
            numbers = ''.join(numbers)
            self.raw_lines.append(numbers)

            if numbers in self.combinations:
                self.combinations[numbers] += 1
            else:
                self.combinations[numbers] = 1

            for x in numbers:
                self.statistics[int(x)] += 1
        f.close()




    def show(self):
        # print(self.statistics)
        for ball, count in self.statistics.items():
            print(str(ball) + " => " + str(count))

    def showReversed(self):
        reversedDict = dict()
        for ball, count in self.statistics.items():
            if count in reversedDict:
                reversedDict[count] += ", " + str(ball)
            else:
                reversedDict[count] = str(ball)

        sortedKeys = reversed(sorted(reversedDict.keys()))
        for count in sortedKeys:
            ball = reversedDict[count]
            print(str(count) + " => " + ball)
        # for count, ball in reversedDict.items():
        #     print(str(count) + " => " + ball)

    def showRaw(self):
        print(sorted(self.raw_lines))

    def showCombinations(self):
        sortedKeys = reversed(sorted(self.combinations.keys()))
        for k in sortedKeys:
            if k == '':
                continue

            v = self.combinations[k]
            print(k, " => ", v)

def main():
    parser = CsvParser()

    # files = glob.glob("/Users/skident/Documents/Projects/Python/SuperLoto/csv/*.csv")
    files = glob.glob("/Users/skident/Documents/Projects/Python/SuperLoto/loto3/*.csv")
    for file in files:
        parser.load(file)
    # parser.show()

    parser.showReversed()
    parser.showRaw()
    parser.showCombinations()

if __name__ == '__main__':
    main()