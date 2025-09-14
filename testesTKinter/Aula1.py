from tkinter import *

window = Tk()

class aplication():
    def __init__(self):
        self.window = window
        self.tela()
        self.frames()
        window.mainloop()        
    def tela (self):
        self.window.title("Cadastro de Otários")
        self.window.configure(background='#2F999C')
        self.window.geometry("700x500")
        self.window.resizable(True, True)
    def frames (self):
        self.frame_1 = Frame(self.window, bd = 4, bg = '#4CD8E4', highlightbackground='#DC4CE4', highlightthickness=5)
        self.frame_2 = Frame(self.window, bd = 4, bg = '#4CD8E4', highlightbackground='#DC4CE4', highlightthickness=5)

        '''place => X / Y (estático)
        pack => mais simples
        grid => linhas / colunas'''

        self.frame_1.place(relx = 0.025, rely = 0.02, relwidth = 0.45, relheight = 0.95)
        self.frame_2.place(relx = 0.525, rely = 0.02, relwidth = 0.45, relheight = 0.95)

aplication()