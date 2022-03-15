from tkinter import *
import tkinter
from gui_search import output
import settings
from predictor import predictValue

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="red")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 
        Frame2 = Frame(master, bg="blue")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Frame3 = Frame(master, bg="green")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

        # Frame 1 build
        searchText = Label(Frame1, text='Search for a player')
        searchBox = Entry(Frame1)
        searchButton = Button(Frame1, text='Search', command=predictValue(searchBox.get()))
        player = Label(Frame1, text='')

        # Frame 1 pack
        searchText.pack(pady=20)
        searchBox.pack()
        searchButton.pack()
        player.pack()
        
        # Frame 2 build
        filters = Label(Frame2, text='Filters')

        overall = Scale(Frame2, from_=0, to=99, orient=HORIZONTAL)
        potential = Scale(Frame2, from_=0, to=99, orient=HORIZONTAL)
        value = Entry(Frame2, text='height')
        height = Entry(Frame2, text='height')
        
        # Frame 2 pack
        filters.pack(pady=50)
        overall.pack(padx=20, pady=10)
        potential.pack(padx=20, pady=10)
        value.pack(padx=20, pady=10)
        height.pack(padx=20, pady=10)

        # Frame 3 build
        # Get a player photo in

        # playerText = Label(Frame3, text=settings.currentPlayerOutline.get('short_name'))
        playerText = Label(Frame3, text='Kalvin Phillips')
        playerOverall = Label(Frame3, text='Overall: 81')
        playerPace = Label(Frame3, text='Pace: 70')
        playerDribbling = Label(Frame3, text='Dribbling: 85')
        playerShooting = Label(Frame3, text='Shooting: 89')
        playerPhysic = Label(Frame3, text='Physicality: 85')
        playerDefending = Label(Frame3, text='Defending: 87')

        # Frame 3 pack
        playerText.pack(pady=10)
        playerOverall.pack(pady=10)
        playerDefending.pack(pady=10)
        playerPace.pack(pady=10)
        playerDribbling.pack(pady=10)
        playerShooting.pack(pady=10)
        playerPhysic.pack(pady=10)
    

root = Tk()
root.geometry("2000x1600+200+200")
app = Application(master=root)
app.mainloop()

