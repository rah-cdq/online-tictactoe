import tkinter as tk
from tkinter import ttk

#Assume User gives perfect information
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class P1IntroUIPacker:

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
        self.address = tk.StringVar()
        self.port = tk.IntVar()
        self.username = tk.StringVar()
        self.result = tk.StringVar()

    def canvasSetup(self):
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("Intro Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='white')  # set the background color of the window
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

    def createUsernameEntry(self):
        self.usernameEntry = tk.Entry(self.master, textvariable=self.username, width=45)
        self.usernameEntry.insert(0, "Enter Username (Alpha-numeric values ONLY):")
        self.usernameEntry.pack()

    def updateIntroValues(self):
        self.address = self.addressEntry.get()
        self.port = self.portEntry.get()
        self.username = self.usernameEntry.get()
        self.master.destroy()

    def getAddress(self):
        return self.address

    def getPort(self):
        return self.port

    def getUsername(self):
        return self.username

    def createSubmitButton(self):
        self.submitButton = tk.Button(self.master, text="Submit", command=self.updateIntroValues).pack()

    def createResultLabel(self):
        self.result.set('')
        self.resultLabel = tk.Label(self.master, textvariable=self.result, width=25).pack()

    def runUI(self):
        # starts my UI - event handler
        self.master.mainloop()

class P1ConnectionErrorUIPacker:
    def __init__(self):
        self.userAnswer = 'n'

        self.canvasSetup()
        self.createOverallLabel()
        self.createYesButton()
        self.createNoButton()
        self.createQuitButton()
        self.runUI()

    def canvasSetup(self):
        # initialize my tkinter canvas
        self.master = tk.Tk()
        self.master.title("Error Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='white')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def createOverallLabel(self):
        self.overallLabel = tk.Label(self.master, text="Connection failed, try Again?")
        self.overallLabel.pack()

    def createYesButton(self):
        self.yesButton = tk.Button(self.master, text="Yes", command=self.setYes).pack()

    def createNoButton(self):
        self.noButton = tk.Button(self.master, text="No", command=self.setNo).pack()

    def setYes(self):
        self.userAnswer = 'y'
        self.master.destroy()

    def setNo(self):
        self.userAnswer = 'n'
        self.master.destroy()


    def getUserAnswer(self):
        return self.userAnswer

    def createQuitButton(self):
        self.quitButton = tk.Button(self.master, text="Quit", command=self.master.destroy).pack()

    def runUI(self):
        # starts my UI - event handler
        self.master.mainloop()

class P1GameBoardGrid:

    def __init__(self):
        self.canvasSetup()

        self.create11()
        self.create12()
        self.create13()

        self.create21()
        self.create22()
        self.create23()

        self.create31()
        self.create32()
        self.create33()

        self.runUI()

    def canvasSetup(self):
        # initialize my tkinter canvas
        # self.master = tk.Tk()
        self.master = tk.Tk()
        self.master.title("P1 Game Screen")  # sets the window title
        self.master.geometry('600x500')  # sets the default size of the window
        self.master.configure(background='red')  # set the background color of the window
        self.master.resizable(0, 0)  # setting the x(horizontal) and y (vertical) to not be resizable.

    def create11(self, entry=''):
        self.button11 = tk.Button(self.master, width=15, height=7, text=entry).grid(padx=60, pady=25)

    def create12(self, entry=''):
        self.button12 = tk.Button(self.master, width=15, height=7, text=entry).grid(padx=60, pady=25)

    def create13(self, entry=''):
        self.button13 = tk.Button(self.master, width=15, height=7, text=entry).grid(padx=60, pady=25)

    def create21(self, entry=''):
        self.button21 = tk.Button(self.master, width=15, height=7, text=entry).grid(row=0, column=1)

    def create22(self, entry=''):
        self.button22 = tk.Button(self.master, width=15, height=7, text=entry).grid(row=1, column=1)

    def create23(self, entry=''):
        self.button23 = tk.Button(self.master, width=15, height=7, text=entry).grid(row=2, column=1)

    def create31(self, entry=''):
        self.button31 = tk.Button(self.master, width=15, height=7, text=entry).grid(row=0, column=2, padx=60)

    def create32(self, entry=''):
        self.button32 = tk.Button(self.master, width=15, height=7, text=entry).grid(row=1, column=2, padx=60)

    def create33(self, entry=''):
        self.button33 = tk.Button(self.master, width=15, height=7, text='O', command=).grid(row=2, column=2, padx=60)

    def player1Selection(self):
        self.button33["text"] = "x"


    def runUI(self):
        self.master.mainloop()
        # starts my UI - event handler

class P1GameBoardPackker:
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
        self.master.title("Final Screen")  # sets the window title
        self.master.geometry('600x400')  # sets the default size of the window
        self.master.configure(background='white')  # set the background color of the window
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


if __name__ == '__main__':
    basicUI = P1GameBoardGrid()

