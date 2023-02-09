class BoardClass:
    """
    Board class object.

    :arg userName user name of current player.
    """

    def __init__(self, userName: str = ""):
        self.__playerName__ = userName
        self.__lastTurn__ = ""
        self.__playerWins__ = 0
        self.__playerTies__ = 0
        self.__playerLosses__ = 0
        self.__gameBoard__ = [['', '', ''], ['', '', ''], ['', '', '']]
        self.__playerFinalData__ = {}

        # Use opposite player's wins as that players losses

    def getLastTurn(self):
        return self.__lastTurn__

    def updateGamesPlayed(self):
        """

        Keeps track how many games have started
        """
        __gamesPlayed__ = self.__playerTies__ + self.__playerLosses__ + self.__playerWins__
        return __gamesPlayed__

    def resetGameBoard(self):
        """
        Clear all the moves from game board in order to start new game.
        """
        self.__gameBoard__ = [['', '', ''], ['', '', ''], ['', '', '']]

    def isWinner(self):
        """
        Checks to see if the current player has won or lost and updates their respective counts.

        :returns Weather or not the current game has ended.
        """

        playerEndgame = False

        # gb stands for game board, just makes the variable name shorter
        # so that everything looks cleaner
        gbTemp = self.__gameBoard__

        if self.__playerName__ == 'player2':
            for row in gbTemp:
                if (row == ['o', 'o', 'o']) or (row == ['O', 'O', 'O']):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break

            column = 0
            while column < 3:
                if (gbTemp[0][column] == 'o' or gbTemp[0][column] == 'O') and (gbTemp[1][column] == 'o' or gbTemp[1][column] == 'O') and (gbTemp[2][column] == 'o' or gbTemp[2][column] == 'O'):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break
                elif (gbTemp[0][0] == 'o' or gbTemp[0][0] == 'O') and (gbTemp[1][1] == 'o' or gbTemp[1][1] == 'O') and (gbTemp[2][2] == 'o' or gbTemp[2][2] == 'O'):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break
                elif (gbTemp[0][2] == 'o' or gbTemp[0][2] == 'O') and (gbTemp[1][1] == 'o' or gbTemp[1][1] == 'O') and (gbTemp[2][0] == 'o' or gbTemp[2][0] == 'O'):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break
                column += 1

        else:
            for row in gbTemp:
                if (row == ['x', 'x', 'x']) or (row == ['X', 'X', 'X']):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break

            column = 0
            while column < 3:
                if (gbTemp[0][column] == 'x' or gbTemp[0][column] == 'X') and (gbTemp[1][column] == 'x' or gbTemp[1][column] == 'X') and (gbTemp[2][column] == 'x' or gbTemp[2][column] == 'X'):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break
                elif (gbTemp[0][0] == 'x' or gbTemp[0][0] == 'X') and (gbTemp[1][1] == 'x' or gbTemp[1][1] == 'X') and (gbTemp[2][2] == 'x' or gbTemp[2][2] == 'X'):
                    playerEndgame = True
                    # playerWon = True
                    self.__playerWins__ += 1
                    break
                elif (gbTemp[0][2] == 'x' or gbTemp[0][2] == 'X') and (gbTemp[1][1] == 'x' or gbTemp[1][1] == 'X') and (gbTemp[2][0] == 'x' or gbTemp[2][0] == 'X'):
                    # playerWon = True
                    playerEndgame = True
                    self.__playerWins__ += 1
                    break
                column += 1

        """
        Player loss section
        """

        if self.__playerName__ == 'player2':
            for row in gbTemp:
                if (row == ['x', 'x', 'x']) or (row == ['X', 'X', 'X']):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break

            column = 0
            while column < 3:
                if (gbTemp[0][column] == 'x' or gbTemp[0][column] == 'X') and (gbTemp[1][column] == 'x' or gbTemp[1][column] == 'X') and (gbTemp[2][column] == 'x' or gbTemp[2][column] == 'X'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                elif (gbTemp[0][0] == 'x' or gbTemp[0][0] == 'X') and (gbTemp[1][1] == 'x' or gbTemp[1][1] == 'X') and (gbTemp[2][2] == 'x' or gbTemp[2][2] == 'X'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                elif (gbTemp[0][2] == 'x' or gbTemp[0][2] == 'X') and (gbTemp[1][1] == 'x' or gbTemp[1][1] == 'X') and (gbTemp[2][0] == 'x' or gbTemp[2][0] == 'X'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                column += 1

        else:

            for row in gbTemp:

                if (row == ['o', 'o', 'o']) or (row == ['O', 'O', 'O']):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break

            column = 0
            while column < 3:
                if playerEndgame is True:
                    break
                if (gbTemp[0][column] == 'o' or gbTemp[0][column] == 'O') and (gbTemp[1][column] == 'o' or gbTemp[1][column] == 'O') and (gbTemp[2][column] == 'o' or gbTemp[2][column] == 'O'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                elif (gbTemp[0][0] == 'o' or gbTemp[0][0] == 'O') and (gbTemp[1][1] == 'o' or gbTemp[1][1] == 'O') and (gbTemp[2][2] == 'o' or gbTemp[2][2] == 'O'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                elif (gbTemp[0][2] == 'o' or gbTemp[0][2] == 'O') and (gbTemp[1][1] == 'o' or gbTemp[1][1] == 'O') and (gbTemp[2][0] == 'o' or gbTemp[2][0] == 'O'):
                    playerEndgame = True
                    # playerLoss = True
                    self.__playerLosses__ += 1
                    break
                column += 1
        return playerEndgame

    def boardIsFull(self):
        """
        Checks if the board is full (tie). Updates the ties count.

        :returns Weather the board is full or not.
        """
        boardFull = True
        outerLoopBreak = False
        boardFullCheckGameBoard = self.__gameBoard__
        for row in boardFullCheckGameBoard:
            for space in row:
                outerLoopBreak = False
                if space == '':
                    boardFull = False
                    outerLoopBreak = True
                    break
                elif (space == 'x') or (space == 'X') or (space == 'o') or (space == 'O'):
                    pass
                else:
                    print('Unexpected character in game board found')
            if outerLoopBreak == True:
                break

            if boardFull is False:
                break

        if boardFull is True:
            self.__playerTies__ += 1

        return boardFull


    def printStats(self, player1Name, player2Name):
        """
        :param player1Name is player 1's user name.
        :param player2Name is player 2's user name.

        Given player1's user name and player2's user name sets __playerFinalData__ variable and prints the following
        each on a new line:

        Prints the players user name.
        Prints the user name of the last person to make a move.
        prints the number of games.
        Prints the number of wins.
        Prints the number of losses.
        Prints the number of ties.
        """
        __playerGames__ = self.__playerTies__ + self.__playerLosses__ + self.__playerWins__
        print('User Name:', self.__playerName__)
        if self.__lastTurn__ == 'player2':
            print('Last player to take turn:', player2Name)
        elif self.__lastTurn__ == 'player1':
            print('Last player to take turn: ', player1Name)
        print('Number of games played: ', __playerGames__)
        print('Number of wins: ', self.__playerWins__)
        print('Number of losses: ', self.__playerLosses__)
        print('Number of ties: ', self.__playerTies__)
        self.__playerFinalData__ = {'user name': self.__playerName__,
                                    'last turn': self.__lastTurn__,
                                    'player wins': self.__playerWins__,
                                    'player ties': self.__playerTies__,
                                    'player losses': self.__playerLosses__,
                                    'games played': __playerGames__
                                    }

    def getPlayerFinalData(self):
        """
        :returns __playerFinalData__
        """
        return self.__playerFinalData__

    def getUserName(self):
        """
        Gets the Username of player. DEBUG ONLY.

        :returns User name of player.
        """
        return self.__playerName__

    def setGameBoard(self):
        """
        Returns current game board. DEBUG ONLY.

        :returns Current game board.
        """
        return self.__gameBoard__

    def gameBoardHandling(self, coordinates, friendOrFoe):
        """
        Uses given coordinates and weather it is player or opponent's turn to fill in the board if the move is valid.

        :param coordinates: coordinates to fill on board
        :param friendOrFoe: Indicates weather player or opponent's coordinates are being passed
        :returns: Returns weather or not the coordinates provided are valid by checking if entered space is available.
        """
        cordinatesValid = True
        print(coordinates)
        xval = coordinates[0]
        yval = coordinates[1]
        print(xval)
        print(yval)
        xCordinates = int(xval) - 1
        yCordinates = int(yval) - 1
        currentBoard = self.__gameBoard__

        if friendOrFoe == 'friend':
            if currentBoard[xCordinates][yCordinates] == '':
                if self.__playerName__ == 'player2':
                    currentBoard[xCordinates][yCordinates] = 'O'
                    self.__lastTurn__ = "player2"
                else:
                    currentBoard[xCordinates][yCordinates] = 'X'
                    self.__lastTurn__ = "player1"
                print('Move Valid')
            else:
                print('Space Already filled')
                cordinatesValid = False
                raise ValueError

        elif friendOrFoe == 'foe':
            if currentBoard[xCordinates][yCordinates] == '':
                if self.__playerName__ == 'player2':
                    currentBoard[xCordinates][yCordinates] = 'X'
                    self.__lastTurn__ = "player1"
                else:
                    currentBoard[xCordinates][yCordinates] = 'O'
                    self.__lastTurn__ = "player2"
                print('Move Valid')
            else:
                print('Space Already filled, see opponent')
                cordinatesValid = False
                # raise ValueError

        print(currentBoard[0])
        print(currentBoard[1])
        print(currentBoard[2])
        return cordinatesValid


def userCordinatesEntry():
    """
    Has player input coordinates for a move then processes them into a usable format to be sent trhough sockets.

    :returns: A processed version of the coordinates.
    """
    while True:
        playerMoveCoordinatesX = input('Enter X input:')
        if playerMoveCoordinatesX == '1' or playerMoveCoordinatesX == '2' or playerMoveCoordinatesX == '3':
            break
        else:
            print('invalid input')
    while True:
        playerMoveCoordinatesY = input('Enter Y input:')
        if playerMoveCoordinatesY == '1' or playerMoveCoordinatesY == '2' or playerMoveCoordinatesY == '3':
            break
        else:
            print('invalid input')
    playerCoordinates = playerMoveCoordinatesX + playerMoveCoordinatesY
    return playerCoordinates


if __name__ == '__main__':
    print('You should not run this file as main unless debugging :/')
    print('Or if your someone who knows more than I do :)')
