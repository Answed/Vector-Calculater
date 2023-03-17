import tkinter as tk
from tkinter import ttk
from VectorClasses import*
import CalculatorLogic as Cl

main_Frame = tk.Tk()
main_Frame.title("Vector Calculator")
main_Frame.geometry("480x270")

tabcontrol = ttk.Notebook(main_Frame)

main_tab = ttk.Frame(tabcontrol)

if __name__ == "__main__":
    main_Frame.mainloop()


