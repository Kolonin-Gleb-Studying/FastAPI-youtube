from fastapi import FastAPI, Query, Path

# Импорт моделей pydantic для валидации данных
from schemas import Book

app = FastAPI()

# Обработчик get запроса на главную страницу
@app.get('/')
def home():
    return {"key": "Hello"}

# Обработчик get запроса с параметром
@app.get('/{pk}') # Пример: http://127.0.0.1:8000/5?q=22
def get_item(pk: int, q: str = None): #fastAPI проведёт валидацию типов данных, поэтому указание типа данных - полезно
    return {"key": pk, "q": q}

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {"key": pk, "item": item}

''' По одному адресу могут приниматься запросы разных типов '''
@app.post('/book') # POST - Для публикации данных на сервер
def create_book(item: Book):
    return item
@app.get('/book')
def get_book(q: str = Query(..., min_length=2, max_length=5, description="Описание параметра")): # Обязательный ПАРАМЕТР с ограничениями
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)): # Ограничения на ПУТЬ и ПАРАМЕТР
    return {"pk": pk, "pages": pages}



'''
Запуск сервера:
uvicorn main:app --reload --port 8000

FastAPI автоматически создаёт Swagger документацию к обработчикам запросов.
Она доступна по адресу:
http://127.0.0.1:8000/docs
Или
http://127.0.0.1:8000/redoc
'''

