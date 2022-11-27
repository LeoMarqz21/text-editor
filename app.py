from tkinter import *
from tkinter import messagebox as MessageBox
from libs.helpers import displayDate
from tkinter import filedialog as FileDialog
from pathlib import Path
from io import open

filePath = ''
filename = ''

def newFile():
    global filePath
    monitorText.set('-- New File --')
    editor.delete(1.0, END)

def openFile():
    global filePath, filename
    monitorText.set('-- open file --')
    filePath = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(('text files', '*.txt'),),
        title='Open text file'
        )
    if filePath != '':
        file = open(filePath, 'r')
        content = file.read()
        editor.delete(1.0, END)
        editor.insert(INSERT, content)
        file.close()
        del(file)
        pt = Path(filePath)
        filename = pt.name
        monitorText.set('-- open file: {} --'.format(filename))

def saveFile():
    global filePath, filename
    if filePath != '':
        #se obtiene el contenido y se elimina el ultimo salto de linea
        #agregado automaticamente
        content = editor.get(1.0, 'end-1c') 
        file = open(filePath, 'w+')
        file.write(content)
        file.close()
        del(file)
        monitorText.set('-- save file: {} --'.format(filename))
    else:
        saveFileAs()

def saveFileAs():
    global filePath, filename
    file = FileDialog.asksaveasfile(
        title='Save file as', 
        mode='w', 
        defaultextension='.txt',
        filetypes=(('text files', '*.txt'),)
        )
    if file is not None:
        filePath = file.name
        content = editor.get(1.0, 'end-1c') 
        file = open(filePath, 'w+')
        file.write(content)
        file.close()
        del(file)
        pt = Path(filePath)
        filename = pt.name
        monitorText.set('-- file saved as: {} --'.format(filename))
    else:
        monitorText.set('-- unsaved file --')
        filePath = ''
        filename = ''

def closeFile():
    global filePath, filename
    filePath = ''
    filename = ''
    editor.delete(1.0, END)

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
fileMenu.add_command(label='Close file', font=('Consolas', 12), command=closeFile)
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