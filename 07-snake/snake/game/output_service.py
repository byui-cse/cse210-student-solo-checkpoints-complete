import sys
from game import constants
import raylibpy

class OutputService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """

    def open_window(self):
        raylibpy.init_window(constants.MAX_X, constants.MAX_Y, "Snake")
        raylibpy.set_target_fps(constants.FRAME_RATE)
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.begin_drawing()
        raylibpy.clear_background(raylibpy.WHITE)

    def draw_box(self, x, y, width, height):
        raylibpy.draw_rectangle(x, y, width, height, raylibpy.BLUE)

    def draw_text(self, x, y, text, is_dark_text):
        color = raylibpy.WHITE

        if is_dark_text:
            color = raylibpy.BLACK

        raylibpy.draw_text(text, x + 5, y + 5, 16, color)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        width = actor.get_width()
        height = actor.get_height()

        is_dark_text = True

        if width > 0 and height > 0:
            self.draw_box(x, y, width, height)
            is_dark_text = False
        
        if text != "":
            self.draw_text(x, y, text, is_dark_text)
        #self._screen.print_at(text, x, y, 7) # WHITE
        #raylibpy.draw_text(text, x, y, 16, raylibpy.BLUE)

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        raylibpy.end_drawing()
