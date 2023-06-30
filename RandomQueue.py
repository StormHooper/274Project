import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the methodA of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n <= 0:
            raise IndexError()
        random_idx = random.randint(self.j, self.n-1)
        temp_rand = self.a[random_idx]
        self.a[random_idx] = self.a[self.j]
        self.a[self.j] = temp_rand
        return super().remove()
