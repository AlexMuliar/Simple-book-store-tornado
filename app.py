import tornado.web
from testing.test import TestHeandler
from handlers.book_list import BookListHeadler, SearchBookHeandler
from handlers.book_page import BookPageHeadler, StoryHandler
from handlers.author_page import AuthorPageHeadler
from handlers.about import AboutHeandler
from handlers.contact_page import ContactHeandler
from handlers.order_page import OrderHeandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/lib', BookListHeadler),
            (r'/search', SearchBookHeandler),
            (r'/book/([A-Za-z0-9-:,]+)', BookPageHeadler),
            (r'/author/([A-Za-z0-9-]+)', AuthorPageHeadler),
            (r'/purchase', OrderHeandler),
            (r'/about', AboutHeandler),
            (r'/contact', ContactHeandler),
            (r"/story/([0-9]+)", StoryHandler),
            (r'/test', TestHeandler),
        ]
        settings = {
            'template_path': 'templates',
            'static_path': 'static',
          #  'ui_modules': {'Result': SolutionModule},
            'debug': True
        }
        tornado.web.Application.__init__(self, handlers, **settings)