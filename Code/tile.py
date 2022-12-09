from utils import *


class Tile:
    def __init__(self, name: str, color: tuple):
        self.name = name
        self.color = color

    def save(self):
        with open(f'tile_{self.name}.json', 'w') as outfile:
            json.dump({
                'name': self.name,
                'color': self.color,
            }, outfile)
            print(f'{outfile.name} saved successfully')

    @staticmethod
    def load(filename):
        with open(f'tile_{filename}.json') as json_file:
            data = json.load(json_file)
            tile = Tile(*data.values())
            print(f'{json_file.name} loaded successfully')
            return tile

