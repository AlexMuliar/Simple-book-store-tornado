from models.data_base import Data_base
from models.book import Book

if __name__ == '__main__':
    db = Data_base().library
    new_book = Book()
    new_book.title = input('title: ')
    new_book.author = input('author: ')
    new_book.publisher = input('publisher: ')
    new_book.rating = float(input('rating: '))
    new_book.publishing_date = int(input('publishing_date: '))
    new_book.genre = input('genre: ')
    new_book.description = input('description: ')
    new_book.img = open(input('image: '), 'rb')
    new_book.save()
