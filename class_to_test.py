import numpy as np

class SomeClass:
    def __init__(self):
        self.some_attribute = 42
        self.some_numpy_array = np.arange(24)

    def some_method(self):
        # just doubles some_attribute every time it's called
        self.some_attribute = self.some_attribute*2

    def reshape_array(self, new_shape=(2,12)):
        return self.some_numpy_array.reshape(new_shape)
