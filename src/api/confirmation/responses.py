from fastapi.responses import HTMLResponse

from src.api.confirmation.forms import base_form

class HtmlResponseStatus:
    
    def account_info(status):
        content_text = f"""
        <p>Ваша запись успешно {status}</p>
        """
        content = base_form.format(text=content_text)
        return HTMLResponse(content)
    
    def error_active():
        content_text = """
        <p>Ваша запись уже активирована.</p>
        <p>Чтобы её удалить используйте приложение.</p>
        """
        content = base_form.format(text=content_text)
        return HTMLResponse(content)