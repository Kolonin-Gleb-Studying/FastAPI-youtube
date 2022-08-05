# Файл с pydantic моделями для валидации данных, отправляемых на сервер
from typing import List # Для аннотирования типов данных. Как строгая типизация

from pydantic import BaseModel
from datetime import date

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] # Список из жанров, что разрешены моделью Genre.
    pages: int
