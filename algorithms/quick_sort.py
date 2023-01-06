from algorithms.visualization import Visualization


class QuickSortVisualization(Visualization):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pivot = 0
        self.left = 0
        self.right = 0

        self.draw()

    def sort(self):
        self.sorting = True
        self.quick_sort(0, len(self.array)-1)
        self.sorting = False

    def partition(self, left: int, right: int):
        self.pivot = left
        self.left = left
        self.right = right
        while self.left < self.right and self.sorting:
            while self.array[self.left] <= self.array[self.pivot] and self.left < len(self.array) and self.sorting:
                self.left += 1
                self.draw()
            while self.array[self.right] > self.array[self.pivot] and self.sorting:
                self.right -= 1
                self.draw()
            if self.left < self.right:
                self.swap(self.left, self.right)
                self.draw()
        self.swap(self.pivot, self.right)
        self.draw()
        return self.right

    def quick_sort(self, left: int, right: int):
        if left < right and self.sorting:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot-1)
            self.quick_sort(pivot+1, right)

    def draw(self):
        super().draw()
        if self.sorting:
            self.draw_item(self.left, '#ff0000')
            self.draw_item(self.right, '#0000ff')
            self.draw_item(self.pivot, '#00ff00')
        self.canvas.update()
