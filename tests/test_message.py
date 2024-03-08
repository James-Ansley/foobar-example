from contextlib import redirect_stdout
from io import StringIO

from foobar import say_message

MESSAGE = r"""
 _______________ 
< hello, world! >
 --------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

""".strip("\n")


def test_say_message():
    string = StringIO()
    with redirect_stdout(string):
        say_message("hello, world!")
    assert string.getvalue().strip("\n") == MESSAGE
