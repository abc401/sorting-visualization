import tkinter as tk
from algorithms.visualization import Visualization


class BubbleSortVisualization(Visualization):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.swapped_1 = {
            'index': 0,
            'color': '#00ff00'
        }

        self.swapped_2 = {
            'index': 0,
            'color': '#ff0000'
        }

        self.draw()

    def sort(self):
        self.sorting = True
        for i in range(len(self.array)):
            for j in range(len(self.array) - i - 1):
                self.swapped_1['index'] = j
                self.swapped_2['index'] = j + 1

                if self.array[j] > self.array[j + 1]:
                    self.swap(j, j + 1)

                self.draw()
                if not self.sorting:
                    break
            if not self.sorting:
                break

        self.sorting = False

    def draw(self):
        super().draw()

        if self.sorting:
            self.draw_item(self.swapped_2['index'], self.swapped_2['color'])

            self.draw_item(self.swapped_1['index'], self.swapped_1['color'])

        self.canvas.update()
