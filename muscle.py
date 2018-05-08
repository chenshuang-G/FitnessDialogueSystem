class Muscle:
    def __init__(self, name, action_list, relative_muscle, muscle_group):
        self.name = name
        self.action_list = action_list
        self.relative_muscle = relative_muscle
        self.muscle_group = muscle_group

    def list_action(self, require):
        ret = []
        for action in self.action_list:
            if action.match(require):
                ret += action
        return ret

