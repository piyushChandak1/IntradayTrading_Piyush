class Supertrend:
    def __init__(self):
        self.data = []

    def decrease_size(self):
        self.data = self.data[len(self.data) // 2:]

    def predict(self, cur_price):
        if self.data[-1] >= cur_price:
            return -1
        else:
            return 1

    def decreasearray(self):
        if len(self.data) > 10000:
            self.decrease_size()
