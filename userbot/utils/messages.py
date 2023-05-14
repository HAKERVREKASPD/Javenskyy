# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import colorama
from colorama import Fore, Style

colorama.init()

Version = "version 1.0"

Logo_Message = f"{Fore.BLUE}{Style.BRIGHT} D A R K N E T \n" \
               f" J|A|V|E|L|I|N \n" \
               f"{Fore.YELLOW}{Style.BRIGHT} . . . Telegram . . . \n" \
               f" < https://t.me/darksecretsoft > \n" \
               f" За питаннями: https://t.me/kamonbabyy \n" \
               f"                    {Fore.RED}{Style.BRIGHT}{Version}{Fore.BLUE}{Style.BRIGHT}\n\n" \

starting_userbot = f"{Fore.GREEN}{Style.BRIGHT}$ Запуск юзерботу..."
connecting_userbot = f"{Fore.GREEN}{Style.BRIGHT}$ Підключення..."
sending_code = f"{Fore.GREEN}{Style.BRIGHT}$ Відправка коду..."
code_sended = f"{Fore.GREEN}{Style.BRIGHT}$ Код відправлений!"
signin_userbot = f"{Fore.GREEN}{Style.BRIGHT}$ Вхід в аккаунт..."
successfully = f"{Fore.GREEN}{Style.BRIGHT}$ Успішно!"

Phone = f"{Fore.GREEN}{Style.BRIGHT}>>> Авторизація:\n{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введіть свій номер телефону(без +):{Fore.WHITE}{Style.RESET_ALL} "

Closed = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Ви вишли з юзербота."

BadRequest = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Помилка вводу{Fore.WHITE}{Style.RESET_ALL}"

FloodWait = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} У вас флуд на авторизацію, почекайте "

PhoneCodeInvalid = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Помилка: Не правильно введений код"

PasswordHashInvalid = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Помилка: Не правильний пароль"

Error = f"{Fore.GREEN}{Style.BRIGHT}>>{Fore.RED} Помилка: {Fore.YELLOW}"

Code = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введіть код з телеграму:{Fore.WHITE}{Style.RESET_ALL} "

Password = f"{Fore.GREEN}{Style.BRIGHT}${Fore.WHITE} Введіть код з двухтапної аутентифікації:{Fore.WHITE}{Style.RESET_ALL} "

Runned = f"{Fore.GREEN}{Style.BRIGHT}$ Скрипт запущений! Напишіть {Fore.BLUE}{Style.BRIGHT}.help{Fore.GREEN}{Style.BRIGHT}(в чат телеграму) щоб подивитись доступні модулі"
