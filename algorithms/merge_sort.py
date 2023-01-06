from algorithms.visualization import Visualization


class MergeSortVisualization(Visualization):
    def __init__(self, *args, **kwargs):

        self.left = 0
        self.right = 0
        self.destination = 0

        super().__init__(*args, **kwargs)

        self.draw()

    def sort(self):
        self.sorting = True
        self.merge_sort(0, len(self.array))
        self.sorting = False

    def merge_sort(self, left, right):
        if right <= left + 1 or not self.sorting:
            return

        middle = (left + right) // 2
        self.merge_sort(left, middle)
        self.merge_sort(middle, right)

        self.merge(left, middle, right)

    def merge(self, left: int, middle: int, right: int):
        self.left = left
        self.right = right - 1

        left_arr = self.array[left:middle]
        right_arr = self.array[middle:right]

        li = 0      # Left array index
        ri = 0      # Right array index
        self.destination = left    # Main array index

        while li < len(left_arr) and ri < len(right_arr) and self.sorting:
            if left_arr[li] < right_arr[ri]:
                self.array[self.destination] = left_arr[li]
                li += 1
            else:
                self.array[self.destination] = right_arr[ri]
                ri += 1

            self.draw()
            self.destination += 1

        while li < len(left_arr) and self.sorting:
            self.array[self.destination] = left_arr[li]
            li += 1

            self.draw()
            self.destination += 1

        while ri < len(right_arr) and self.sorting:
            self.array[self.destination] = right_arr[ri]
            ri += 1

            self.draw()
            self.destination += 1

    def draw(self):
        super().draw()

        if self.sorting:
            self.draw_item(self.left, '#ff0000')
            self.draw_item(self.right, '#0000ff')
            self.draw_item(self.destination, '#00ff00')

        self.canvas.update()
