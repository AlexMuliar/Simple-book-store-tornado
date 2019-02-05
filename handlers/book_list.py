import tornado.web
from models.book import Book
from models.data_base import Data_base
from PIL import Image
from io import BytesIO
import base64

class BookListHeadler(tornado.web.RequestHandler):
    def get(self):
        self.render('pages/books-list.html', books=self.get_books(), search=False)

    def get_books(self):
        db = Data_base().library
        books = list()
        for book in Book.objects.order_by('-rating'):
            books.append({
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publisher': book.publisher,
                'ganre': book.genre,
                'publishing_date': book.publishing_date,
                'image': self.get_image(book.img),
                'rating': book.rating
            })
        return books

    def get_image(self, image):
        buffered = BytesIO()
        if not image:
            return None
        img = Image.open(image)
        img.save(buffered, format="JPEG")
        return b"data:image/jpeg;base64," + base64.b64encode(buffered.getvalue())

class SearchBookHeandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pages/books-list.html', books=self.get_books(self.get_argument('require')), search=self.get_argument('require'))

    def get_books(self, require):
        db = Data_base().library
        books = list()
        for book in Book.objects(title__icontains=require).order_by('-rating'):
            books.append(self.zip_book(book))
        for book in Book.objects(author__icontains=require).order_by('-rating'):
            books.append(self.zip_book(book))
            if books.count(books[-1]) > 1:
                del books[-1]
        for book in Book.objects(description__icontains=require).order_by('-rating'):
            books.append(self.zip_book(book))
            if books.count(books[-1]) > 1:
                del books[-1]
        return books

    def zip_book(self, book):
        return {
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publisher': book.publisher,
                'ganre': book.genre,
                'publishing_date': book.publishing_date,
                'image': self.get_image(book.img),
                'rating': book.rating,
                'price': book.price
            }

    def get_image(self, image):
        buffered = BytesIO()
        if not image:
            return None
        img = Image.open(image)
        img.save(buffered, format="JPEG")
        return b"data:image/jpeg;base64," + base64.b64encode(buffered.getvalue())