from tornado.web import RequestHandler

class AboutHeandler(RequestHandler):
    def get(self):
        print('aobut pageee')
        self.render("pages/about.html")
