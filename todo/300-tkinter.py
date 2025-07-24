# from tkinter import *   #importamos Librerias para armar una APP para trabajar
import tkinter as tk

app = tk.Tk()

#definir tamaño de la ventana
app.geometry("600x400")
#definir color al fondo de la ventana
app.configure(background="coral")
#definir nombre a la ventana
tk.Wm.wm_title(app, "mi programa")

# tk.Button(
#     app,
#     text="clickme",
#     font=("courier", 14),
#     bg="aqua",
#     fg="white"
# ).pack(
#     fill=tk.BOTH,
#     expand=True,
# )



app.mainloop()

