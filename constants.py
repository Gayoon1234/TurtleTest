from enum import Enum

class Color(Enum):
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    WHITE = "white"

RGB_COLORS = [Color.RED.value, Color.GREEN.value, Color.BLUE.value]
ROYAL_COLORS = [Color.BLUE.value, Color.PURPLE.value, Color.RED.value]

 
# Follow constant naming conventions
SHOULD_DRAW_INSTANTLY = True