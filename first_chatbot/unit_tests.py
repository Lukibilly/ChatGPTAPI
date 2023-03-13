from api_functions import *
from bot_functions import *
from helper_functions import *


def test_get_bot_blueprint():
    info = get_bot_blueprint("test")
    print(info.split("\n"))



def main():
    test_get_bot_blueprint()


if __name__ == '__main__':
    main()