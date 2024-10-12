from ft_filter import ft_filter
import sys

def main():
    try:
        argc = len(sys.argv)
        assert argc == 3, "AssertionError: the arguments are bad"
        assert sys.argv[2].isdigit(), "AssertionError: the arguments are bad"
        nbr = int(sys.argv[2])
        splited = sys.argv[1].split()
        print(list(ft_filter(lambda item : len(item) > nbr and item.isalnum() , splited)))

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
