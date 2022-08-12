import tkinter as tk

class Aplication():
    def __init__(self):
        self.contador = 0
        self.ventana1 = tk.Tk()
        self.ventana1.title('Contador')
        self.lblContador = tk.Label(self.ventana1, text=self.contador, foreground='red')
        self.lblContador.grid(row=0, column=1)
        self.btnIncrement = tk.Button(self.ventana1, text='Incrementar', command=self.increment)
        self.btnDecrement = tk.Button(self.ventana1, text='Decrementar', command=self.decrement)
        self.ventana1.mainloop()
        
    def incrementar(self):
        self.contador += 1
        
    def decrementar(self):
        pass
        
x = Aplication()