#Host File
"""
PLAYER2 NOW HAS A USERNAME
"""
import socket
import gameboard
import tkinter as tk

def recivingGameStatusPlayer2(gameEndMessage, opponentUserNameEndGame):
    """
    Checks if current game is over and calls appropriate functions to update board class counts.

    :param gameEndMessage: Ending mesage that is sent from player1.py after a game finishes.
    :param opponentUserNameEndGame: Player 1's username for printing name in last turn section.
    :return: Weather or not the current game has ended so undesired code does not run.
    """
    nextGame = False
    if (player2BoardData.isWinner() is True) or (player2BoardData.boardIsFull() is True):
        # = clientSocket.recv(1024)
        if gameEndMessage.decode('ascii') == 'Game Continues':
            pass
        elif gameEndMessage.decode('ascii') == 'Play Again':
            print(gameEndMessage.decode('ascii'))
            player2BoardData.resetGameBoard()
            nextGame = True
            return nextGame
        elif gameEndMessage.decode('ascii') == 'Fun Times':
            print(gameEndMessage.decode('ascii'))
            player2BoardData.printStats(opponentUserNameEndGame)
            exit()
        else:
            print('something has gone horribly wrong')

class P2IntroUIPacker:

    def __init__(self):
        self.address = ''
        self.port = None

        self.canvasSetup()
        self.initTKVariables()
        # self.returnKeyBind()

        self.createOverallLabel()

        self.createAddressEntry()

        self.createPortEntry()

        self.createSubmitButton()
        self.createQuitButton()
        self.runUI()

    def initTKVariables(self):
        self.address = tk.StringVar()
        self.port = tk.IntVar()
        self.result = tk.StringVar()

    def canvasSetup(self):
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Intro Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy).pack()

    def createOverallLabel(self):
        self.overallLabel = tk.Label(self.master, text="Tic Tac Toe Game")
        self.overallLabel.pack()

    def createAddressEntry(self):
        self.addressEntry = tk.Entry(self.master, textvariable=self.address, width=30)
        self.addressEntry.insert(0, "Enter IP Address or Host Name:")
        self.addressEntry.pack()
        """Get Rid of Zero"""

    def createPortEntry(self):
        self.portEntry = tk.Entry(self.master, textvariable=self.port)
        self.portEntry.insert(0, "Enter Port:")
        self.portEntry.pack()
        """Get Rid of Zero"""

    def updateIntroValues(self):
        self.address = self.addressEntry.get()
        self.port = self.portEntry.get()
        self.master.destroy()

    def getAddress(self):
        return self.address

    def getPort(self):
        return self.port

    def createSubmitButton(self):
        self.submitButton = tk.Button(self.master, text="Submit", command=self.updateIntroValues).pack()

    def runUI(self):
        # starts my UI - event handler
        self.master.mainloop()

class P2GameBoardGrid:

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

        self.coordinates = ()
        self.player2Coordinates = ''
        self.runUI()

    def canvasSetup(self):
        # initialize my tkinter canvas
        # self.master = tk.Tk()
        self.master = tk.Tk()
        self.master.title("P2 Game Screen")  # sets the window title
        self.master.geometry('600x500')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def player1selection(self, selector):
        if selector == '11':
            self.button11["text"] = "X"
            self.button11["state"] = "disabled"
        if selector == '12':
            self.button12["text"] = "X"
            self.button12["state"] = "disabled"
        if selector == '13':
            self.button13["text"] = "X"
            self.button13["state"] = "disabled"
        if selector == '21':
            self.button21["text"] = "X"
            self.button21["state"] = "disabled"
        if selector == '22':
            self.button22["text"] = "X"
            self.button22["state"] = "disabled"
        if selector == '23':
            self.button23["text"] = "X"
            self.button23["state"] = "disabled"
        if selector == '31':
            self.button31["text"] = "X"
            self.button31["state"] = "disabled"
        if selector == '32':
            self.button32["text"] = "X"
            self.button32["state"] = "disabled"
        if selector == '33':
            self.button33["text"] = "X"
            self.button33["state"] = "disabled"

    def initialInput

    def player

    def player2Selection11(self):
        self.coordinates = ('1', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button11["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button11["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection12(self):
        self.coordinates = ('1', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button12["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button12["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection13(self):
        self.coordinates = ('1', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button13["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button13["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection21(self):
        self.coordinates = ('2', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button21["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button21["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection22(self):
        self.coordinates = ('2', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button22["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button22["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection23(self):
        self.coordinates = ('2', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button23["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button23["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection31(self):
        self.coordinates = ('3', '1')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button31["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button31["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection32(self):
        self.coordinates = ('3', '2')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button32["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button32["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def player1Selection33(self):
        self.coordinates = ('3', '3')
        coordinatesFixed = self.coordinates[0] + self.coordinates[1]
        validity = player1BoardData.gameBoardHandling(coordinatesFixed, 'friend')
        if validity is True:
            self.button33["text"] = "X"
            connectionSocket.send(coordinatesFixed.encode())
            self.button33["state"] = "disabled"
            player1EndCheck(player1UserName)
            opponentMove = connectionSocket.recv(1024)
            opponentMoveStr = opponentMove.decode()
            player1BoardData.gameBoardHandling(opponentMoveStr, 'foe')
            self.player2selection(opponentMoveStr)
            player1EndCheck(player1UserName)

    def setPlayer2Coordinates(self, coordinates=''):
        self.player2Coordinates = coordinates

    def player2Handling(self):
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
        return self.coordinates


    def runUI(self):
        self.master.mainloop()
        # starts my UI - event handler

class P2EndBoardPackker:
    def __init__(self):
        self.getUserinfo = {}
        self.canvasSetup()
        self.createOverallLabel()
        self.createQuitButton()
        self.runUI()

    def setUserInfo(self, UserInfo):
        self.getUserInfo = UserInfo

    def canvasSetup(self):
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("P2 Final Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='blue')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy).pack()

    def createOverallLabel(self):
        finalText = "Username: " + self.getUserInfo['user name'] + '/n' + \
                    'Last player to take turn: ' + self.getUserInfo['last turn'] + '/n' + \
                    'Wins: ' + self.getUserInfo['player wins'] + '/n' + \
                    'losses:' + self.getUserInfo['player losses'] + '/n' + \
                    'ties:' + self.getUserInfo['player ties'] + '/n' + \
                    'Games Played:' + self.getUserInfo['games played'] + '/n'

        self.overallLabel = tk.Label(self.master, text=finalText)
        self.overallLabel.pack()

    def runUI(self):
        # starts my UI - event handler
        self.master.mainloop()

# Provide host information
serverAddress = input("Enter desired IP address or host name:")
serverPort = int(input("Enter desired port number:"))

# Creates host server object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds IP & port
serverSocket.bind((serverAddress, serverPort))

# Begin listening for opponent
# 1 is max number of connections at a given time
serverSocket.listen(1)
clientSocket,clientAddress = serverSocket.accept()



player2BoardData = gameboard.BoardClass('player2')
player2UserName = player2BoardData.getUserName()


#User name sending

opponentUserName = clientSocket.recv(1024)
opponentUserNameStr = opponentUserName.decode('ascii')

clientSocket.send(player2UserName.encode())

print("Client connected from: ", clientAddress)
print('Opponent: ', opponentUserNameStr)

while True:
    playerSwitch2 = False
    # Reiciving opponent's move

    player1Move = clientSocket.recv(1024)
    player1GameStatus = clientSocket.recv(1024)
    player1MoveStr = player1Move.decode('ascii')
    # player1MoveInt = int(player1MoveStr)
    player2BoardData.gameBoardHandling(player1MoveStr, 'foe')
    playerSwitch2 = recivingGameStatusPlayer2(player1GameStatus, opponentUserNameStr)

    # communicate move
    while True:
        try:
            if playerSwitch2 != True:
                player2Coordinates = gameboard.userCordinatesEntry()
                player2BoardData.gameBoardHandling(player2Coordinates, 'friend')
            break
        except ValueError:
            print('Try Move Again')
    if playerSwitch2 != True:
        clientSocket.send(str(player2Coordinates).encode())
        player1GameStatus = clientSocket.recv(1024)

        playerSwitch2 = recivingGameStatusPlayer2(player1GameStatus, opponentUserNameStr)

    





