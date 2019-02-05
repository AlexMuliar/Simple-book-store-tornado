from models.author import Author
from models.data_base import Data_base

if __name__ == '__main__':
    db = Data_base().library
    a = Author({
        'first': input("F_name: "),
        'second': input("S_name: "),
        'addactive': input("Add_name: ") or None},
        {
        'day': 2,
        'month': 6,
        'year': 1920
        },
    )
    print(a.name['first'])
    date = [int(i) for i in input("date: ").split()]
    date.extend([None, None])
    a.born['day'], a.born['month'], a.born['year'] = date[2] or None, date[1] or None, date[0] or None
    a.img = open(r"C:\Users\sashk\PycharmProjects\Library\static\image\\" + input("Img: "), 'rb')
    a.save()
