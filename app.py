from tkinter import *
from tkinter import messagebox as MessageBox
from libs.helpers import displayDate
from tkinter import filedialog as FileDialog

filePath = ''

def newFile():
    global filePath
    monitorText.set('-- New File --')
    editor.delete(1.0, END)

def openFile():
    global filePath
    monitorText.set('-- open file --')
    filePath = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(('text files', '*.txt'),),
        title='Open text file'
        )
    print(filePath)

def saveFile():
    global filePath
    monitorText.set('-- save file --')

def saveFileAs():
    global filePath
    monitorText.set('-- save file as --')

app = Tk()
app.iconbitmap('./images/logo.ico')
app.geometry('750x600')
app.title('Text Editor')
navbar = Menu(app, tearoff=0, bd=5, font='Consolas 12 bold')
app.config(menu=navbar)

#menu----------------
fileMenu = Menu(navbar, tearoff=0)
fileMenu.add_command(label='New File', font=('Consolas', 12), command=newFile)
fileMenu.add_command(label='Open File', font=('Consolas', 12), command=openFile)
fileMenu.add_command(label='Save File', font=('Consolas', 12), command=saveFile)
fileMenu.add_command(label='Save File As', font=('Consolas', 12), command=saveFileAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=app.quit, font=('Consolas', 12))

supportMenu = Menu(navbar, tearoff=0)
supportMenu.add_command(label='Help', font=('Consolas', 12))
supportMenu.add_command(label='Customized Assistance', font=('Consolas', 12))

navbar.add_cascade(menu=fileMenu, label='File')
navbar.add_cascade(menu=supportMenu, label='Support')

#editor---------------------------
editor = Text(app)
editor.pack(fill='both', expand=1)
editor.config(bd=0, font=('Consolas', 12))

monitorText = StringVar()
monitorText.set('Welcome to my text editor')
monitor = Label(app, text='', textvariable=monitorText)
monitor.pack(side='left', padx=3)

date = StringVar()
date.set(displayDate())
currentDate = Label(app, text='', textvariable=date)
currentDate.pack(side='right', padx=3)


app.mainloop()