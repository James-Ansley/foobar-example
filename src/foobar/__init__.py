from cowsay import cowsay

__all__ = ["say_message"]


def say_message(message: str, cow: str = "default") -> None:
    print(cowsay(message, cow=cow))
