from fastapi import FastAPI


app = FastAPI()

# Обработчик get запроса на главную страницу
@app.get('/')
def home():
    return {"key": "Hello"}

# Обработчик get запроса с параметром
@app.get('/{pk}')
def get_item(pk: int, q: str = None): #fastAPI проведёт валидацию типов данных, поэтому указание типа данных - полезно
    return {"key": pk, "q": q}


'''
Запуск сервера:
uvicorn main:app --reload --port 8000

FastAPI автоматически создаёт Swagger документацию к обработчикам запросов.
Она доступна по адресу:
http://127.0.0.1:8000/docs
Или
http://127.0.0.1:8000/redoc
'''
