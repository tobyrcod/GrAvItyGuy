from utils import *


class Tile:
    def __init__(self, name: str, color: tuple):
        self.name = name
        self.color = color
        self.dimensions = pygame.Vector2(1, 1)

    def to_json(self):
        return json.dumps({
            'name': self.name,
            'color': self.color,
            'dimensions': self.color
        })

    def from_json(self, json_tile):
        data = json.load(json_tile)
        self.name = data.name
        self.color = data.color
        self.dimensions = data.dimensions
