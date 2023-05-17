import pyjokes as pj
import tkinter as tk



root = tk.Tk()
root.title("My first GUI")
root.geometry("400x400")


def tell_joke():
    joke.config(text = pj.get_joke())



joke = tk.Label(text = "Your joke here")
joke.grid(row = 0,column = 1)

#b = tk.Entry()
#b.grid(row = 2, column = 1)

button = tk.Button(text = "Tell me a joke", command = tell_joke, bg = "red", fg = "blue")
button.grid(row = 3, column = 1)




#print(pyjokes.get_joke())

root.mainloop()