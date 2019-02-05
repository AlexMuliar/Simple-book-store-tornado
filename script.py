from models.data_base import Data_base
from models.author import Author
from models.book import Book

if __name__ == "__main__":
    db = Data_base().library
    for obj in Book.objects():
       obj.price = float(input(obj.title + ": "))
       obj.save()