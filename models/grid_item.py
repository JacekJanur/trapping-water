class GridItem:
    """
    Attributes:
        color (str): The color of the grid item.

    """

    def __init__(self, color="white"):
        """
        Args:
            color (str): The color of the grid item. Default is "white".
        """
        self.color = color

    def set_color(self, color):
        """
        Args:
            color (str): The new color of the grid item.
        """
        self.color = color

    def get_color(self):
        """
        Returns:
            str: The color of the grid item.
        """
        return self.color
