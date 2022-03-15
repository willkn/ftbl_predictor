import tkinter as tk
from predictor import predictValue

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='FTBLPRDCTR')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Search for a player:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def output():
    name = str(entry1.get())
    name = name.title()
    print(name)
    
    label3 = tk.Label(root, text= 'The recommended market value of ' + name + ' is: €' + str("{:,}".format(predictValue(name))) ,font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    
button1 = tk.Button(text='Search', command=output, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

