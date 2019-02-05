from tornado.web import RequestHandler
from models.data_base import Data_base
from models.book import Book
from models.order import Order

class OrderHeandler(RequestHandler):
    def get(self):
        book = self.get_book(self.get_argument('book').replace('-', ' '))   
        self.render('pages/order-page.html', book=book)

    def post(self):
        self.save_order(
            self.get_argument('book_title'),
            self.get_argument('cash'),
            self.get_argument('first_name'),
            self.get_argument('second_name'),
            self.get_argument('email'),
            self.get_argument('phone'),
            self.get_argument('adress')
        )
        self.render("pages/order-complete.html")


    def save_order(self, book, cash, f_name, s_name, email, phone, adress):
        db = Data_base().library
        Order(book, cash, f_name + ' ' + s_name, email, phone, adress).save()


    def get_book(self, title):
        db = Data_base().library
        print(title)
        for book in Book.objects(title=title):
            return {
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publisher': book.publisher,
                'ganre': book.genre,
                'publishing_date': book.publishing_date,
                'rating': book.rating,
                'price': book.price
            }
