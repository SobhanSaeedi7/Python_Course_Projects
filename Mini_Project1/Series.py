from Media import Media

class Series(Media):
    def __init__(self, id, n, di, s, u, du, c, e):
        super().__init__(id, n, di, s, u, du, c)
        self.episods = e

