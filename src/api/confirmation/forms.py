active_account_form = """
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
        <p>Ваша запись успешно активирована</p>
        <p>Всего хорошего :^</p>
    </div>
</body>
</html>
"""


html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Форма ввода пароля</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
        }
        .form-container {
            max-width: 300px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="password"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
    <script>
        async function submitForm(event) {
            event.preventDefault(); // Предотвращаем стандартное поведение формы

            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            const response = await fetch({link}, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    password: password,
                    confirmPassword: confirmPassword
                }),
            });

            if (response.ok) {
                alert('Пароли успешно отправлены!');
            } else {
                alert('Ошибка при отправке паролей.');
            }
        }
    </script>
</head>
<body>

<div class="form-container">
    <h2>Введите пароль</h2>
    <form onsubmit="submitForm(event)">
        <div class="form-group">
            <label for="password">Пароль:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div class="form-group">
            <label for="confirm-password">Повторите пароль:</label>
            <input type="password" id="confirm-password" name="confirm-password" required>
        </div>
        <input type="submit" value="Отправить">
    </form>
</div>

</body>
</html>
"""