from math import isnan

def NULL_not_found(object: any) -> int:
    data = dict({
        "int" : "Zero: 0 ",
        "float" : "Cheese: nan ",
        "NoneType": "Nothing: None ",
        "str": "Empty: ",
        "bool": "Fake: False ",
    })
    c = type(object)
    if (c == float and isnan(object)) or not object:
        print(f'{data[c.__name__]} {c}')
    else:
        print('Type not Found')
        return 1
    return 0
