# Дипломный проект | Yandex Practicum #
>Проект выполнил Ситнов Руслан Сергеевич

*Ссылка на сайт (В разработке)*

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
SECRET_KEY=*
```
##Запуск приложения в Docker
```
docker-compose up -d --build  # Запустите docker-compose
sudo docker-compose exec -T backend python manage.py makemigrations  # Создать миграции миграции
sudo docker-compose exec -T backend python manage.py migrate --noinput  # Применить миграции
sudo docker-compose exec -T backend python manage.py createsuperuser  # Создать суперпользователя
sudo docker-compose exec -T backend python manage.py collectstatic --no-input  # Собрать статику
```
Проект будет вам доступен по 
[адресу](http://localhost/recipes)

Продолжение следует.. 
