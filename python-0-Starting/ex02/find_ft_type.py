def all_thing_is_obj(object: any) -> int:
    c = type(object)
    if c in [list, tuple, set, dict]:
        print(f'{c.__name__.capitalize()} : {c}')
    elif c == str:
        print(f'{object} is in the kitchen : {c}')
    else:
        print("Type not found")
    return 42
