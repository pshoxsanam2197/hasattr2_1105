# 3-m
class Book:
    def __init__(self, title, auther):
        self.title = title
        self.auther = auther

    def read(self, page):
        print(f"Sahifa: {page}")

class Notebook:
    def write(self, text):
        print(f"Text: {text}")

class Library:
    def open_book(self, obj, page):
        if hasattr(obj, "read"):
            obj.read(page)
        else:
            print(f"read methodi topilmadi")

b1 = Book('Binafsha shulasi', 'Usoma Muslim' )
n1 = Notebook()

library = Library()

library.open_book(b1, 4)
print("----")
library.open_book(n1,8)
