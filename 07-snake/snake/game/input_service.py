import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._current = Point(1, 0)
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        if self.is_left_pressed():
            self._current = Point(-1, 0)
        elif self.is_right_pressed():
            self._current = Point(1, 0)
        elif self.is_up_pressed():
            self._current = Point(0, -1)
        elif self.is_down_pressed():
            self._current = Point(0, 1)

        return self._current

    def is_left_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_LEFT)

    def is_right_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_RIGHT)

    def is_up_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_pressed(raylibpy.KEY_DOWN)

    def window_should_close(self):
        return raylibpy.window_should_close()
