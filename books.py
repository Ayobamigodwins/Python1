class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_details(self):
        print(f"{self.title} by {self.author} with {self.pages} pages")


book1 = Book(title="The Prince", author="Noccolo Machiavelli", pages=250)

book1.show_details()