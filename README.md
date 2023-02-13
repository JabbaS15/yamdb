# YaMDb - Онлайн сервис для сбора отзывов на произведения.
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=013220)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=013220)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=013220)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=ffffff&color=013220)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=ffffff&color=013220)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=013220)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=013220)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=ffffff&color=013220)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=ffffff&color=013220)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=ffffff&color=013220)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=ffffff&color=013220)](https://cloud.yandex.ru/)

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
### Authentication SimpleJWT
Используется аутентификация с использованием JWT-токенов
|Key          |Value           |
|-------------|----------------|
|Authorization|Bearer `token`  |

- Аутентификация выполняется с помощью djoser-токена.
- На запросы POST, PUT и PATCH в ответ API возвращает объект.

### Доступные запросы:
| Запрос | Эндпоинт | Метод |
|--------|:---------|-------|
| [Спецификация](https://github.com/JabbaS15/yamdb/blob/master/api_yamdb/static/redoc.yaml) API | `.../api/v1/docs/` | - |
| Регистрация нового пользователя |`.../api/v1/auth/signup/`| POST |
| Получение JWT-токена |`.../api/v1/auth/token/`| POST |
| Получение списка всех категорий |`.../api/v1/categories/`| GET |
| Добавление новой категории |`.../api/v1/categories/`| POST |
| Удаление категории |`.../api/v1/categories/{slug}/`| DELETE |
| Получение списка всех жанров |`.../api/v1/genres/`| GET |
| Добавление жанра |`.../api/v1/genres/`| POST |
| Удаление жанра |`.../api/v1/genres/{slug}/`| DELETE |
| Получение списка всех произведений |`.../api/v1/titles/`| GET |
| Добавление произведения |`.../api/v1/titles/`| POST |
| Получение информации о произведении |`.../api/v1/titles/{title_id}/`| GET |
| Частичное обновление информации о произведении |`.../api/v1/titles/{title_id}/`| PATCH |
| Удаление произведения |`.../api/v1/titles/{title_id}/`| DELETE |
| Получение списка всех отзывов |`.../api/v1/titles/{title_id}/reviews/`| GET |
| Добавление нового отзыва |`.../api/v1/titles/{title_id}/reviews/`| POST |
| Получение отзыва по id |`.../api/v1/titles/{title_id}/reviews/{review_id}/`| GET |
| Частичное обновление отзыва по id |`.../api/v1/titles/{title_id}/reviews/{review_id}/`| PATCH |
| Удаление отзыва по id |`.../api/v1/titles/{title_id}/reviews/{review_id}/`| DELETE |
| Получение списка всех комментариев к отзыву |`.../api/v1/titles/{title_id}/reviews/{review_id}/comments/`| GET |
| Добавление комментария к отзыву |`.../api/v1/titles/{title_id}/reviews/{review_id}/comments/`| POST |
| Получение комментария к отзыву |`.../api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`| GET |
| Частичное обновление комментария к отзыву |`.../api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`| PATCH |
| Удаление комментария к отзыву |`.../api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`| DELETE |
| Получение списка всех пользователей |`.../api/v1/users/`| GET |
| Добавление пользователя |`.../api/v1/users/`| POST |
| Получение пользователя по username |`.../api/v1/users/{username}/`| GET |
| Изменение данных пользователя по username |`.../api/v1/users/{username}/`| PATCH |
| Удаление пользователя по username |`.../api/v1/users/{username}/`| DELETE |
| Получение данных своей учетной записи |`.../api/v1/users/me/`| GET |
| Изменение данных своей учетной записи |`.../api/v1/users/me/`| PATCH |

### Аутентификация
#### Алгоритм регистрации пользователей
1. Пользователь отправляет _**POST**_-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `.../api/v1/auth/signup/`.  
> Пример запроса:  
> _**POST .../api/v1/auth/signup/**_  
> ```JSON
> {
>   "email": "string",
>   "username": "string"
> }
> ```
> Пример ответа (200):
> ```JSON
> {
>   "email": "string",
>   "username": "string"
> }
> ```
2. YaMDB отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес `email`.
3. Пользователь отправляет _**POST**_-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (_JWT_-токен).
> Пример запроса:  
> _**POST .../api/v1/auth/token/**_  
> ```JSON
> {
>   "username": "string",
>   "confirmation_code": "string"
> }
> ```
> Пример ответа (200):
> ```JSON
> {
>   "token": "string"
> }
> ```
4. При желании пользователь отправляет _**PATCH**_-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле.
> Пример запроса:  
> _**POST .../api/v1/users/me/**_  
> ```JSON
> {
>   "username": "string",
>   "email": "user@example.com",
>   "first_name": "string",
>   "last_name": "string",
>   "bio": "string"
> }
> ```
> Пример ответа (200):
> ```JSON
> {
>   "username": "string",
>   "email": "user@example.com",
>   "first_name": "string",
>   "last_name": "string",
>   "bio": "string"
>   "role": "user"
> }
> ```

### Связанные данные и каскадное удаление.
- При удалении объекта пользователя User удаляются все отзывы и комментарии этого пользователя (вместе с оценками-рейтингами).
- При удалении объекта произведения Title удаляются все отзывы к этому произведению и комментарии к ним.
- При удалении объекта отзыва Review удаляются все комментарии к этому отзыву.
- При удалении объекта категории Category остаются связанные с этой категорией произведения.
- При удалении объекта жанра Genre остаются связанные с этим жанром произведения.

### Пользовательские роли.
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** (`user`) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор** (`moderator`) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- **Администратор** (`admin`) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер** Django должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.

### Самостоятельная регистрация новых пользователей.
Пользователь отправляет POST-запрос с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
Сервис YaMDB отправляет письмо с кодом подтверждения (`confirmation_code`) на указанный адрес email.
Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполнить поля в своём профайле (описание полей — в документации).

### Создание пользователя администратором.
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт `api/v1/users/` (описание полей запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой `email` и `username` на эндпоинт `/api/v1/auth/signup/`, в ответ ему должно прийти письмо с кодом подтверждения.
Далее пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен), как и при самостоятельной регистрации.

## Инструкция по развёртыванию.
### Локально:
1. Загрузите проект:
```bash
git clone https://github.com/JabbaS15/yamdb.git
```
2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
python3 -m pip install --upgrade pip
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


### Настроен Workflow и состоит из четрыех шагов:
- Проверка кода на соответствие PEP8
- Сборка и публикация образа бекенда на DockerHub.
- Автоматический деплой на удаленный сервер.
- Отправка уведомления в телеграм-чат.

### Описание команд для запуска приложения в контейнерах:
1. На Гитхабе добавьте данные в `Settings - Secrets - Actions secrets`:
```
DOCKER_USERNAME - имя пользователя в DockerHub
DOCKER_PASSWORD - пароль пользователя в DockerHub
HOST - ip-адрес сервера
USER - пользователь
SSH_KEY - приватный ssh-ключ
PASSPHRASE - кодовая фраза для ssh-ключа
SECRET_KEY - секретный ключ приложения django
ALLOWED_HOSTS - список разрешённых адресов
TELEGRAM_TO - id своего телеграм-аккаунта
TELEGRAM_TOKEN - токен бота
DB_NAME - postgres (по умолчанию)
DB_ENGINE - django.db.backends.postgresql
DB_HOST - db (по умолчанию)
DB_PORT - 5432 (по умолчанию)
POSTGRES_USER - postgres (по умолчанию)
POSTGRES_PASSWORD - postgres (по умолчанию)
```
2. На сервере остановите службу nginx:
```
sudo systemctl stop nginx 
```
3. Установите docker и docker-compose:
```bash
sudo apt install docker.io
sudo apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh 
sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
sudo apt install docker-ce docker-compose -y
```
Скопируйте файлы docker-compose.yaml и nginx/default.conf из вашего проекта на сервер в home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.

4. После успешного деплоя перейдите в директорию `infra/` и выполните команды:
- Для остановки контейнеров, выполните `docker-compose down -v`.

- Запуск контейнера.
- Применить миграции.
- Создать суперпользователя.
- Собрать статику.

````bash
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
````

#### Описание команды для заполнения базы данными.
5. Запустить терминал и выполнить команды:
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

### Автор проекта:
| [Шведков Роман](https://github.com/JabbaS15) | [Александр Хоменко](https://github.com/alkh0304) | [Марк Мазуров](https://github.com/MarkMazurov) |
