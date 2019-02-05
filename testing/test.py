import tornado.web
from models.book import Book
from models.data_base import Data_base
from PIL import Image
from io import BytesIO
import base64

class TestHeandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pages/custom.html', username='Vasya')

    def get_img(self):
        buffered = BytesIO()
        db = Data_base().db
        img = 0
        for book in Book.objects():
            img = book.img
        img = Image.open(img)
        #print(img.title)
        img.save(buffered, format="JPEG")
        #print(base64.b64encode(buffered.getvalue()))
        return  b"data:image/jpeg;base64," + base64.b64encode(buffered.getvalue())