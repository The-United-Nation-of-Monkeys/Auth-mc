register_form = """
<html>
  <head>
    <style>
      body {{
        font-family: Arial, sans-serif;
        padding: 20px;
      }}
      .wrapper {{
        display: flex;
        justify-content: center;
      }}
      .labelWrapper {{
        margin-top: 40px;
        margin-left: 200px;
      }}
      .label {{
        font-size: 14px;
        color: '#ccc';
      }}
    </style>
  </head>
    <body>
      <div class="wrapper">
        <div>
            <h1>Здравствуйте, {name}!</h1>
          <p>Для подтверждения перейдите по <a href="{link}">этой ссылке.</a></p>
          <p>Если это были не вы, для отмены перейдите по <a href="{delete_link}">этой ссылке.</a></p>
            <p>Спасибо что выбрали нас!</p>
          <div class="labelWrapper">
          <p class="label">С уважением, команда LKS 2.0</p>
          </div>
        </div>
      </div>
    </body>
</html>
"""

special_register_form = """
<html>
  <head>
    <style>
      body {{
        font-family: Arial, sans-serif;
        padding: 20px;
      }}
      .wrapper {{
        display: flex;
        justify-content: center;
      }}
      .labelWrapper {{
        margin-top: 40px;
        margin-left: 200px;
      }}
      .label {{
        font-size: 14px;
        color: '#ccc';
      }}
    </style>
  </head>
    <body>
      <div class="wrapper">
        <div>
            <h1>Здравствуйте, {name}!</h1>
          <p>Роль котороую вы выбрали при регистрации необходимо дополнительно подтвердить.</p>
          <p>С вами скоро свяжутся наши администраторы.</p>
          <p>Если это были не вы, для отмены перейдите по <a href="{delete_link}">этой ссылке.</a></p>
            <p>Спасибо что выбрали нас!</p>
          <div class="labelWrapper">
          <p class="label">С уважением, команда LKS 2.0</p>
          </div>
        </div>
      </div>
    </body>
</html>
"""

switch_password_form = """
<html>
    <body>
        <h1>Здравствуйте!</h1>
        <p>С вашего аккаунта поступил запрос на смену пароля, если вы не отправляли его, игнорируйте это письмо.</p>
        <p>Ваш код для смены пароля: <span style="font-weight: 800;font-size: 24px;">{code}</span></p>
        <p>Спасибо что выбрали нас!</p>
    </body>
</html>
"""

base_form = """
<html>
  <head>
    <style>
      body {{
        font-family: Arial, sans-serif;
        padding: 20px;
      }}
      .wrapper {{
        display: flex;
        justify-content: center;
      }}
      .labelWrapper {{
        margin-top: 40px;
        margin-left: 200px;
      }}
      .label {{
        font-size: 14px;
        color: '#ccc';
      }}
    </style>
  </head>
    <body>
      <div class="wrapper">
        <div>
            <h1>Здравствуйте, {name}!</h1>
          <p>Роль котороую вы выбрали при регистрации необходимо дополнительно подтвердить.</p>
          <p>С вами скоро свяжутся наши администраторы.</p>
          <p>Если это были не вы, для отмены перейдите по <a href="{delete_link}">этой ссылке.</a></p>
            <p>Спасибо что выбрали нас!</p>
          <div class="labelWrapper">
          <p class="label">С уважением, команда LKS 2.0</p>
          </div>
        </div>
      </div>
    </body>
</html>
"""