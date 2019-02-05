from tornado.web import RequestHandler
from models.data_base import Data_base
from models.book import Book
from PIL import Image
from io import BytesIO
import base64

class BookPageHeadler(RequestHandler):
    def get(self, book):
        book = self.get_book(book.replace('-', ' '))
        self.render('pages/book-page.html', book=book)


    def get_book(self, book):
        db = Data_base().library
        for book in Book.objects(title=book):
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

class StoryHandler(RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)