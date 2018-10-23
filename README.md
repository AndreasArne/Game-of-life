# Game-of-life
Implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)

TO-DO:
* Implement web version
    - Add tests using headless server
    - Deploy
* Python
    - Re-write Turtle with [ontimer](https://docs.python.org/3.6/library/turtle.html#turtle.ontimer), so game loop is in GUI and not game.py.
    - Use decorator for tick function? https://realpython.com/primer-on-python-decorators/
    - Create tests before re-writing as objects!
    - Implement an object oriented version.
* Try other implementations of the algorithm.
* <s>Read starting gamefield from file so can test [patterns](https://en.wikipedia.org/wiki/Conway's_Game_of_Life#Examples_of_patterns)</s>
* <s>Pixel graphics for gamefield so not only showing 0 and 1. Using Turtle</s>
* <s>Try other GUI library, Turtle is slow!</s> Fixed by turning of animations and delays.
* <s>Inject pattern into size dimensional list instead of using using patterns size for gamefield</s>.
