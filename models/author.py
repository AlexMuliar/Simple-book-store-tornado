import proto_book
from mongoengine import Document, StringField, DateTimeField, IntField, ImageField, FileField, FloatField, DictField

class Author(Document):
    name = DictField()
    born = DictField()
    description = StringField()
    img = FileField()


if __name__ == '__main__':
    a = Author({
        'first': 'Isaac',
        'second': 'Asimov'},
        {
        'day': 2,
        'month': 6,
        'year': 1920
        },
        r'C:\Users\sashk\PycharmProjects\Library\static\image\Isaac-Asimov-bw.jpg'
    )
    print(a.name['first'])