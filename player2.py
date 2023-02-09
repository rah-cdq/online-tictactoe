import tkinter as tk
import socket
import gameboard


class P2IntroUIPacker:
    """
    Intro screen class object TK inter Gui to enter IP address, port, and username.
    """
    def __init__(self):
        self.address = ''
        self.port = None
        self.username = ''
        self.resultLabel = ''

        self.canvasSetup()
        self.initTKVariables()
        # self.returnKeyBind()

        self.createOverallLabel()

        self.createAddressEntry()

        self.createPortEntry()

        self.createUsernameEntry()

        self.createSubmitButton()
        self.createResultLabel()
        self.createQuitButton()
        self.runUI()

    def initTKVariables(self):
        """
        Sets the TK inter variables for this GUI class
        """
        self.address = tk.StringVar()
        self.port = tk.IntVar()
        self.username = tk.StringVar()
        self.result = tk.StringVar()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Intro Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createQuitButton(self):
        """
        Creates a quit button, usually used for debugging.
        """
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy).pack()

    def createOverallLabel(self):
        """
        Creates a label to indicate this is Tic Tac Toe.
        """
        self.overallLabel = tk.Label(self.master, text="Tic Tac Toe Game")
        self.overallLabel.pack()

    def createAddressEntry(self):
        """
        Creates a text box to enter IP address.
        """
        self.addressEntry = tk.Entry(self.master, textvariable=self.address, width=30)
        self.addressEntry.insert(0, "Enter IP Address or Host Name:")
        self.addressEntry.pack()
        """Get Rid of Zero"""

    def createPortEntry(self):
        """
        Creates a text box to enter port.
        """
        self.portEntry = tk.Entry(self.master, textvariable=self.port)
        self.portEntry.insert(0, "Enter Port:")
        self.portEntry.pack()
        """Get Rid of Zero"""

    def createUsernameEntry(self):
        """
        Creates a text box to enter user name.
        """
        self.usernameEntry = tk.Entry(self.master, textvariable=self.username, width=45)
        self.usernameEntry.insert(0, "Enter Username (Alpha-numeric values ONLY):")
        self.usernameEntry.pack()

    def updateIntroValues(self):
        """
        Retrieves values from text boxes and destroys GUI.
        """
        self.address = self.addressEntry.get()
        self.port = self.portEntry.get()
        self.username = self.usernameEntry.get()
        self.master.destroy()

    def getAddress(self):
        """
        :returns IP address.
        """
        return self.address

    def getPort(self):
        """
        :returns Port.
        """
        return self.port

    def getUsername(self):
        """
        :returns User name.
        """
        return self.username

    def createSubmitButton(self):
        """
        Creates a button to submit text box values.
        """
        self.submitButton = tk.Button(self.master, text="Submit", command=self.updateIntroValues).pack()

    def createResultLabel(self):
        """
        Creates blank label for aesthetic purposes.
        """
        self.result.set('')
        self.resultLabel = tk.Label(self.master, textvariable=self.result, width=25).pack()

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


class P2GameBoardGrid:
    """
    Game board class object TK inter Gui for the player to play Tic Tac Toe on.
    """
    def __init__(self):
        self.canvasSetup()

        self.button11 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection11)
        self.button11.grid(padx=60, pady=25)
        self.button12 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection12)
        self.button12.grid(padx=60, pady=25)
        self.button13 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection13)
        self.button13.grid(padx=60, pady=25)
        self.button21 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection21)
        self.button21.grid(row=0, column=1)
        self.button22 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection22)
        self.button22.grid(row=1, column=1)
        self.button23 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection23)
        self.button23.grid(row=2, column=1)
        self.button31 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection31)
        self.button31.grid(row=0, column=2, padx=60)
        self.button32 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection32)
        self.button32.grid(row=1, column=2, padx=60)
        self.button33 = tk.Button(self.master, width=15, height=7, text='', command=self.player2Selection33)
        self.button33.grid(row=2, column=2, padx=60)

        self.turnLabel = tk.Label(self.master, width=17, height=3, text="Current Player's turn:")
        self.turnLabel.grid(row=3, column=0)
        self.turnButton = tk.Label(self.master, width=17, height=3, text=opponentUserName)
        self.turnButton.grid(row=3, column=1)
        self.startingTurn()
        self.coordinates = ()
        self.player1Coordinates = ''
        self.runUI()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        # self.master = tk.Tk()
        self.master = tk.Tk()
        self.master.title("P2 Game Screen")  # sets the window title
        self.master.geometry('600x600')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def recivingGameStatusPlayer2(self, opponentUserNameEndGame):
        """
        Checks if current game is over and calls appropriate functions to update board class counts.


        :param opponentUserNameEndGame: Player 1's username for debugging purposes mostly.
        :return: Weather or not the current game has ended so undesired code does not run.
        """
        nextGame = False
        if (player2BoardData.isWinner() is True) or (player2BoardData.boardIsFull() is True):
            # = clientSocket.recv(1024)
            player2BoardData.printStats(opponentUserNameStr, player2UserName)
            self.disableAllButtons()
            lastUI = P2EndBoardPacker()
            print('listening')
            gameEndTempMessage = clientSocket.recv(1024)
            print('got')
            gameEndMessage = gameEndTempMessage.decode('ascii')
            print(gameEndMessage)
            if gameEndMessage == 'Game Continues':
                pass
            elif gameEndMessage == 'Play Again':
                print(gameEndMessage)
                P2PlayAgainPacker()

                player2BoardData.resetGameBoard()
                self.resetBoard()

                nextGame = True
                return nextGame
            elif gameEndMessage == 'Fun Times':
                P2FunTimesPacker()
                print(gameEndMessage)
                self.master.destroy()

                exit()
        return nextGame

    def resetBoard(self):
        """
        Resets board to its original state.
        """
        self.turnButton["text"] = opponentUserNameStr

        self.button11["text"] = ""
        self.button11["state"] = "active"
        self.button12["text"] = ""
        self.button12["state"] = "active"
        self.button13["text"] = ""
        self.button13["state"] = "active"

        self.button21["text"] = ""
        self.button21["state"] = "active"
        self.button22["text"] = ""
        self.button22["state"] = "active"
        self.button23["text"] = ""
        self.button23["state"] = "active"

        self.button31["text"] = ""
        self.button31["state"] = "active"
        self.button32["text"] = ""
        self.button32["state"] = "active"
        self.button33["text"] = ""
        self.button33["state"] = "active"
        self.turnDisplay(opponentUserNameStr)

        self.master.update()
        self.startingTurn()

    def disableAllButtons(self):
        """
        Disables all buttons on the board.
        """

        self.button11["state"] = "disabled"

        self.button12["state"] = "disabled"

        self.button13["state"] = "disabled"

        self.button21["state"] = "disabled"

        self.button22["state"] = "disabled"

        self.button23["state"] = "disabled"

        self.button31["state"] = "disabled"

        self.button32["state"] = "disabled"

        self.button33["state"] = "disabled"

    def turnDisplay(self, turn):
        """
        Sets text on the label that indicates who's turn it is

        :param turn: indicates who's turn it is.
        """
        if turn == opponentUserNameStr:
            self.turnButton["text"] = opponentUserNameStr
        else:
            self.turnButton["text"] = player2UserName

    def startingTurn(self):
        """
        Waits to receive player 1's initial move.
        """
        opponentMove = clientSocket.recv(1024)
        opponentMoveStr = opponentMove.decode('ascii')
        player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')

        self.player1selection(opponentMoveStr)
        self.recivingGameStatusPlayer2(player2UserName)
        self.turnDisplay(player2BoardData)

    def player2Selection11(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button11["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button11["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection12(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '2')
        coordinatesFixed = self.coordinates[1] + self.coordinates[0]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button12["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button12["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection13(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button13["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button13["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection21(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button21["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button21["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection22(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('2', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button22["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button22["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection23(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button23["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button23["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection31(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button31["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button31["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection32(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('2', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button32["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button32["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def player2Selection33(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player2BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button33["text"] = "O"
            clientSocket.send(coordinatesFixed.encode())
            self.button33["state"] = "disabled"

            a = self.recivingGameStatusPlayer2(opponentUserNameStr)
            if a is False:
                self.turnDisplay(opponentUserNameStr)
                self.master.update()
                opponentMove = clientSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player2BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player1selection(opponentMoveStr)

                self.recivingGameStatusPlayer2(opponentUserNameStr)
                self.turnDisplay(player2UserName)
                self.master.update()

    def destroyP2GameBoardGrid(self):
        """
        Destroys game board grid, mostly for debugging purposes.
        """
        self.master.destroy()

    def player1selection(self, selector):
        """
        Handles putting opponent's move on the board.

        :param selector: coordinates of opponent's move
        """
        if selector == '11':
            self.button11["text"] = "X"
            self.button11["state"] = "disabled"
        if selector == '21':
            self.button12["text"] = "X"
            self.button12["state"] = "disabled"
        if selector == '31':
            self.button13["text"] = "X"
            self.button13["state"] = "disabled"
        if selector == '12':
            self.button21["text"] = "X"
            self.button21["state"] = "disabled"
        if selector == '22':
            self.button22["text"] = "X"
            self.button22["state"] = "disabled"
        if selector == '32':
            self.button23["text"] = "X"
            self.button23["state"] = "disabled"
        if selector == '13':
            self.button31["text"] = "X"
            self.button31["state"] = "disabled"
        if selector == '23':
            self.button32["text"] = "X"
            self.button32["state"] = "disabled"
        if selector == '33':
            self.button33["text"] = "X"
            self.button33["state"] = "disabled"

    def setPlayer1Coordinates(self, coordinates=''):
        self.player1Coordinates = coordinates

    def getCoordinates(self):
        """
        Gets coordinates of player 2.
        """
        return self.coordinates

    def runUI(self):
        """
        Starts UI loop.
        """
        self.master.mainloop()
        # starts my UI - event handler


class P2EndBoardPacker:
    """
    End screen class object TK inter GUI for the player's end screen during tic tac toe.
    """
    def __init__(self):
        self.message = ''

        self.userInfo = {}
        self.canvasSetup()
        self.createOverallLabel()
        self.messageLabel = tk.Label(self.master, text=self.message)
        self.messageLabel.pack()

        self.quitButton = tk.Button(self.master, text="Click to get message", command=self.quitButtonP2EndUI)
        self.quitButton.pack()

        self.runUI()

    def quitButtonP2EndUI(self):
        """
        Handles what happens when quit button is clicked.
        """
        self.master.quit()
        self.master.destroy()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Final Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createOverallLabel(self):
        """
        Creates label to display final results.
        """
        self.userInfo = player2BoardData.getPlayerFinalData()
        if self.userInfo['last turn'] == 'player2':
            lastTurnFixed = player2UserName
        else:
            lastTurnFixed = opponentUserNameStr

        finalText = "Username: " + player2UserName + '\n' + \
                    'Last player to take turn: ' + lastTurnFixed + '\n' + \
                    'Wins: ' + str(self.userInfo['player wins']) + '\n' + \
                    'losses:' + str(self.userInfo['player losses']) + '\n' + \
                    'ties:' + str(self.userInfo['player ties']) + '\n' + \
                    'Games Played:' + str(self.userInfo['games played']) + '\n'
        self.overallLabel = tk.Label(self.master, text=finalText).pack()

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


class P2PlayAgainPacker:
    """
    Epilogue screen class object TK inter GUI for the player's end screen after message play again is received.
    """
    def __init__(self):
        self.message = 'Play Again'
        self.canvasSetup()
        self.messageLabel = tk.Label(self.master, text=self.message)
        self.messageLabel.pack()
        self.onlyButton = tk.Button(self.master, text="Click to continue", command=self.onlyButtonHandaling)
        self.onlyButton.pack()
        self.runUI()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Play Again Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def onlyButtonHandaling(self):
        """
        Handles what happens if player selects continue button.
        """
        self.master.quit()
        self.master.destroy()

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


class P2FunTimesPacker:
    """
    Epilogue screen class object TK inter GUI for the player's end screen after message fun times is received.
    """
    def __init__(self):
        self.message = 'Fun Times'
        self.canvasSetup()
        self.messageLabel = tk.Label(self.master, text=self.message)
        self.messageLabel.pack()
        self.onlyButton = tk.Button(self.master, text="Click to continue", command=self.onlyButtonHandaling)
        self.onlyButton.pack()
        self.runUI()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Play Again Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def onlyButtonHandaling(self):
        """
        Handles what happens if player selects continue button.
        """
        self.master.quit()
        self.master.destroy()

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


if __name__ == '__main__':

    userNameCheckSentinelValue = False
    while True:
        introUserInterface = P2IntroUIPacker()
        provisionalUserName2 = introUserInterface.getUsername()
        for alphaNum in provisionalUserName2:
            if (alphaNum.isnumeric() is True) or (alphaNum.isspace() is True) or (alphaNum.isalpha() is True):
                userNameCheckSentinelValue = True

            else:
                userNameCheckSentinelValue = False


        serverAddress = introUserInterface.getAddress()
        try:
            serverPort = int(introUserInterface.getPort())
            userNameCheckSentinelValue = True
        except Exception:
            userNameCheckSentinelValue = False
        if userNameCheckSentinelValue is True:
            break

    # Creates host server object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binds IP & port
    serverSocket.bind((serverAddress, serverPort))

    # Begin listening for opponent
    # 1 is max number of connections at a given time
    serverSocket.listen()
    clientSocket, clientAddress = serverSocket.accept()

    player2BoardData = gameboard.BoardClass('player2')
    player2UserName = provisionalUserName2

    opponentUserName = clientSocket.recv(1024)
    opponentUserNameStr = opponentUserName.decode('ascii')

    print(opponentUserNameStr)
    clientSocket.send(player2UserName.encode())

    # change server sockets to client sockets
    gameboardUI = P2GameBoardGrid()
