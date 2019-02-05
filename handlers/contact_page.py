from tornado.web import RequestHandler

class ContactHeandler(RequestHandler):
    def get(self):
        self.render("pages/contact.html")