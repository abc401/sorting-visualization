import tkinter as tk
from app import App

from algorithms.bubble_sort import BubbleSortVisualization
from algorithms.selection_sort import SelectionSortVisualization
from algorithms.merge_sort import MergeSortVisualization
from algorithms.quick_sort import QuickSortVisualization


class SortingVisualizer(App):

    def __init__(self):
        super().__init__('Sorting Visualization')

        self.buttons = self.Frame(self.root)

        self.algos = (
            'Bubble sort',
            'Selection sort',
            'Merge sort',
            'Quick sort'
        )

        self.algo_dict = {
            self.algos[0]: BubbleSortVisualization,
            self.algos[1]: SelectionSortVisualization,
            self.algos[2]: MergeSortVisualization,
            self.algos[3]: QuickSortVisualization
        }

        self.selected_algo = tk.StringVar()
        self.selected_algo.set(self.algos[0])
        self.algo_menu = tk.OptionMenu(self.buttons, self.selected_algo, command=self.set_algo, *self.algos)
        self.algo_menu.pack(side='left',  padx=(5, 0))

        self.start_btn = tk.Button(self.buttons, text='Start', command=self.sort)
        self.start_btn.pack(side='right', padx=(10, 5))

        self.randomize_btn = tk.Button(self.buttons, text='Randomize', command=self.randomize)
        self.randomize_btn.pack(side='right')

        self.buttons.pack(side='top', fill='x')

        self.buttons.update()
        self.root.update()

        width, height = (
            self.root.winfo_width(),
            self.root.winfo_height() - self.buttons.winfo_height()
        )

        self.root.bind("<MouseWheel>", self.on_mouse_wheel)
        self.visualization = BubbleSortVisualization(self.root, width, height)

    def randomize(self):
        self.visualization.randomize()

    def set_algo(self, choice):
        try:
            self.visualization.sorting = False
            self.visualization = self.algo_dict[choice].from_visualization(self.visualization)
        except KeyError:
            print(choice)

    def sort(self):
        self.visualization.sort()

    def on_mouse_wheel(self, event):
        step_size = 1
        if event.delta == 120:
            self.visualization.item_width += step_size
        elif event.delta == -120:
            self.visualization.item_width -= step_size


if __name__ == '__main__':
    SortingVisualizer().run()
    # print([1, 2, 3, 4, 5, 6, 7, 8, 9][0:2])
