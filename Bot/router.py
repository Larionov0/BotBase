from .Keyboards.keyboard import Keyboard, Button


class Router:
    def __init__(self, bot):
        self.bot = bot

    def answer_to_message(self, user, text):
        user.next_message_handler(user, text)

    def start_handler(self, user, text):
        self.bot.send_message(user.chat_id, 'Добро пожаловать в нашего бота! Просим вам зарегистрироваться.\n'
                                        'Введите свой никнейм:')
        user.next_message_handler = self.registration_handler

    def registration_handler(self, user, text):
        username = text.strip()
        if 3 <= len(username) <= 15:
            user.username = username
            self.bot.send_message(user.chat_id, 'Никнейм сохранен!')
            self.main_menu(user)
        else:
            self.bot.send_message(user.chat_id, 'Попробуй еще раз:')

    def main_menu(self, user):  # это просто пример, тебе нужно будет переписать эту функцию
        text = f'-----= Главное меню =----\n{user.username}'
        keyboard = Keyboard([
            [Button('Играть'), Button('Чихнуть')],
            [Button('Магазин'), Button('удалить аккаунт')]
        ])
        self.bot.send_message(user.chat_id, text, keyboard)
        user.next_message_handler = self.main_menu_handler

    def main_menu_handler(self, user, text):
        if text == 'Играть':
            pass
        elif text == 'Чихнуть':
            self.bot.send_message(user.chat_id, 'Апчхи!')
            self.main_menu(user)
        elif text == 'Магазин':
            pass
        elif text == 'удалить аккаунт':
            pass
        else:
            self.bot.send_message(user.chat_id, 'Уважаемый, такой дичи мы не видали')
