from connector import Mongo

def creat_action_dict(file):
    res = Mongo.action.find()

    File = open(file, 'w')
    for action in res:
        name = action['name']
        if name[-1] == ')':
            l = name.find('(')
            name = name[:l]
            File.write(name + '\n')
        elif name[-1] == 'L':
            name = name[:-1]
            File.write(name + '\n')


if __name__ == '__main__':
    creat_action_dict('dict/action.txt')
