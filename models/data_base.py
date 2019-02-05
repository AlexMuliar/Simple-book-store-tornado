import mongoengine as me

class Data_base(object):
    def __init__(self):
        self.library = me.connect('Library')


if __name__ == "__main__":
    my_db = Data_base()
    print(my_db.db)
