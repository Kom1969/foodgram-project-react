# Дипломный проект — сайт Foodgram
## Онлайн-сервис «Продуктовый помощник»
### Описание
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
### Технологии
- Python 3.10
- Django - свободный фреймворк для веб-приложений на языке Python.
- Django REST Framework - мощный и гибкий набор инструментов для создания веб-API.

### Учетные данные администратора
- Логин: admin7
- Пароль: kim2005

### Запуск проекта
- Клонировать репозиторий foodgram-project-react
- Перейти в директорию infra
```
cd foodgram-project-react/infra
```
- В папке infra выполните команду 
```
docker-compose up
```
- При выполнении этой команде сервис frontend, описанный в docker-compose.yml подготовит файлы, необходимые для работы фронтенд-приложения, а затем прекратит свою работу.
### После запуска увидеть спецификацию API вы сможете по адресу:
```
 http://localhost/api/docs/
```

### Backend
```
cd foodgram-project-react
```
- Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустить проект:
```
python3 manage.py runserver
```
### Приложения
- Создайте приложения согласно спецификации API
### Модели 
- Создайте модели согласно спецификации API
### ViewSets
- Во вьюсетах вам потребуется добавлять дополнительные action
### Serializers
- Сериализаторы должны соовествовать требованиям

### Запустите миграции
```
python manage.py makemigrations
python manage.py migrate
```
### Создание суперюзера
```
python manage.py createsuperuser
```
### Примеры
- Список пользователей
```
GET http://127.0.0.1:8000/api/users/
```
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/?page=4",
  "previous": "http://foodgram.example.org/api/users/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": false
    }
  ]
}
```
- Регистрация пользователя
```
POST http://127.0.0.1:8000/api/users/
```
```
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "Qwerty123"
}
```
- Изменение пароля
```
POST http://127.0.0.1:8000/api/users/set_password/
```
```
{
  "new_password": "string",
  "current_password": "string"
}
```
- Cписок тегов
```
GET http://127.0.0.1:8000/api/tags/
```
```
[
  {
    "id": 0,
    "name": "Завтрак",
    "color": "#E26C2D",
    "slug": "breakfast"
  }
]
```
- Получение тега
```
POST http://127.0.0.1:8000/api/tags/{id}/
```
```
{
  "id": 0,
  "name": "Завтрак",
  "color": "#E26C2D",
  "slug": "breakfast"
}
```
- Список рецептов
```
GET  http://127.0.0.1:8000/api/recipes/
```
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```
- Скачать список покупок
```
GET http://127.0.0.1:8000/api/recipes/download_shopping_cart/
```
```
{
  "detail": "Учетные данные не были предоставлены."
}
```
- Добавить рецепт в избранное
```
POST http://127.0.0.1:8000/api/recipes/{id}/favorite/
```
```
{
  "id": 0,
  "name": "string",
  "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
  "cooking_time": 1
}
```
- Мои подписки
```
 http://127.0.0.1:8000/api/users/subscriptions/
```
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/users/subscriptions/?page=4",
  "previous": "http://foodgram.example.org/api/users/subscriptions/?page=2",
  "results": [
    {
      "email": "user@example.com",
      "id": 0,
      "username": "string",
      "first_name": "Вася",
      "last_name": "Пупкин",
      "is_subscribed": true,
      "recipes": [
        {
          "id": 0,
          "name": "string",
          "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
          "cooking_time": 1
        }
      ],
      "recipes_count": 0
    }
  ]
}
```
- Список ингредиентов
```
GET http://127.0.0.1:8000/api/ingredients/
```
```
[
  {
    "id": 0,
    "name": "Капуста",
    "measurement_unit": "кг"
  }
]
```

### Автор
- Михаил Корюкин
```
https://github.com/Kom1969
```
