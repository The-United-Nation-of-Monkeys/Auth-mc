active_account_form = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Спасибо!</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }}
        .message {{
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="message">
        <h1>Спасибо за использование нашего сервиса!</h1>
        <p>Ваша запись успешно {status_}</p>
        <p>Всего хорошего :^</p>
    </div>
</body>
</html>
"""

error_active_form = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Спасибо!</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        .message {
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="message">
        <h1>Спасибо за использование нашего сервиса!</h1>
        <p>Ваша запись уже активирована.</p>
        <p>Чтобы её удалить используйте приложение.</p>
        <p>Всего хорошего :^</p>
    </div>
</body>
</html>

"""
