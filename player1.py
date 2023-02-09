import tkinter as tk
import socket
import gameboard

# Assume User gives perfect information


class P1IntroUIPacker:
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
        self.master.title("P1 Intro Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='red')  # set the background color of the window
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


class P1ConnectionErrorUIPacker:
    """
    Error screen class object TK inter Gui to indicate a failed connection.
    """
    def __init__(self):
        self.userAnswer = 'n'

        self.canvasSetup()
        self.createOverallLabel()
        self.createYesButton()
        self.createNoButton()
        self.createQuitButton()
        self.runUI()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P1 Error Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='red')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createOverallLabel(self):
        """
        Creates a label to indicate what has happened.
        """
        self.overallLabel = tk.Label(self.master, text="Connection failed, try Again?")
        self.overallLabel.pack()

    def createYesButton(self):
        """
        Creates a Yes button.
        """
        self.yesButton = tk.Button(self.master, text="Yes", command=self.setYes).pack()

    def createNoButton(self):
        """
        Creates a No button.
        """
        self.noButton = tk.Button(self.master, text="No", command=self.setNo).pack()

    def setYes(self):
        """
        Handles what happens when Yes is pressed.
        """
        self.userAnswer = 'y'
        self.master.destroy()

    def setNo(self):
        """
        Handles what happens when No is pressed.
        """
        self.userAnswer = 'n'
        self.master.destroy()

    def getUserAnswer(self):
        """
        Gets which button the user pressed through a string value.

        :returns y or n string.
        """
        return self.userAnswer

    def createQuitButton(self):
        """
        Creates a quit button, mostly for debugging purposes.
        """
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy).pack()

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


class P1GameBoardGrid:
    """
    Game board class object TK inter Gui for the player to play Tic Tac Toe on.
    """
    def __init__(self):
        self.canvasSetup()

        self.button11 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection11)
        self.button11.grid(padx=60, pady=25)
        self.button12 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection12)
        self.button12.grid(padx=60, pady=25)
        self.button13 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection13)
        self.button13.grid(padx=60, pady=25)
        self.button21 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection21)
        self.button21.grid(row=0, column=1)
        self.button22 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection22)
        self.button22.grid(row=1, column=1)
        self.button23 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection23)
        self.button23.grid(row=2, column=1)
        self.button31 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection31)
        self.button31.grid(row=0, column=2, padx=60)
        self.button32 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection32)
        self.button32.grid(row=1, column=2, padx=60)
        self.button33 = tk.Button(self.master, width=15, height=7, text='', command=self.player1Selection33)
        self.button33.grid(row=2, column=2, padx=60)

        self.turnLabel = tk.Label(self.master, width=17, height=3, text="Current Player's turn:")
        self.turnLabel.grid(row=3, column=0)
        self.turnButton = tk.Label(self.master, width=17, height=3, text=player1UserName)
        self.turnButton.grid(row=3, column=1)

        self.coordinates = ()
        self.player2Coordinates = ''
        self.runUI()

    def player1EndCheck(self, player1UserNameEndCheck):
        """
        Checks if current game is over and calls appropriate functions to update board class counts.

        :param player1UserNameEndCheck: Player 1's username, mostly for debugging purposes.
        :return: Weather or not the current game has ended so undesired code does not run.
        """
        replay = False
        if (player1BoardData.isWinner() is True) or (player1BoardData.boardIsFull() is True):
            player1BoardData.printStats(player1UserName, opponentUserName)
            self.disableAllButtons()
            endUI = P1EndBoardPacker()
            print('past')
            playAgain = endUI.getAnswer()
            print('pack got')

            # = endUI.getAnswer()
            print(playAgain)

            # playAgain = input('Do you want to play again?')
            if playAgain == 'y' or playAgain == 'Y':
                pa = 'Play Again'
                connectionSocket.send(pa.encode())
                player1BoardData.resetGameBoard()
                self.resetBoard()
                replay = True
                return replay
                # break
            elif playAgain == 'n' or playAgain == 'N':
                ft = 'Fun Times'
                connectionSocket.send(ft.encode())
                connectionSocket.close()
                self.destroyP1GameBoardGrid()
                exit()
            else:
                print('Invalid Input')
        return replay

    def resetBoard(self):
        """
        Resets board to its original state.
        """
        self.turnButton["text"] = player1UserName

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
        self.turnDisplay('Not Player two')

        self.master.update()

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
        if turn == 'player2':
            self.turnButton["text"] = opponentUserNameStr
        else:
            self.turnButton["text"] = player1UserName

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        # self.master = tk.Tk()
        self.master = tk.Tk()
        self.master.title("P1 Game Screen")  # sets the window title
        self.master.geometry('600x600')  # sets the default size of the window
        self.master.configure(background='red')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def player2selection(self, selector):
        """
        Handles putting opponent's move on the board.

        :param selector: coordinates of opponent's move
        """
        if selector == '11':
            self.button11["text"] = "O"
            self.button11["state"] = "disabled"
        if selector == '21':
            self.button12["text"] = "O"
            self.button12["state"] = "disabled"
        if selector == '31':
            self.button13["text"] = "O"
            self.button13["state"] = "disabled"
        if selector == '12':
            self.button21["text"] = "O"
            self.button21["state"] = "disabled"
        if selector == '22':
            self.button22["text"] = "O"
            self.button22["state"] = "disabled"
        if selector == '32':
            self.button23["text"] = "O"
            self.button23["state"] = "disabled"
        if selector == '13':
            self.button31["text"] = "O"
            self.button31["state"] = "disabled"
        if selector == '23':
            self.button32["text"] = "O"
            self.button32["state"] = "disabled"
        if selector == '33':
            self.button33["text"] = "O"
            self.button33["state"] = "disabled"

    def player1Selection11(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button11["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button11["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection12(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '2')
        coordinatesFixed = self.coordinates[1] + self.coordinates[0]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button12["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button12["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection13(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button13["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button13["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection21(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button21["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button21["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection22(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('2', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button22["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button22["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection23(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button23["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button23["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection31(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('1', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button31["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button31["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection32(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('2', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button32["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button32["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def player1Selection33(self):
        """
        Handles what happens when button corresponding to x,y coordinate numbers in title is pressed.
        """
        self.coordinates = ('3', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:

            self.button33["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button33["state"] = "disabled"
            a = self.player1EndCheck(player1UserName)
            if a is False:
                self.turnDisplay('player2')
                self.master.update()
                opponentMove = connectionSocket.recv(1024)
                opponentMoveStr = opponentMove.decode('ascii')
                player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
                self.player2selection(opponentMoveStr)
                self.player1EndCheck(player1UserName)
                self.turnDisplay(player1UserName)
                self.master.update()

    def setPlayer2Coordinates(self, coordinates=''):
        """
        Sets opponent's coordinates

        :param coordinates in string format form opponent's current move.
        """
        self.player2Coordinates = coordinates

    def player2Handling(self):
        """
        Handles putting opponent's move on the board.
        """
        if self.player2Coordinates == '11':
            self.button11["text"] = "O"
        elif self.player2Coordinates == '12':
            self.button12["text"] = "O"
        elif self.player2Coordinates == '13':
            self.button13["text"] = "O"
        elif self.player2Coordinates == '21':
            self.button21["text"] = "O"
        elif self.player2Coordinates == '22':
            self.button22["text"] = "O"
        elif self.player2Coordinates == '23':
            self.button23["text"] = "O"
        elif self.player2Coordinates == '31':
            self.button31["text"] = "O"
        elif self.player2Coordinates == '32':
            self.button32["text"] = "O"
        elif self.player2Coordinates == '33':
            self.button33["text"] = "O"

    def getCoordinates(self):
        """
        Gets coordinates of player 1.
        """
        return self.coordinates

    def destroyP1GameBoardGrid(self):
        """
        Destroys game board TK object, mostly for debugging purposes.
        """
        self.master.destroy()

    def runUI(self):
        """
        Starts UI loop.
        """
        self.master.mainloop()
        # starts my UI - event handler


class P1EndBoardPacker:
    """
    End screen class object TK inter GUI for the player's end screen during tic tac toe.
    """
    def __init__(self):
        self.answer = ''

        self.userInfo = {}
        self.canvasSetup()
        self.createOverallLabel()
        self.createQuestionLabel()

        self.yesButton = tk.Button(self.master, text="Yes", command=self.yesHandling)
        self.yesButton.pack()

        self.noButton = tk.Button(self.master, text="No", command=self.noHandling)
        self.noButton.pack()

        self.runUI()

    def canvasSetup(self):
        """
        Sets the attributes for the TK canvas.
        """
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P1 Final Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='red')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createOverallLabel(self):
        """
        Creates label to display final results.
        """
        self.userInfo = player1BoardData.getPlayerFinalData()
        if self.userInfo['last turn'] == 'player2':
            lastTurnFixed = opponentUserNameStr
        else:
            lastTurnFixed = player1UserName

        finalText = "Username: " + self.userInfo['user name'] + '\n' + \
                    'Last player to take turn: ' + lastTurnFixed + '\n' + \
                    'Wins: ' + str(self.userInfo['player wins']) + '\n' + \
                    'losses:' + str(self.userInfo['player losses']) + '\n' + \
                    'ties:' + str(self.userInfo['player ties']) + '\n' + \
                    'Games Played:' + str(self.userInfo['games played']) + '\n'
        self.overallLabel = tk.Label(self.master, text=finalText)
        self.overallLabel.pack()

    def createQuestionLabel(self):
        """
        Creates label to ask if player wants to play again.
        """
        self.overallLabel = tk.Label(self.master, text='Play again?')
        self.overallLabel.pack()
    """
    def createQuitButtton(self):
        self.quitButton = tk.Button(self.master, text="Quit this screen", command=self.master.destroy)
        self.quitButton.pack()
        self.master.update()
    """

    def yesHandling(self):
        """
        Handles what happens if player selects yes to playing again.
        """
        self.answer = 'y'
        self.master.quit()
        self.master.destroy()
        """
        self.yesButton["state"] = 'disabled'
        self.noButton["state"] = 'disabled'
        self.createQuitButtton()
        """

    def noHandling(self):
        """
        Handles what happens if player selects no to playing again.
        """
        self.answer = 'n'
        self.master.quit()
        self.master.destroy()
        """
        self.noButton["state"] = 'disabled'
        self.yesButton["state"] = 'disabled'
        self.createQuitButtton()
        """

    def getAnswer(self):
        """
        :returns string value of weather player wants to play again.
        """
        return self.answer

    def runUI(self):
        """
        Starts UI loop.
        """
        # starts my UI - event handler
        self.master.mainloop()


if __name__ == '__main__':

    while True:
        allDataSolid = False
        userNameCheckSentinelValue = False
        while True:
            introUserInterface = P1IntroUIPacker()
            provisionalUserName = introUserInterface.getUsername()
            for alphaNum in provisionalUserName:
                if (alphaNum.isnumeric() is True) or (alphaNum.isspace() is True) or (alphaNum.isalpha() is True):
                    userNameCheckSentinelValue = True

                else:
                    userNameCheckSentinelValue = False

            if userNameCheckSentinelValue is True:
                break
            else:
                print('User Name has non alpha-numeric characters, try again.')

        while True:
            # startAtUsername = False
            # prompting user for host IP & socket
            serverAddress = introUserInterface.getAddress()
            try:
                serverPort = int(introUserInterface.getPort())
                print(serverAddress)
                print(serverPort)
                # Creates socket object
                connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Attempts to connect to player 2
                connectionSocket.connect((serverAddress, serverPort))
                allDataSolid = True
                break
            except Exception:
                networkUserInterface = P1ConnectionErrorUIPacker()
                doYouWantToRetryConnection = networkUserInterface.getUserAnswer()
                if doYouWantToRetryConnection == 'y':
                    startAtUsername = False
                    break
                elif doYouWantToRetryConnection == 'n':
                    exit()
                else:
                    print('Invalid Input, try again')
        if allDataSolid is True:
            break

print(provisionalUserName)
connectionSocket.send(provisionalUserName.encode())

opponentUserName = connectionSocket.recv(1024)
opponentUserNameStr = opponentUserName.decode('ascii')

print(opponentUserNameStr)

player1UserName = provisionalUserName
player1BoardData = gameboard.BoardClass(player1UserName)
gameboardUI = P1GameBoardGrid()
