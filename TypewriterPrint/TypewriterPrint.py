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
    def print_tw(string, speed=1500):
        """
        Method prints the input string with an animation.

        Args:
            speed (int): Speed of print, in characters per minute.
            string (str): A string to be printed.

        Returns: None

        """
        if speed < 200:
            raise UserWarning('Speed entered is {}, which is an invalid value.'.format(speed))
        elif speed > 20000:
            raise UserWarning('Speed entered, {}, is very high for typewriter animation will not work.'.format(speed))

        timeout = 60 / speed

        for char in string:
            sleep(timeout)
            print(char, end='')
            sys.stdout.flush()
            if char == '\n':
                sleep(0.5)
        sleep(1)
        print('\n')


if __name__ == '__main__':
    tp = TypewriterPrint()
    tp.print_tw("Hello World!\nThis is an example run. See what happens when we change a line"
                "\nSecond line", 1999)
