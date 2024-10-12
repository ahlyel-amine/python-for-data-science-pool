from sys import argv, exit

def to_integer(obj : str) -> int:
    try : 
        return int(obj)
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

argc = len(argv)

if argc < 2:
    exit(0)

try :
    assert argc <= 2, "AssertionError: more than one argument is provided"
    nbr = to_integer(argv[1])
    print('I\'m Odd.' if nbr % 2 else 'I\'m Even.')
except AssertionError as error:
    print(error)
