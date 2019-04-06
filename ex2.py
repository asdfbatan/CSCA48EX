from container import *


def banana_verify(source, goal, container, moves):
    '''(string, string, class, list) -> bool
    This is a function that verifies solutions for the banana game.
    REQ: the moves list must in the form like ['P', 'M', 'G', 'M']
    '''
    same = len(source) == len(goal)
    i = 0
    j = 0
    temp_goal = ""
    while i < len(moves) and same:
        if moves[i] == "P":
            try:
                container.put(source[j])
            except:
                same = False
            j += 1
        elif moves[i] == "G":
            try:
                temp_goal += container.get()
            except:
                same = False
        else:
            try:
                temp_goal += source[j]
            except:
                same = False
            j += 1
        i += 1
    return same and temp_goal == goal
