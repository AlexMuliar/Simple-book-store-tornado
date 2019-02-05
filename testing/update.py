from models.data_base import Data_base
from models.book import Book

if __name__ == '__main__':
    db = Data_base().library
    title = input('Title: ')
    for book in Book.objects(title=title):
        a = book
        print(a)
        #book.description = input()
        #book.img = open(input('Image: '), 'rb')
        a.description = input()
        a.save()
