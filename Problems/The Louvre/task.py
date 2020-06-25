class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year_of_creation):
        self.title = title
        self.painter = painter
        self.year_of_creation = year_of_creation


paint = Painting(input().strip(), input().strip(), input().strip())
print('"' + paint.title + '"', "by", paint.painter, "(" + paint.year_of_creation + ")", "hangs in the", paint.museum + ".")