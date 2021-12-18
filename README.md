# Дипломный проект | Yandex Practicum #
>Проект выполнил Ситнов Руслан Сергеевич *[Ссылка на сайт](http://178.154.199.160/recipes)*
##
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
##
Foodgram - Продуктовый помощник.
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Подготовка и запуск проекта
##### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/Fitoyaz/foodgram-project-react.git
```

Установите docker на сервер:
```
sudo apt install docker.io
```
Установите docker-compose на сервер:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Скопируйте папки docs и infra на сервер в ~/

##Подготовка окружения
Выполните команды
```
python3 -m venv venv # создание окружения
. venv/bin/activate # активация окружения
./manage.py makemigrations && ./manage.py migrate # создание и запуск миграций

```

##Установка переменных окружения
Для работы с базой данных создайте .env в /backend с переменными
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
SECRET_KEY=* # Добавить SECRET_KEY из настроек
```
##Запуск приложения в Docker
```
docker-compose up -d --build  # Запустите docker-compose
sudo docker-compose exec -T backend python manage.py makemigrations  # Создать миграции миграции
sudo docker-compose exec -T backend python manage.py migrate --noinput  # Применить миграции
sudo docker-compose exec -T backend python manage.py createsuperuser  # Создать суперпользователя
sudo docker-compose exec -T backend python manage.py collectstatic --no-input  # Собрать статику
docker-compose exec backend python manage.py load_data # Загрузка ингредиентов
```
Проект будет вам доступен по 
[адресу](http://localhost/recipes)

# Загрузка на боевой сервер
Для полноценной работы загрузите на сервер директорию /docs и /infra
В директории /infra измените файл docker-compose.yml и nginx.conf на конфигурации из директории /site. Создайте файл .env с переменными. Не забудьте изменить server_name на ваш публичный IPv4.
# Выполните команды
```
docker-compose up -d --build  # Запустите docker-compose
sudo docker-compose exec -T backend python manage.py makemigrations  # Создать миграции миграции
sudo docker-compose exec -T backend python manage.py migrate --noinput  # Применить миграции
sudo docker-compose exec -T backend python manage.py createsuperuser  # Создать суперпользователя
sudo docker-compose exec -T backend python manage.py collectstatic --no-input  # Собрать статику
docker-compose exec backend python manage.py load_data # Загрузка ингредиентов
```
>Проект будет доступен по вашему IP.