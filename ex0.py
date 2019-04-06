def greeting(name):
    '''(string) -> NoneType
    This function take a person’s name, returns a greeting in required form.
    REQ: the input must be a string.
    >>>greeting("a")
    'Hello a how are you today?'
    '''
    return "Hello " + name + " how are you today?"


def mutate_list(list1):
    '''(list) -> NoneType
    This function takes in a list and modifies that list in the following ways:
    integer multipled by 2, boolean is inverted,
    string has its first and last characters removed
    The 0th element of the list is set to the string Hello.
    REQ: (1) The input list will have at least 1 element in it
         (2) All strings will have at least 2 characters in them.
         (3) The function shouldn’t return anything.
    >>>mutate_list([1, 55, "hiitsme", False, True])
    ['Hello', 110, 'iitsm', True, False]
    >>>mutate_list(['Hello', False, 1, True, 0.5, 5, 0, 'utorid'])
    ['Hello', True, 2, False, 0.5, 10, 0, 'tori']
    '''
    for i in range(1, len(list1)):
        if isinstance(list1[i], bool):
            list1[i] = not list1[i]
        elif isinstance(list1[i], int):
            list1[i] += list1[i]
        elif isinstance(list1[i], str):
            list1[i] = list1[i][1: -1]
        else:
            pass
    list1[0] = "Hello"


def merge_dicts(dictionary1, dictionary2):
    '''(dict, dict) -> dict
    This function takes two dictionaries as input,
    returns a new dictionary with all key: value pairs from both dictionaries.
    If the dictionaries share a key, the resulting value will be the list from
    the second dictionary appended to the list from the first dictionary.
    REQ: the format {str: list of ints}.
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    '''
    dictionary = {}
    for key in dictionary1:
        dictionary[key] = dictionary1[key][:]
    for key in dictionary2:
        if key in dictionary:
            dictionary[key] += dictionary2[key]
        else:
            dictionary[key] = dictionary2[key][:]
    return dictionary
