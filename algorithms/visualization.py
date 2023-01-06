import time
import tkinter as tk
from random import random
from abc import ABC, abstractmethod


class Visualization(ABC):
    def __init__(
            self, root: tk.Tk,
            width: int = 100, height: int = 100,
            item_width: int = 10,
            min_item_width: int = 10,
            array: list = None,
            canvas: tk.Canvas = None
    ):
        self.root = root

        self.width = width
        self.height = height

        self.sorting = False

        self.min_item_width = min_item_width
        self.max_item_width = width

        self._item_width = item_width

        self.n_items = self.width // self._item_width

        self.delay_bias = 2
        self.time_delay = self.delay_bias / self.n_items

        if array is None:
            self.array = [random() * self.height for i in range(self.n_items)]
        else:
            self.array = array

        if canvas is None:
            self.canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0, bg='#ffffff')
            self.canvas.pack()
        else:
            self.canvas = canvas

    def swap(self, index_1: int, index_2: int):
        self.array[index_1], self.array[index_2] = self.array[index_2], self.array[index_1]

    @classmethod
    def from_visualization(cls, origin):
        if origin is not None:
            return cls(
                root=origin.root,
                width=origin.width, height=origin.height,
                item_width=origin.item_width,
                min_item_width=origin.min_item_width,
                array=origin.array,
                canvas=origin.canvas
            )
        else:
            print("origin is none")

    def randomize(self):
        self.array = [random() * self.height for i in range(self.n_items)]
        self.sorting = False
        self.draw()

    @property
    def item_width(self):
        return self._item_width

    @item_width.setter
    def item_width(self, val: int):
        if self.min_item_width < val < self.max_item_width:
            self._item_width = val
            self.n_items = self.width // self._item_width
            self.time_delay = self.delay_bias / self.n_items
            self.randomize()

    def after(self, ms: int, func):
        self.canvas.after(ms, func)

    def draw_item(self, index: int, fill: str = ''):
        try:
            x0 = index * self._item_width
            y0 = self.height
            x1 = x0 + self._item_width
            y1 = self.height - self.array[index]

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
        except IndexError:
            print(index, len(self.array))

    @abstractmethod
    def sort(self):
        pass

    def draw(self):
        self.canvas.delete('all')
        for i in range(len(self.array)):
            self.draw_item(i)

        time.sleep(self.time_delay)
