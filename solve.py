from action import *
from muscle import *


def get_muscle_of_action(action):
    return Action(action).get_muscle()


def get_equipment_of_action(action):
    return Action(action).get_equipment()


def get_level_of_action(action):
    return Action(action).get_level()


def get_details_of_action(action):
    return Action(action).get_details()


def get_type_of_action(action):
    return Action(action).get_type()


if __name__ == '__main__':
    print(get_muscle_of_action('平板支撑'))
