from models.book import Book
from models.data_base import Data_base

if __name__ == '__main__':
    base = Data_base().db
    print(base)
   # img = open('starwars.jpg', 'rb')
   # img.show()
    my_book = Book('New_book', 'Vasya Pupkin', 'Test defult cover', 'govno std', 'Zalupa', 2043)
    my_book.save()
    print(my_book.publishing_date)