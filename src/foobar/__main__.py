import sys

from foobar import say_message


def main():
    match sys.argv:
        case [_, msg]:
            say_message(msg)
        case [_, msg, cow]:
            say_message(msg, cow)
