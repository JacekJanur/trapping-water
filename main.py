import tkinter as tk
from tkinter import messagebox

from models import *
from ui import *
from clicked_values_manager import ClickedValuesManager

class Controller:
    """
    Attributes:
        app_ui (AppUI): The user interface component associated with this controller.
        clicked_values_manager (ClickedValuesManager): The manager for handling clicked values.
    """

    def __init__(self, app_ui: AppUI):
        """
        Args:
            app_ui (AppUI): The user interface component associated with this controller.
        """
        self.app_ui: AppUI = app_ui
        self.clicked_values_manager: ClickedValuesManager = ClickedValuesManager()

        # Add the grid UI as an observer if the app UI is available
        if self.app_ui:
            self.clicked_values_manager.add_observer(self.app_ui.grid_ui)

    def redraw(self, event=None):
        """
        Args:
            event: Optional event argument. Defaults to None.
        """
        if self.app_ui:
            self.clicked_values_manager.clicked_values.clear()

            width: int = self.app_ui.x_entry.get_value()
            height: int = self.app_ui.y_entry.get_value()

            # Check if the values are greater than 1
            if width <= 1 or height <= 1:
                messagebox.showerror("Error", "Width and height must be greater than 1")
                return

            self.app_ui.grid_ui.draw_grid(width, height)



if __name__ == "__main__":
    root: tk.Tk = tk.Tk()

    controller: Controller = Controller(None)

    app_ui: AppUI = AppUI(root, controller)
    controller.app_ui = app_ui
    if controller.app_ui.grid_ui:
        controller.app_ui.grid_ui.controller = controller
        controller.clicked_values_manager.add_observer(controller.app_ui.grid_ui)
        
    root.mainloop()
