import tkinter as tk
from tkinter import ttk
from VectorClasses import*
import CalculatorLogic as Cl

main_Frame = tk.Tk()
main_Frame.title("Vector Calculator")
main_Frame.geometry("480x270")

tabcontrol = ttk.Notebook(main_Frame)

main_tab = ttk.Frame(tabcontrol)

def MainTab():
    tabcontrol.add(main_tab, text="Calculator") 

    new_vector2_L = tk.Label(main_tab, text="Create a new Vector 2")
    new_vector2_E = tk.Entry(main_tab, width=50)
    add_vector2_B = tk.Button(main_tab, text="Add Vector")

    new_vector2_L.grid(column=0, row=0)
    new_vector2_E.grid(column=1, row=0)
    add_vector2_B.grid(column=1, row=1)


if __name__ == "__main__":
    MainTab()
    tabcontrol.pack(expand=1, fill="both")
    main_Frame.mainloop()


