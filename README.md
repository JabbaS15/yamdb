# YaMDb - онлайн сервис для сбора отзывов пользователей на различные произведения
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=043A6B)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=ffffff&color=043A6B)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=ffffff&color=043A6B)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=ffffff&color=043A6B)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=ffffff&color=043A6B)](https://cloud.yandex.ru/)

#### Статус проекта:
![example workflow](https://github.com/JabbaS15/yamdb/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание проекта:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 

Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.


## Работа с API:
| Увидеть [спецификацию](https://github.com/JabbaS15/yamdb/blob/master/api_yamdb/static/redoc.yaml) API вы сможете по адресу | `.../api/v1/docs/` |
|--------|---------|

### Доступные ресурсы:
| Ресурсы | Возможности |
|:---------:|-------|
| auth | аутентификация |
| users | пользователи |
| titles | произведения, к которым пишут отзывы (определённый фильм, книга или песенка) |
| categories | категории (типы) произведений («Фильмы», «Книги», «Музыка») |
| genres | жанры произведений. Одно произведение может быть привязано к нескольким жанрам |
| reviews | отзывы на произведения. Отзыв привязан к определённому произведению |
| comments | комментарии к отзывам. Комментарий привязан к определённому отзыву |

### Authentication SimpleJWT
Используется аутентификация с использованием JWT-токенов
|Key          |Value           |
|-------------|----------------|
|Authorization|Bearer `token`  |

- Аутентификация выполняется с помощью djoser-токена.
- На запросы POST, PUT и PATCH в ответ API возвращает объект.

### Регистрация пользователей
Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
YaMDB отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес `email`.
Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

### Связанные данные и каскадное удаление
- При удалении объекта пользователя User удаляются все отзывы и комментарии этого пользователя (вместе с оценками-рейтингами).
- При удалении объекта произведения Title удаляются все отзывы к этому произведению и комментарии к ним.
- При удалении объекта отзыва Review удаляются все комментарии к этому отзыву.
- При удалении объекта категории Category остаются связанные с этой категорией произведения.
- При удалении объекта жанра Genre остаются связанные с этим жанром произведения.

### Пользовательские роли
- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (`user`) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (`moderator`) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- Администратор (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

### Самостоятельная регистрация новых пользователей
Пользователь отправляет POST-запрос с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
Сервис YaMDB отправляет письмо с кодом подтверждения (`confirmation_code`) на указанный адрес email.
Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполнить поля в своём профайле (описание полей — в документации).

### Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт `api/v1/users/` (описание полей запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой `email` и `username` на эндпоинт `/api/v1/auth/signup/`, в ответ ему должно прийти письмо с кодом подтверждения.
Далее пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен), как и при самостоятельной регистрации.

## Инструкция по развёртыванию:
1. Загрузите проект:
```bash
git clone https://github.com/JabbaS15/yamdb.git
```
2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
python api_yamdb/manage.py migrate 
```
5. В папке с файлом manage.py выполните команду запуска:
```bash
python3 manage.py runserver
```

### Описание команд для запуска приложения в контейнерах:
1. Заполните файл env. по шаблону.
````
DB_ENGINE="указываем, что работаем с postgresql"
DB_NAME="имя базы данных"
POSTGRES_USER="логин для подключения к базе данных"
POSTGRES_PASSWORD="пароль для подключения к БД (установите свой)"
DB_HOST="название сервиса (контейнера)"
DB_PORT="порт для подключения к БД"
EMAIL_HOST_USER="Email"
EMAIL_HOST_PASSWORD="Email Password"
````
2. Перейдите в директорию `infra/`
#### Выполните команды:
- Применить миграции.
- Создать суперпользователя.
- Собрать статику.
- Запуск контейнера.
- Для остановки контейнеров, выполните:

````bash
docker-compose up -d --build

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input

docker-compose up

docker-compose down -v
````

#### Описание команды для заполнения базы данными.

3. Запустить терминал и выполнить команды:

```bash
python manage.py shell
```
````python
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
````
```bash
python manage.py loaddata fixtures.json
```

### Настроен Workflow и состоит из четрыех шагов:
- Проверка кода на соответствие PEP8
- Сборка и публикация образа бекенда на DockerHub.
- Автоматический деплой на удаленный сервер.
- Отправка уведомления в телеграм-чат.

### Автор проекта:
| [Шведков Роман](https://github.com/JabbaS15) | [Александр Хоменко](https://github.com/alkh0304) | [Марк Мазуров](https://github.com/MarkMazurov) |
