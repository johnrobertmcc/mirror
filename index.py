import tkinter as tk

window = tk.Tk()

window.attributes('-fullscreen', True)

label = tk.Label(window, text="This is a test", font=('Monospace 18 bold'))

label.pack(pady=20)

window.mainloop()
