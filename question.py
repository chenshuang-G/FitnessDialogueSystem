#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

import re

'''
Question class is a util class to convert a question
from a string format to a searching format, such as
"平板支撑锻炼了哪块肌肉？"
 =>
    focus("action")
    content("平板支撑")
    target("action.muscle.txt")

The basic workflow to finish this requirement：
1. questionCut
'''

class Question:
    patternList = ['special', 'muscle', 'action', 'machine', 'negative']

    def __init__(self):
        self.matchPattern = {}
        for pattern in Question.patternList:
            filename = 'dict/' + str(pattern) + '.txt'
            list = []
            with open(filename, 'rt', encoding='UTF-8') as file:
                for line in file.readlines():
                    list.append(line.strip())
            if list != []:
                self.matchPattern[str(pattern)] = re.compile(str(list) + str('+'), re.I | re.M)
            else:
                self.matchPattern[str(pattern)] = None

    def questionCut(self, question):
        matchResult = {}
        for pattern in Question.patternList:
            if self.matchPattern[str(pattern)] == None:
                continue
            for m in self.matchPattern[str(pattern)].finditer(question):
                matchResult[str(pattern)] = {'content': m.group(0),'startPos': m.start(), 'endPos': m.end()}

        for key in matchResult.keys():
            print(str(key), str(matchResult[str(key)]))
        # print(matchResult)

questionInstance = Question()

question = "平板支撑锻炼了哪块肌肉?"
print(question)
questionInstance.questionCut(question)

question = "平板支撑锻炼肌肉要多少天才有效果?"
print(question)
questionInstance.questionCut(question)