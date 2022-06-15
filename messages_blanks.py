def main_info(client_name, client_phone_number, telegram_username, message_from_app):
    return f"""
Имя: {client_name}
            
Контактный номер: {client_phone_number}
            
Имя пользователя телеграмм(при наличии): {telegram_username}
            
Текстовое сообщение: {message_from_app}
            
Прикреплённые файлы:
"""