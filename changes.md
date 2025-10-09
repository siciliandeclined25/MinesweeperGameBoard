**Minesweeper (feature/minesweeper)**
```
Initial Commit (v0.1)
Code written by Lucas Frias
```
**Changes**
- Added and created the minesweep.py file!
- Created a class to model Minesweeper
- Inside the class, added these new functions
    - __init__(self, mineCount, boardSize, autogenerate=True)
    - generateBoard(self)
    - calculateNeighbours(self)
    - badDisplay(self)
    - guess(self, boardPosition) - boardPosition being a number from 0 to boardSize^2 - 1

*Any changes are absolutely welcome!*\
**Feature To-Do List for Phase 0**:
- Create near neighbor recursive clearing functions
- Implement demonstratable clear visuals
- Create game loop from class
- Playtest and determine appropriate difficulty levels
- Create function for handling user given mines for IEEE demo
