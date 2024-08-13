from database import books

# Criar função par listagem de livros
def list_books():
    return books


# Buscar livro por id
def get_book_by_id(id: int) -> dict:
    for book in books:
        if book["id"] == id:
            return book
    return {}
        
        
# Retornar os livros que pertencem ao gênero passado pelo usuário
def get_book_by_genre(genre: str):
    filtered_books = []
    for book in books:
        if book["main_genre"] == genre:
            filtered_books.append(book)
    return filtered_books
    return {"Nenhum livro encontrado"}

# Adicionar novos livros ao banco de dados
# {
#         "title": "Jogos Vorazes: em chamas",
#         "price": 40.20,
#         "main_genre": "Ficção"
#     }
# Gerar o ID
def add_book(book_data: dict):
    last_id = 0
    for book in books:
        if book["id"] > last_id:
            last_id = book["id"]
        book_data["id"] = last_id + 1
    books.append(book_data)
    return book_data