from tkinter import *
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.title('Meu primeiro executável Python')
root.iconbitmap(resource_path('Vlad.ico'))


mainCanvas = Canvas(root, width = 500, height = 300)
mainCanvas.pack()

def saudação ():
        etiqueta1 = Label(root, text = 'Eu vivo!', fg='red', font=('arial', 12, 'bold'))
        mainCanvas.create_window(250, 200, window=etiqueta1)

botão1 = Button(text='Clica aqui', command=saudação, bg='gray', fg='white')
mainCanvas.create_window(250, 150, window=botão1)

root.mainloop()