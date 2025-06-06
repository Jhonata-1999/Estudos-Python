from tkinter import Tk, Label

janela = Tk()
janela.configure(bg="#e5e5e5")  # Fundo cinza médio

label = Label(janela, text="Texto de teste", fg="black", bg="#e5e5e5")  # Texto sobre fundo cinza claro
label.pack()

janela.mainloop()
