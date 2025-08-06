
class Box:
    # Constants for size
    BULKY_PACKAGE_VOLUME = 1000000
    BULKY_DIMENSION = 150
    HEAVY_MASS = 20

    # Constants for queue
    STANDARD_QUEUE_NAME = "STANDARD"
    SPECIAL_QUEUE_NAME = "SPECIAL"
    REJECTED_QUEUE_NAME = "REJECTED"
    QUEUE_POINTS = {
        0: STANDARD_QUEUE_NAME,
        1: SPECIAL_QUEUE_NAME,
        2: REJECTED_QUEUE_NAME
    }

    height: float = 0
    width: float = 0
    length: float = 0
    mass: float = 0

    def __init__(self, width: float, height: float, length: float, mass: float):
        if not(
            isinstance(width, (float, int)) and
            isinstance(height, (float, int)) and
            isinstance(length, (float, int)) and
            isinstance(mass, (float, int))
        ):
            raise Exception("Invalid format for measures. Please use only int and/or float")

        self.height = height
        self.width = width
        self.length = length
        self.mass = mass
    
    def _check_bulky(self) -> bool:
        """
        Returns if the package is bulky
        """

        return (
            self.height >= self.BULKY_DIMENSION or
            self.width >= self.BULKY_DIMENSION or
            self.length >= self.BULKY_DIMENSION or
            self.height * self.width * self.length >= self.BULKY_PACKAGE_VOLUME
        )

    def sort(self) -> str:
        """
        This method returns the name of the stack where the package should go
        """
        score: int = 0
        if self._check_bulky():
            score += 1
        
        if self.mass >= self.HEAVY_MASS:
            score += 1

        return self.QUEUE_POINTS[score]
    
def sort(width: float, height: float, length: float, mass: float):
    return Box(width, height, length, mass).sort()