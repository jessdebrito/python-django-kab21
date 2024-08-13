
# from data_types import list
# from data_types import tuple
#from data_types import dict
from manager import manager_books

if __name__ == "__main__":
    # list.list_fundamentals() 
    # list.list_looping()
    # tuple.tuple_fundamentals()
    # dict.dict_fundamentals()
    # dict.dict_looping()
    # print(manager_books.get_book_by_id(1))
    # print(manager_books.get_book_by_genre("Fantasia"))
    
    book_data = {
        "title": "Filho de Netuno",
        "price": 45.80,
        "main_genre": "Fantasia"
    }
    print(manager_books.add_book(book_data))