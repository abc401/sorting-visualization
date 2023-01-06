import tkinter as tk
from algorithms.visualization import Visualization


class SelectionSortVisualization(Visualization):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.compared = {
            'index': 0,
            'color': '#00ff00'
        }

        self.destination = {
            'index': 0,
            'color': '#ff0000'
        }

        self.maximum = {
            'index': 0,
            'color': '#0000ff'
        }

        self.draw()

    def sort(self):
        self.sorting = True

        for i in range(len(self.array)):
            self.destination['index'] = self.maximum['index'] = i

            for j in range(i, len(self.array)):
                if self.array[j] < self.array[self.maximum['index']]:
                    self.maximum['index'] = j
                self.compared['index'] = j
                self.draw()

                if not self.sorting:
                    break

            self.swap(i, self.maximum['index'])
            if not self.sorting:
                break

        self.sorting = False

    def draw(self):
        super().draw()

        if self.sorting:
            self.draw_item(self.compared['index'], self.compared['color'])
            self.draw_item(self.maximum['index'], self.maximum['color'])

            self.draw_item(self.destination['index'], self.destination['color'])

        self.canvas.update()
