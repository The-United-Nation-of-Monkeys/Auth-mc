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
          {text}
          <p>Спасибо что выбрали нас!</p>
          <p class="label">С уважением, команда LKS 2.0</p>
          </div>
        </div>
      </div>
    </body>
</html>
"""