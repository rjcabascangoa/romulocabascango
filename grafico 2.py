import tkinter as tk
#palabra= tk.StringVar(app)
#entrada = tk.StrigVar(app)

app = tk.Tk ()
app.geometry("300x600")
app.configure(background="black")
tk.Wm.wm_title(app,"Hola Javier")
def saludar():
    print("Hola Javier")
tk.Button(
    app,
    text="Clik",
    font=("Courier",14),
    bg="#00a8e8",
    fg="white",
    command=lambda:print("Holaaaaa"),
    relief="flat"
).pack(
    fill=tk.BOTH,
    expand=True,
)
tk.Label(
    app,
    text="HOLA SOY ETIQUETA",
    fg="white",
    bg="black",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True,
)
tk.Entry(
    fg="white",
    bg="black",
    justify="center"

).pack(
    fill=tk.BOTH,
    expand=True,
)
app.mainloop()