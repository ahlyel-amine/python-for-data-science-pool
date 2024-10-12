import sys

PUNCTUATIONS = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def ispunctuationmarks(char : str) -> bool:
    """
    Check if a character is a punctuation mark.

    Parameters:
    char (str): The character to be checked.

    Returns:
    bool: True if the character is a punctuation mark, False otherwise.
    """
    return char in PUNCTUATIONS


def building(obj:str):
    """
    This function takes a string as input and prints information about the characters in the string.
    
    Parameters:
    obj (str): The input string.
    
    Returns:
    None
    """
    print("Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.")
    print(f'The text contains {len(obj)} characters:')
    print(sum(map(str.isupper, obj)), ' upper letters')
    print(sum(map(str.islower, obj)), ' lower letters')
    print(sum(map(ispunctuationmarks, obj)), '  punctuation marks')
    print(sum(map(str.isspace, obj)), ' spaces')
    print(sum(map(str.isdigit, obj)), ' digits')

def main():
    """
    This function is the entry point of the program.
    It takes an optional command-line argument or prompts the user for input.
    It then calls the `building` function with the provided argument.
    If more than one argument is provided, it raises an AssertionError.
    """
    try:
        argc = len(sys.argv)
        if argc == 1:
            arg = input("ara prompt: ")
        else :
            arg = sys.argv[1]
        assert argc <= 2, "More than one argument is provided to the program. Expected 1"
        building(arg)
    except AssertionError as error:
        print(error)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        sys.exit(0)
    except EOFError:
        print("\nEnd of file error.")
        sys.exit(0)


if __name__ == "__main__":
    main()
