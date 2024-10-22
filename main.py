import random
from typing import List


class WaveFunctionCollapse:
    def __init__(self, seed: int = None):
        self.seed = seed if seed is not None else random.randint(0, 999999)
        self.rng = random.Random(self.seed)

        # emojis represent tiles
        self.tiles = {
            'grass': '🌱',
            'water': '💧',
            'tree': '🌲',
            'sand': '🏖️',
            'flower': '🌷'
        }

        self.rules = {
            'grass': {'grass': 0.8, 'water': 0.1, 'tree': 0.6, 'sand': 0.3, 'flower': 0.4},
            'flower': {'grass': 0.4, 'water': 0.0, 'tree': 0.2, 'sand': 0.1, 'flower': 0.1},
            'water': {'grass': 0.1, 'water': 0.9, 'tree': 0.0, 'sand': 0.4, 'flower': 0.0},
            'tree': {'grass': 0.6, 'water': 0.0, 'tree': 0.4, 'sand': 0.1, 'flower': 0.2},
            'sand': {'grass': 0.3, 'water': 0.4, 'tree': 0.1, 'sand': 0.7, 'flower': 0.1},
        }

    # calc probability of a tile fitting at a position based on neighbors
    def calculate_tile_probability(self, x: int, y: int, tile: str, grid: List[List[str]]) -> float:
        height, width = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        probability = 1.0
        neighbors = 0

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != None:
                neighbor_tile = grid[new_x][new_y]
                probability *= self.rules[tile][neighbor_tile]
                neighbors += 1

        # no neighbors return neutral probability
        return probability if neighbors > 0 else 0.5

    def generate(self, width: int, height: int) -> List[List[str]]:
        grid = [[None for _ in range(width)] for _ in range(height)]

        # start with a random tile in the middle
        mid_x, mid_y = height // 2, width // 2
        grid[mid_x][mid_y] = self.rng.choice(list(self.tiles.keys()))

        # keep track of cells to fill
        to_fill = [(i, j) for i in range(height) for j in range(width) if grid[i][j] is None]
        self.rng.shuffle(to_fill)

        # fill grid
        for x, y in to_fill:
            probabilities = {}
            for tile in self.tiles.keys():
                probabilities[tile] = self.calculate_tile_probability(x, y, tile, grid)

            # normalize probabilities
            total = sum(probabilities.values())
            if total > 0:
                probabilities = {k: v / total for k, v in probabilities.items()}
            else:
                probabilities = {k: 1 / len(self.tiles) for k in self.tiles.keys()}

            # choose tile based on probabilities
            choices, weights = zip(*probabilities.items())
            grid[x][y] = self.rng.choices(choices, weights=weights, k=1)[0]

        return grid

    # demo render func, to see results printed to console
    def render_map(self, tile_map: List[List[str]]) -> str:
        result = []
        for row in tile_map:
            result.append(''.join(self.tiles[tile] for tile in row))
        return '\n'.join(result)



if __name__ == "__main__":
    seed = 1
    generator = WaveFunctionCollapse(seed)

    tile_map = generator.generate(35, 20)

    print(f"Map generated with seed: {seed}")
    print(generator.render_map(tile_map))