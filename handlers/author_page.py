from tornado.web import RequestHandler
from models.data_base import Data_base
from models.author import Author
from models.book import Book
from PIL import Image
from io import BytesIO
import base64


class AuthorPageHeadler(RequestHandler):
    def get(self, author):
        author = self.get_author(author.replace('-', ' '))
        if author:
            print(author['name'])
            books = self.get_books(author['name']['first'] + " " + author['name']['second'])

            for i in books:
                print(i['title'])

            self.render('pages/author-page.html', author=author, books=books)
        else:
            self.write_error(404)

    def get_author(self, author):
        db = Data_base().library
        writer = str()
        for man in Author.objects(name__first=author.split()[0], name__second=author.split()[-1]):
            writer = {
                'name': man.name,
                'born': man.born,
                'img': self.get_image(man.img),
                'description': man.description
            }
        return writer

    def get_books(self, author):
        db = Data_base().library
        books = list()
        for book in Book.objects(author=author):
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