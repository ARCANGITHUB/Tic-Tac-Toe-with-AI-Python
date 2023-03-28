class Painting:
    museum = "the Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def info(self):
        return f'"{self.title}" by {self.artist} ({self.year}) ' \
               f'hangs in {self.museum}.'


painting = Painting(input(), input(), input())

print(painting.info())
