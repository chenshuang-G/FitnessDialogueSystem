from solve import *

patternList = [
    ['action', '肌肉']
]


def pattern_match(pattern, sentence):
    #print(pattern)
    #print(sentence)
    if len(pattern) != len(sentence):
        return False
    l = len(sentence)
    #print(l)
    for i in range(l):
        #print(pattern[i])
        #print(sentence[i])
        if pattern[i] == 'action':
            if sentence[i][0] == 'action':
                continue
            return False
        if pattern[i] == 'muscle':
            if sentence[i][0] == 'muscle':
                continue
            return False
        if sentence[i][0] == 'special' or sentence[i][1] == pattern[i]:
            continue
        return False
    return True


def pattern(sentence):
    for index, p in enumerate(patternList):
        if pattern_match(p, sentence):
            if index == 0:
                return get_muscle_of_action(sentence[0][1])
    return 'unknown'


if __name__ == '__main__':
    print(pattern([('action', '平板支撑'), ('special', '肌肉')]))