from TypewriterPrint import TypewriterPrint as tp
import pytest


def test_speed_error():
    with pytest.raises(UserWarning):
        tp.print_tw("hi", 20000)
