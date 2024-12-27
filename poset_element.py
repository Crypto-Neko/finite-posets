class PosetElement:
    def __init__(self, value, poset=None):
        self.value = value
        self.poset = poset

    def __lt__(self, other):
        if self.poset != self.other
