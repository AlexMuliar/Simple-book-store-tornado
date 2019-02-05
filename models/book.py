from mongoengine import Document, StringField, DateTimeField, IntField, ImageField, FileField, FloatField

class Book(Document):
    title = StringField()
    author = StringField()
    description = StringField()
    publisher = StringField()
    genre = StringField()
    publishing_date = IntField()
    img = FileField()
    rating = FloatField()
    price = FloatField()

if __name__ == '__main__':
    a = Book('Lord of Rings', 'Tolkien', 'Cool book about ring', 'publisher', 'fantasy', 1968)
    print(a.author)