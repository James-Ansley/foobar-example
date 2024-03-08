from cowsay import cowsay

__all__ = ["say_message"]


def say_message(message: str) -> None:
    print(cowsay(message))
