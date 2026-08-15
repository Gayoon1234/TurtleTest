from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

RGB_COLORS = [Color.RED.value, Color.GREEN.value, Color.BLUE.value]
 
# Follow constant naming conventions
SHOULD_DRAW_INSTANTLY = True