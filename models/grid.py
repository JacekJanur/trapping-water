from models.grid_item import GridItem

class Grid:
    """
    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        grid (list): A 2D list representing the grid items.
    """

    def __init__(self, width, height):
        """
        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
        """
        self.width = width
        self.height = height
        self.grid = [[GridItem() for _ in range(height)] for _ in range(width)]

    def set_item_color(self, x, y, color):
        """
        Args:
            x (int): The x-coordinate of the grid item.
            y (int): The y-coordinate of the grid item.
            color (str): The color to set for the grid item.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y].set_color(color)

    def get_item_color(self, x, y):
        """
        Args:
            x (int): The x-coordinate of the grid item.
            y (int): The y-coordinate of the grid item.

        Returns:
            str: The color of the grid item at position (x, y).
            None: If the position is out of bounds.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y].get_color()
        return None
