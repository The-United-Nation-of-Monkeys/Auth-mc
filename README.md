Инструкция по запуску:

1) склонировать репразиторий
2) перейти в папку с проектом
3) запустить docker-compose.yml(если будет выдавать ошибку попробуйте изменить название в networks а затем в каждом сервисе
   в разделе servises замените название сети на указанное вами в разеделе network для каждого сервиса)
5) готово
   
Так же так как это админ панель необходимо авторизоваться, пароль: test, имя: test
Проверить работу можно по адресу 127.0.0.1:8000/docs

при необходимости запустить приложение без контейнеризации 
1) открыть файл docekr-compose.yml и удалить от туда сервис app
2) создать окуржение
3) установить зависимости из файла req.txt(pip install -r req.txt)
4) запустить docker-compose.yml
5) запустить файл /docekr/start.py
6) запустить uvicorn src.main:app --reload или просто запустить файл main.py
