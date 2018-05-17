from solve import *

patternList = [
<<<<<<< Updated upstream
    ['action'],# 怎样做俯卧撑
    ['action','肌肉'],# 卧推锻炼哪些肌肉
    ['action','组'],# 卧推怎样做组训练
    ['action','防具'],# 深蹲防具该准备哪些
    ['action','注意'],# 卧推要有什么特别注意事项
    ['action', '要', '器'],# 平板支撑需要什么器械/道具/设备/条件
    ['action', '动作'],# 跟仰卧起坐差不多的动作有什么
    ['action','muscle'],# 俯卧撑除了练胸还能练哪里
    ['action','muscle','special'],# 哑铃练二头有效果吗
    
    ['muscle', '练'],# 腹肌怎么练
    ['muscle','拉伸'],# 背阔肌怎样拉伸
    ['muscle','热身'],# 背阔肌怎样热身
    
    ['练','水'],# 锻炼怎样补充水
    ['练','能量'],# 锻炼能量怎样补充
    ['练', 'muscle'],# 怎么样可以锻炼腹肌
    ['极限','action','保护'],# 极限重量深蹲怎样保护避免受伤
    ['服饰'],# 去健身房穿什么运动服饰比较好
    
    ['machine','动作'],# 哑铃主要可以做哪些动作
    ['machine','action','重量'],# 杠铃卧推重量该怎么选择
    ['machine','action','special'],# 哑铃卧推比杠铃卧推效果好吗
    ['machine','action','muscle'],# 哑铃卧推怎样锻炼到胸中束
    ['machine','muscle','special'],# 哑铃练二头有效果吗
    ['',''],#明天再写点 ，不知道这种可以不？
=======
    ['action', '肌肉'],# 卧推锻炼哪些肌肉1 return muscle of action
    ['action', 'muscle'],# 俯卧撑除了练腹肌 return muscle of action
    ['action'],# 怎样做俯卧撑3 return detial of action ##如果只有一个词，返回动作整体信息
    ['练', 'muscle'],# 怎么样可以锻炼腹肌4 return detial of action
    ['action', '要', '器'],# 平板支撑需要什么器械/道具/设备/条件5 return equipment of action
    ['action', '动作'],# 跟仰卧起坐差不多的动作有什么6 return action of muscle
    ['muscle', '练'],# 腹肌怎么练7 return detail of action
>>>>>>> Stashed changes
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
                return get_muscle_of_action(sentence[0][1])
            if index == 1:
                return get_muscle_of_action([0][1])
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
