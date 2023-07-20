# Bake Cake #

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Загрузка тестовых данных
Для загрузки начальных тестовых данных необходимо выполнить команду
```shell
python3 manage.py loaddata demo-data --format JSON
```


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта (обязательно)
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).

## run with Docker
Run Docker container

```shell
sudo docker-compose up
```

This should build the image and start the container. You may see Windows Defender warning about Docker trying to listen on port 8000. After the container has started, open the browser again on http://localhost:8000/, and you should see site