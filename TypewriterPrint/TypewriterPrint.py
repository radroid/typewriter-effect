#!usr/bin/python
from time import sleep
import sys


class TypewriterPrint:
    """
    The class contains a static method to print the input string with a typewriter effect (animation effect).

    Example:

        >> TypewriterPrint.print_tw('Hello World!')
        Hello World! # Printed with an animation.
    """

    @staticmethod
    def print_tw(string, speed=250):
        """
        Method prints the input string with an animation.

        Args:
            speed (int): Speed of print in characters per minute.
            string (str): A string to be printed.

        Returns: None

        """

        if speed < 0:
            raise UserWarning(f'Speed entered is {speed}, which is an invalid value.')
        elif speed > 285:
            raise UserWarning(f'Speed entered, {speed}, is very high for typewriter animation will not work.')

        timeout = 60 / speed

        for char in string:
            sleep(timeout)
            print(char, end='')
            sys.stdout.flush()
        print('\n')


if __name__ == '__main__':
    tp = TypewriterPrint()
    tp.print_tw("Hello World!")