from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/")
async def initial_api():
    return {"message":"hello world"}

@app.get("/books")
async def get_all_books():
    return BOOKS

#http://127.0.0.1:8000/books/Title%20One
#path parameters
@app.get("/books/{book_name}")
async def bookOne(book_name: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_name.casefold():
            return book
        
#query parameters
@app.get("/books/")
async def getBookByCategory(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#path plus query
#http://127.0.0.1:8000/books/author%20two/?category=science
@app.get("/books/{book_author}/")
async def getBooksByAuthorAndCategory(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
        book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#POST request
@app.post("/books/create_book")
async def createBooks(new_book=Body()):
    BOOKS.append(new_book)


#PUT
@app.put("/books/update_book")
async def updateBooks(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

#Delete
@app.delete("/books/{book_title}")
async def deleteBooks(book_title: str):
    for i, book in enumerate(BOOKS):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


