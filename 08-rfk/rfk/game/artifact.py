from game.actor import Actor
from game import constants

class Artifact(Actor):
    def __init__(self):
        super().__init__()

        self._description = ""
        self.set_width(constants.DEFAULT_BLOCK_SIZE)
        self.set_height(constants.DEFAULT_BLOCK_SIZE)

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def has_description(self):
        return self._description != ""