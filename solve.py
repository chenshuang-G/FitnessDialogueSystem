from action import *
from muscle import *


def get_muscle_of_action(action):
    #返回肌肉列表
    return Action(action).get_muscle()


def get_equipment_of_action(action):
    #返回器械列表
    return Action(action).get_equipment()


def get_level_of_action(action):
    #返回动作等级
    return Action(action).get_level()


def get_details_of_action(action):
    #返回动作细节
    return Action(action).get_details()


def get_type_of_action(action):
    #返回动作类别
    return Action(action).get_type()

def get_muscleGroup_action(muscleGroup):
    #返回肌肉组 涵盖动作
    return MuscleGroup(muscleGroup).list_muscleGroup_action()

if __name__ == '__main__':
    print(get_muscle_of_action('平板支撑'))
    print(get_muscleGroup_action('肱二头肌'))
