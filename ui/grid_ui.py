import tkinter as tk
from observer import Observer
from models import TrappedWater

class GridUI(tk.Canvas, Observer):
    """
    Args:
        master: The master widget managing this interface.
        controller: The controller object managing the application logic.
        **kwargs: Additional keyword arguments for configuring the canvas.

    Attributes:
        controller: The controller object managing the application logic.
        trapped_water: An instance of the TrappedWater class for calculating water trapping simulation.
    """

    def __init__(self, master, controller, **kwargs):
        """
        Args:
            master: The master widget managing this interface.
            controller: The controller object managing the application logic.
            **kwargs: Additional keyword arguments for configuring the canvas.
        """
        super().__init__(master, background="white", **kwargs)
        self.controller = controller
        self.trapped_water = TrappedWater()
        self.bind("<Button-1>", self.handle_click)
        self.draw_grid(10, 10)

    def update(self, clicked_values_manager):
        """
        Args:
            clicked_values_manager: The manager object containing clicked values data.
        """
        self.delete("all")
        width, height = self.controller.width, self.controller.height
        self.draw_grid(width, height)
       
        clicked_values = clicked_values_manager.get_clicked_values()
        water = self.trapped_water.trap(clicked_values)
        
        heights = [0] * (len(water))
        for x, y in clicked_values:
            heights[x] = y + 1 
            
        for x, y in clicked_values:
            for h in range(height-y -1, height):
                self.update_item_color(x, h, "black")
        for x,y in enumerate(water):
            for h in range(y):
                self.update_item_color(x, height - h -1 - heights[x], "blue")
                
    def draw_grid(self, width, height):
        """
        Args:
            width: The width of the grid.
            height: The height of the grid.
        """
        self.delete("all")
        self.controller.width = width 
        self.controller.height = height 
        cell_width = self.winfo_width() / width
        cell_height = self.winfo_height() / height

        for i in range(width + 1):
            self.create_line(i * cell_width, 0, i * cell_width, self.winfo_height(), fill='black')
        for i in range(height + 1):
            self.create_line(0, i * cell_height, self.winfo_width(), i * cell_height, fill='black')

    def update_item_color(self, x, y, color):
        """
        Args:
            x: The x-coordinate of the grid cell.
            y: The y-coordinate of the grid cell.
            color: The color to fill the grid cell.
        """
        cell_width = self.winfo_width() / self.controller.width
        cell_height = self.winfo_height() / self.controller.height
        outline_color = 'black' if color == 'white' else ''
        self.create_rectangle(x * cell_width, y * cell_height,
                               (x + 1) * cell_width, (y + 1) * cell_height,
                               fill=color, outline=outline_color)

    def handle_click(self, event):
        """
        Args:
            event: The mouse event object.
        """
        x = int(event.x / (self.winfo_width() / self.controller.width))
        y = self.controller.height - 1 -int(event.y / (self.winfo_height() / self.controller.height))
        current_color = self.controller.clicked_values_manager.get_clicked_values()
        if (x, y) in current_color:
            self.controller.clicked_values_manager.delete_clicked_value(x,  y)
        else:
            self.controller.clicked_values_manager.add_clicked_value(x,  y)
