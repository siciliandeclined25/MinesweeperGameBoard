##########################
# MINESWEEPER GAMEBOARD  #
# CLASS BY LUCAS FRIAS   #
############################
#modules
import random

class Minesweeper:
    """A class representing a Minesweeper game board and game functions/logic"""
    def __init__(self, mineCount: int, boardSize = 8, autoGenerate=True) -> None:
        """Initialize the class constructor and define all variables"""
        #this variable defnes the default dictionary
        # tree used for each tile on the game board
        self.defaultDictionary = {
            "discovered": False,
            "flagged": False,
            "mine": False,
            "neighbours": 0
        }
        #create a symetrical board from the size
        #this is arranged (rows) of columns
        self.board = [[self.defaultDictionary.copy() for _ in range(boardSize)] for _ in range(boardSize)]
        self.mineCount = mineCount
        self.boardSize = boardSize
        #here's some type declaration of different types of events
        self.explosion = "boom!"
        #this is only set if autogenerate is true, then we
        #generate the board with mines
        if autoGenerate:
            self.generateBoard()
    def generateBoard(self, safeSpaces = []):
        """Generates a board with mines after a given input is used to start"""
        #this statement generates a list of random integers given the value of
        # the boardsize times itself (symmetrical board)
        randomIntegers = [random.randint(0, (self.boardSize*self.boardSize)-1) for _ in range(self.mineCount)]
        #let's iterate through every value!!!
        # and assign our amazing mines into
        # amazinger loccations of the dictionary
        for mineLocation in randomIntegers:
            if mineLocation in safeSpaces:
                #whoops this is a safe space where the user started
                #add a random number that is hopefully new
                randomIntegers.append(random.randint(0, (self.boardSize*self.boardSize)-1))
                continue #make sure to remove the mine from a safe space if true
            #let's assign the mine location to the board
            # which is integer division for the row(rounds down) + remainder of division

            self.board[mineLocation//8][mineLocation%8]["mine"] = True
        #time to calculate the neighbours....
        self.calculateNeighbours()
    def calculateNeighbours(self):
        """Calculates the number of neighbours for each tile"""
        #bella would be so proud of this function
        # okay so first each row
        for row in range(self.boardSize):
            #each column
            for col in range(self.boardSize):
                #mines can't have friends!
                if self.board[row][col]["mine"]:
                    continue
                #otherwise let's iterate
                for i in range(-1, 2):
                    #for each of our immediate close neighbours in i
                    for j in range(-1, 2):
                        #same with j
                        # okay so basically we check first that row + i is within bounds
                        # because we don't want to loop to a non-existant tile
                        # the same thing with the next part of the boolean expression with j
                        # then we check if the tile being analyzed i and j is a mine
                        # if true just increment
                        if 0 <= row + i < self.boardSize and 0 <= col + j < self.boardSize and self.board[row + i][col + j]["mine"]:
                            self.board[row][col]["neighbours"] += 1
                        #the secret sauce is in the range function as we go to each neighbour
                        # and evaluate what the value inside of it is in every point or instance
    def badDisplay(self):
        """Displays the board in a bad way"""
        for row in self.board:
            print(" ".join([str(tile["neighbours"]) if tile["mine"] == False else "X" for tile in row]))
    def guess(self, guess):
        """Guesses the area of the board given an integer guess 0-63 that will then be processed"""
        if guess < 0 or guess > 63:
            raise ValueError("Guess must be between 0 and 63")
        row = guess // self.boardSize
        col = guess % self.boardSize
        spotChosen = self.board[row][col]
        #make sure we haven't done this before
        if spotChosen["discovered"]:
            return False
        #make sure that isn't not a bomb!!
        if spotChosen["mine"]:
            #boom, return boom. boom boom
            return self.explosion
        #okay now we need to clear everything around us and check if they are a bom
        #this list is for the 0 neighbors that we need to
        #look through because after a guess if the value is 0 let's
        # loop through all values
        futureZeroNeighborsToIterateThrough = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                #okay look at above for the explanation of this code in calculateNeighbours
                if 0 <= row + i < self.boardSize and 0 <= col + j < self.boardSize and self.board[row + i][col + j]["mine"]:
                    self.board[row][col]["discovered"] = True
                    #if there's no neighbors add me to the no neighbors list
                    if self.board[row][col]["neighbours"] == 0:
                        print("true")
                        futureZeroNeighborsToIterateThrough.append(self.board[row + i][col + j])
        for zeroNeighborPoints in futureZeroNeighborsToIterateThrough:
            print(zeroNeighborPoints)
ms = Minesweeper(mineCount=10)
ms.badDisplay()
ms.guess(12)
