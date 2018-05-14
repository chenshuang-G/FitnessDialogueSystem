from solve import *

patternList = [
    ['action', '肌肉'],# 卧推锻炼哪些肌肉
    ['action', 'muscle'],# 俯卧撑除了练
    ['action'],# 怎样做俯卧撑
    ['练', 'muscle'],# 怎么样可以锻炼腹肌
    ['action', '要', '器'],# 平板支撑需要什么器械/道具/设备/条件
    ['action', '动作'],# 跟仰卧起坐差不多的动作有什么
    ['muscle', '练'],# 腹肌怎么练
]


def pattern_match(pattern, sentence):
    #print(pattern)
    #print(sentence)
    #1 split sentence
    #2 find out focus word  eg muscle/special/action
    #3
    if len(pattern) != len(sentence):
        return False
    l = len(sentence)
    # print(l)
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
        if sentence[i][1] == pattern[i]:
            continue
        return False
    return True


def pattern(sentence):
    for index, p in enumerate(patternList):
        # print(index)

        if pattern_match(p, sentence):
            print(sentence)
            if index == 0:
                # print(1)
                return get_muscle_of_action(sentence[0][1])
            if index == 1:
                return get_muscleGroup_action(sentence[1][1])
            if index == 2:
                return get_details_of_action(sentence[0][1])
            if index == 3:
                return get_muscleGroup_action(sentence[1][1])
            if index == 4:
                return get_equipment_of_action(sentence[0][1])
            if index == 5:
                return get_muscleGroup_action(sentence[0][1])
    return 'unknown'


if __name__ == '__main__':
    print(pattern([('action', '平板支撑'), ('special', '肌肉')]))
    print(pattern([('action', '平板支撑'), ('muscle', '腹肌')]))
    print(pattern([('action', '平板支撑'), ('special','有效')]))
    print(pattern([('special', '可以'), ('muscle', '腹肌')]))
    print(pattern([('action', '平板支撑'), ('special', '器材')]))
    # print(pattern([('action', '平板支撑'), ('special', '动作')]))#unsovle
