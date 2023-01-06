import tkinter as tk
from abc import ABC


class App(ABC):
    class Frame(tk.Frame):
        def __init__(self, *args, **kwargs):
            kwargs['bg'] = '#ffffff'
            super().__init__(*args, **kwargs)

    def __init__(self, title='App'):
        self.root = tk.Tk()

        self.root.title(title)
        self.root.state('zoomed')
        self.root['bg'] = '#ffffff'

    def run(self):
        self.root.mainloop()
