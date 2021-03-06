from connector import Mongo


class Muscle:
    def __init__(self, name, action_list, relative_muscle, muscle_group):
        self.name = name
        self.action_list = action_list
        self.relative_muscle = relative_muscle
        self.muscle_group = muscle_group

    def get_action(self, require):
        ret = []
        for action in self.action_list:
            if action.match(require):
                ret += action
        return ret


class MuscleGroup:
    def __init__(self, name):
        self.name = name

    def list_muscleGroup_action(self):
        res = Mongo.muscle.find_one({'name': self.name})
        dict_muscle = res['muscleGroup']
        new_dict = str(dict_muscle).replace(' ','').split(',')
        return new_dict

