import tkinter as tk

class NumericEntry(tk.Frame):
    """
    Attributes:
        master: The parent widget.
        default (int): The default value for the entry.
        label (str): The label text.
    """

    def __init__(self, master, default, label):
        """
        Args:
            master: The parent widget.
            default (int): The default value for the entry.
            label (str): The label text.
        """
        super().__init__(master)
        self.label = tk.Label(self, text=label)
        self.label.pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(self)
        self.entry.insert(0, str(default))
        self.entry.pack(side=tk.LEFT)

    def get_value(self):
        """
        Returns:
            int: The integer value entered in the entry widget. If the entry contains a non-numeric value
                 or a value less than or equal to 1, returns 0.
        """
        try:
            value = int(self.entry.get())
            if value <= 1:
                return 0
            return value
        except ValueError:
            return 0
