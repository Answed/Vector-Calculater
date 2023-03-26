import tkinter as tk

def WrongInput(message: str):
    newWindow = tk.Toplevel()
    newWindow.title("Error")
    newWindow.geometry("300x100")

    errorMessage_L = tk.Label(newWindow, text=message)
    closeWindow_B = tk.Button(newWindow, text="OK!", command=lambda: newWindow.destroy())

    errorMessage_L.pack()
    closeWindow_B.pack()