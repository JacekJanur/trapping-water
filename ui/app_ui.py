import tkinter as tk
from ui.grid_ui import GridUI
from models import NumericEntry 

class AppUI:
    """
    Args:
        master: The master widget managing this interface.
        controller: The controller object managing the application logic.

    Attributes:
        master: The master widget managing this interface.
        controller: The controller object managing the application logic.
        grid_ui: The grid user interface widget for displaying the simulation grid.
        x_entry: The entry widget for specifying the width of the grid.
        y_entry: The entry widget for specifying the height of the grid.
    """

    def __init__(self, master, controller):
        """
        Args:
            master: The master widget managing this interface.
            controller: The controller object managing the application logic.
        """
        self.master = master
        self.controller = controller
        self.master.title("Trapping Rain Water Simulation")
        self.master.geometry("900x600")
        self.master.resizable(False, False) 

        self.grid_ui = GridUI(self.master, controller)

        self.create_widgets()
        self.master.bind("<Configure>", self.resize_event) 

    def create_widgets(self):
        self.x_entry = NumericEntry(self.master, default=10, label="Width:")
        self.x_entry.grid(row=0, column=1, padx=10, pady=10)

        self.y_entry = NumericEntry(self.master, default=10, label="Height:")
        self.y_entry.grid(row=0, column=3, padx=10, pady=10)

        calculate_button = tk.Button(self.master, text="Calculate", command=self.controller.redraw)
        calculate_button.grid(row=0, column=4, padx=20, pady=10)

        self.grid_ui.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew") 

        self.master.grid_columnconfigure(0, weight=1)  
        self.master.grid_rowconfigure(1, weight=1)  

    def resize_event(self, event):
        self.controller.redraw()
