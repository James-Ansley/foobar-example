import sys

from foobar import say_message


def main():
    match sys.argv:
        case [_, "--help", *_]:
            print("FooBar: Cool Cowsay tool")
            print("Usage:")
            print("foobar mssage [cow-type]")
        case [_, msg]:
            say_message(msg)
        case [_, msg, cow]:
            say_message(msg, cow)
