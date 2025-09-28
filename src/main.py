import os
from dotenv import load_dotenv

def print_author():
    load_dotenv(dotenv_path='secret.env')  # Загружаем переменные
    author = os.getenv('AUTHOR')  # Читаем переменную
    print(f"Автор проекта: {author}")

print_author()