import tkinter as tk
from tkinter import ttk
from VectorClasses import*
import CalculatorLogic as Cl
import DataManager as DM

main_Frame = tk.Tk()
main_Frame.title("Vector Calculator")
main_Frame.geometry("480x270")

tabcontrol = ttk.Notebook(main_Frame)

main_tab = ttk.Frame(tabcontrol)

class Visualize2D(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master=master)
        tabcontrol.add(self, text="2D Display")

        head_of_tab_L = tk.Label(self, text="This Tab is for visualaising 2D vectors")
        available_vectors_L = tk.Label(self, text="All available Vectors")
        self.available_vectors = tk.Listbox(self) # Has to be self. so i can use it later to actually add and remove the vectors from the list
        selected_vectors_L = tk.Label(self, text="All selected Vectors")
        self.selected_vectors = tk.Listbox(self)  # Has to be self. so i can use it later to actually add and remove the vectors from the list
        add_vector_B = tk.Button(self, text="Add Vector", command=lambda: self.add_vector())
        display_vector_B = tk.Button(self, text="Show selected \n vectors") 

        head_of_tab_L.grid(column=1, row=0)
        available_vectors_L.grid(column=0, row=1)
        self.available_vectors.grid(column=0, row=2)
        add_vector_B.grid(column=0, row=3)
        selected_vectors_L.grid(column= 2, row=1)
        self.selected_vectors.grid(column=2, row=2)
        display_vector_B.grid(column=2, row=3)

        self.load2DVectors()

    def load2DVectors(self):
        if (self.available_vectors.size() < len(DM.saved_vector2_dic)):
            for vector in DM.saved_vector2_dic:
                if not vector in self.available_vectors.get(0, tk.END):
                    self.available_vectors.insert(tk.END ,vector)
                    self.after(1000, self.load2DVectors)
        else:   self.after(1000, self.load2DVectors)
    
    def add_vector(self):
        self.selected_vectors.insert(tk.END, self.available_vectors.get(tk.ANCHOR))

class Visualize3D(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master=master)
        tabcontrol.add(self, text="3D Display")

        head_of_tab_L = tk.Label(self, text="This Tab is for visualaising 3D vectors")
        available_vectors_L = tk.Label(self, text="All available Vectors")
        self.available_vectors = tk.Listbox(self) # Has to be self. so i can use it later to actually add and remove the vectors from the list
        selected_vectors_L = tk.Label(self, text="All selected Vectors")
        self.selected_vectors = tk.Listbox(self)  # Has to be self. so i can use it later to actually add and remove the vectors from the list
        add_vector_B = tk.Button(self, text="Add Vector")
        display_vector_B = tk.Button(self, text="Show selected \n vectors") 

        head_of_tab_L.grid(column=1, row=0)
        available_vectors_L.grid(column=0, row=1)
        self.available_vectors.grid(column=0, row=2)
        add_vector_B.grid(column=0, row=3)
        selected_vectors_L.grid(column= 2, row=1)
        self.selected_vectors.grid(column=2, row=2)
        display_vector_B.grid(column=2, row=3)

        self.load3DVectors()

    def load3DVectors(self):
        if (self.available_vectors.size() < len(DM.saved_vector2_dic)):
            for vector in DM.saved_vector2_dic:
                if not vector in self.available_vectors.get(0, tk.END):
                    self.available_vectors.insert(tk.END ,vector)
                    self.after(1000, self.load3DVectors)
        else:   self.after(1000, self.load3DVectors)
    
    def add_vector(self):
        self.selected_vectors.insert(tk.END, self.available_vectors.get(tk.ANCHOR))

def MainTab():
    tabcontrol.add(main_tab, text="Calculator") 
    visualize2D = Visualize2D(tabcontrol)
    visualize3D = Visualize3D(tabcontrol)

    # UI needed for adding a Vector 2 to the list
    new_vector2_name_L = tk.Label(main_tab, text="Name of vector 2")
    new_vector2_name_E = tk.Entry(main_tab, width=25)
    new_vector2_value_L = tk.Label(main_tab, text="Enter the values from the vector 2")
    new_vector2_value_E = tk.Entry(main_tab, width=25)
    new_vector2_value_E.insert(0, "(x|y)")
    add_vector2_B = tk.Button(main_tab, text="Add Vector", command=lambda: DM.save_Vector2(new_vector2_name_E.get(), new_vector2_value_E.get()))

    # UI needed for adding a Vector 3 to the list
    new_vector3_name_L = tk.Label(main_tab, text="Name of vector 3")
    new_vector3_name_E = tk.Entry(main_tab, width=25)
    new_vector3_value_L = tk.Label(main_tab, text="Enter the values from the vector 3")
    new_vector3_value_E = tk.Entry(main_tab, width=25, )
    new_vector3_value_E.insert(0, "(x|y|z)")
    add_vector3_B = tk.Button(main_tab, text="Add Vector", command=lambda: DM.save_Vector3(new_vector3_name_E.get(), new_vector3_value_E.get()))

    new_vector2_name_L.grid(column=0, row=0)
    new_vector2_name_E.grid(column=1, row=0)
    new_vector2_value_L.grid(column=0, row=1)
    new_vector2_value_E.grid(column=1, row=1)
    add_vector2_B.grid(column=1, row=2)
    new_vector3_name_L.grid(column=0, row=3)
    new_vector3_name_E.grid(column=1, row=3)
    new_vector3_value_L.grid(column=0, row=4)
    new_vector3_value_E.grid(column=1, row=4)
    add_vector3_B.grid(column=1, row=5)

if __name__ == "__main__":
    MainTab()
    tabcontrol.pack(expand=1, fill="both")
    main_Frame.mainloop()

