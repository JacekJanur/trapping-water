class ClickedValuesManager:
    """
    Attributes:
        observers (list): List of observers to be notified of changes.
        clicked_values (list): List of clicked values in the format (x, y).
    """

    def __init__(self):
        self.observers: list = []
        self.clicked_values: list = []

    def add_observer(self, observer):
        """
        Args:
            observer: The observer object to be added.
        """
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def add_clicked_value(self, x: int, y: int):
        """
        Args:
            x (int): The x-coordinate of the clicked value.
            y (int): The y-coordinate of the clicked value.
        """
        if x in [val[0] for val in self.clicked_values]:
            self.update_clicked_value(x, y)
            return
        self.clicked_values.append((x, y))
        self.notify_observers()

    def update_clicked_value(self, x: int, y: int):
        """
        Args:
            x (int): The x-coordinate of the clicked value to be updated.
            y (int): The new y-coordinate for the clicked value.
        """
        for i, (xi, _) in enumerate(self.clicked_values):
            if xi == x:
                self.clicked_values[i] = (x, y)
                break
        self.notify_observers()

    def delete_clicked_value(self, x: int, y: int):
        """
        Args:
            x (int): The x-coordinate of the clicked value to be deleted.
            y (int): The y-coordinate of the clicked value to be deleted.
        """
        self.clicked_values = [(xi, yi) for xi, yi in self.clicked_values if not (xi == x and yi == y)]
        self.notify_observers()

    def clear(self):
        self.observers = []
        self.clicked_values = []

    def get_clicked_values(self):
        """
        Returns:
            list: The list of clicked values in the format (x, y).
        """
        return self.clicked_values
