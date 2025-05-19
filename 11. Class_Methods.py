class Book():
    totle_books = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.totle_books += 1

b=Book("The Alchemist","Paulo Coelho", 208)
b2=Book("The Subtle Art of Not Giving a F*ck","Mark Manson", 232)
b3=Book("The Subtle Art of Not Giving a F*ck","Mark Manson", 232)
print(b.totle_books)        