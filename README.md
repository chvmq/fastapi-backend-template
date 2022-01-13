### Структура

+ Python 3.8
+ Django 3.2
+ Nginx (проксирующий сервер)
+ PostgreSQL
+ Redis (кэш и брокер для celery)
+ Сelery (отложенные и регулярные задачи)


### Запуск

```
$ docker-compose up --build
```

### Features

+ Users table
+ Alembic migration tool


### Системные требования

+ docker-compose 1.26.0
+ docker 20.10.9
