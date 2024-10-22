# Wave Function Collapse with Text

This script is a demo implimentation of the wave function collapse algorithm used for generating tilemap environments based on a set of constraints.

Created to help myself understand the algorithm, I also wanted to test and see if there was a way to provide a seed to make the result deterministic.

## Usage

running the script with:

```
    seed = 1
    generator = WaveFunctionCollapse(seed)

    tile_map = generator.generate(35, 20)

    print(f"Map generated with seed: {seed}")
    print(generator.render_map(tile_map))
```

will print:

```
Map generated with seed: 1
💧🌱🌱🌷🌲🌱🌱🏖️🌲🌱🌱🌱🌱🌱🏖️🌱🌷🌱🏖️🌲🌲🌱🌷🌱🌱🌱🌲🌱🌲🌷🌱🌱🌱🌱🏖️
🏖️🏖️🌲🌲🌱🏖️🏖️🏖️🌱🌲🌲🌱🌷🏖️🏖️💧🌱🏖️🏖️🌱🌲🌲🌲🌱🌷🌷🌱🌱🌲🌲🌱🌲🌷🌲🏖️
🌲🌱🌱🏖️💧💧🌱🏖️🌱🌲🌱🌱🌱💧💧💧🌱🌱🌲🌱🌱🌱🌱🏖️🏖️🌱🌱🌷🌱🌱🌲🌲🌲🌲🌱
🌱🌷🌲🌱🏖️💧🌱🏖️🌱🌱🌱🌷🌲🏖️🏖️🏖️🏖️🌷🌱🌱🌲🌱💧🏖️🌱🌲🌲🌱🌱🌲🌱🌲🌱🌷🌲
🌲🌷🌱🏖️🏖️🌱💧💧💧💧🌱🏖️🏖️💧💧💧🏖️🌷🌱🌲🌲🌱💧💧🏖️🏖️🏖️💧🌱🌲🌱🌱🏖️🌱🌱
🌲🌱🏖️💧🏖️🏖️💧💧🏖️🌱🌱💧💧🏖️💧💧💧🌱🏖️🌲🌱🌱🌱💧💧💧🏖️💧🏖️🌱🌱🌱🌱🌱🌱
🌱🏖️🏖️💧💧🏖️💧💧🌱🌲🌱🏖️🏖️🌷🏖️🏖️🏖️🌱🌱🌷🌱🌱🌱🌱💧💧🏖️🏖️🌱🌲🌱🌲🌱🏖️🌲
🌱🌱🏖️🏖️🌱🏖️💧🏖️🌲🌲🌲🌲🌲🌱💧💧🏖️🌱🌱🌱🌱🌷🌷🌱💧🏖️🌱🌱🌱🌲🌱🌲🌷🏖️🏖️
🌷🌱🌱🌷🌱🌱🏖️🌱🌱🌱🌱🌱🌱🌲🏖️💧💧🏖️🏖️🏖️🌱🌱🌱🌱🌱🏖️🌱🌱💧🏖️🌱🌲🏖️🏖️🏖️
🌱🌲🌲🌲🌱🌲🌲🌱🌲🏖️🌱🌷🌱🌲🌱💧💧🏖️🏖️🏖️🏖️💧🌱🌷🌱🏖️🌱🌷🌱🌲🌱🌷🏖️🌷🌱
🌷🌱🌱🌱🌲🌱🌷🌷🌷🌷🏖️🏖️🌱🌱🌷🏖️💧💧💧💧💧💧🌱🌱🌱🏖️🏖️🌱🌱🌱🌱🌱💧🌱🌲
🌱🌲🌱🌱🌱🌲🌱🌲🌱🌱💧🏖️🌷🌲🌱🏖️💧💧💧💧💧💧🌱🌱🏖️🏖️💧🌱🌱🏖️🏖️🌱🌱🌱🌲
🌱🏖️💧💧💧🌱🌲🌱🌱🌱💧🏖️🌲🌱💧💧🏖️💧💧🏖️💧🏖️🌲🏖️🏖️🏖️🏖️🌱🌱🌱🏖️🌱🌷🌱🌲
🏖️💧💧💧💧🏖️🌱🌲🌲🌱💧🌱🌲🌱💧💧🏖️💧💧💧💧🏖️🏖️💧🏖️🏖️🌱🌲🌱🌱🏖️🌱🌱💧🌱
🏖️🏖️🏖️🌱🌱🌷🏖️🌱🏖️💧🌱🌲🌱🌱💧🏖️🏖️🏖️💧💧🏖️🌲🌱🌱🌱🏖️💧🌱🌱🌲🏖️🌱🌱🌱🌱
🌱🏖️🌱🌷🌱🌱🏖️🌱🌱🌱🌷🌱🏖️🏖️🏖️🏖️🏖️🌱🌱🌱🏖️🌲🌱🌱🌱🌱💧🌱🏖️🏖️🏖️🏖️🌲🌱🌲
🌱🌲🌲🌲🌱🌱🏖️🌱🌷🌷🌲🌱🏖️🌱🌱🏖️🏖️🌱🌱🏖️🌱🌱💧🌱🌲🌱🌱🌷🏖️🏖️💧💧🌱🌲🌱
🌲🌱🌱🌱🌷🌱🌱🏖️🏖️🏖️🌱🏖️🏖️🌱🌱💧💧💧🏖️🏖️🏖️💧💧🏖️🌱🌱💧🏖️🌱🌱🌱🌱🌱🌱🏖️
🌷🏖️🌱🌱🌱🌷🌱💧💧💧🏖️🌷🌱🌲🌲🌱💧💧🌱🌱🌱💧💧💧🏖️🏖️💧🏖️🌱🌷🌷🌱🌱🌲🌱
🌲🌱🌷🌱🏖️🏖️💧💧💧🏖️🏖️🌱🏖️🏖️🌱🌱🏖️💧🌱🌱🌱🌱🏖️🏖️💧💧🌱🌱🏖️🌱🌱🌲🌱🌷🌲
```

adjusting the rules, tiles and seed will produce different results:

```
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
```

tiles can be any string not just emojis, but keep the text length == 1 to ensure the grid.