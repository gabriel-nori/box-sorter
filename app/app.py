from app.models.box import sort

class App:
    def start(self, width: float, height: float, length: float, mass: float):
        print(sort(width, height, length, mass))