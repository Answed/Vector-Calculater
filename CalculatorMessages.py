import tkinter as tk

# Is used everythime something went wrong with an input.
def WrongInput(message: str):
    newWindow = tk.Toplevel()
    newWindow.title("Error")
    newWindow.geometry("300x100")

    errorMessage_L = tk.Label(newWindow, text=message)
    closeWindow_B = tk.Button(newWindow, text="OK!", command=lambda: newWindow.destroy())

    errorMessage_L.pack()
    closeWindow_B.pack()

# Will be used for displaying the results of a calculation.
def Result(message: str):
    newWindow = tk.Toplevel()
    newWindow.title("Result")
    newWindow.geometry("300x100")

    errorMessage_L = tk.Label(newWindow, text=message)
    closeWindow_B = tk.Button(newWindow, text="THX!", command=lambda: newWindow.destroy())

    errorMessage_L.pack()
    closeWindow_B.pack()