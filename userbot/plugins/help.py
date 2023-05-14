# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

import asyncio

from pyrogram.types import Message
from pyrogram import Client, filters

from ..utils.logger import logger

CMD_HELP = {}

@Client.on_message(filters.command("help", ".") & filters.me)
async def help_command_handler(client: Client, message: Message):
    cmd = message.command
    
    if len(cmd) > 1:
        module_name = " ".join(cmd[1:]).lower()
        await send_help_message(message, module_name)
    elif message.reply_to_message:
        try:
            help_arg = message.reply_to_message.text
            if help_arg in CMD_HELP:
                module_name = (help_arg.split("\n")[0].strip().replace("Інформація о ", "").replace(":", ""))
                await send_help_message(message, module_name) 
            else:
                await send_help_message(message)
        except Exception as e:
            print(f"<emoji id=5210952531676504517>🔴</emoji> Помилка: {e}")
            logger.error(f"help_command_handler: {e}")
    else:
        await send_help_message(message)
    await asyncio.sleep(20)
    await message.delete()


def add_command_help(module_name: str, commands: list) -> None:
    command_dict = CMD_HELP.setdefault(module_name, {})
    
    for command, description in commands:
        command_dict[command] = description


def split_list(input_list: list, n: int) -> list[list]:
    n = max(1, n)
    
    return [input_list[i: i + n] for i in range(0, len(input_list), n)]


async def send_help_message(message: Message, module_name: str = None) -> None:
    if module_name:
        if module_name in CMD_HELP:
            commands = CMD_HELP[module_name]
            module_help = f"<emoji id=5443132326189996902>🍃</emoji> __Інформація про__ **{module_name}**"
            for command, description in commands.items():
                module_help += f"**`{command}`** \n└ __{description}__\n"
            await message.edit_text(module_help)
        else:
            await message.edit_text("`<emoji id=5210952531676504517>🔴</emoji> Будь-ласка, вкажи нормальне імя модуля.`")  
    else:
        all_commands = "**<emoji id=5447410659077661506>🛠️</emoji> __Список модулів__:**\n\n"
        for module_group in split_list(sorted(CMD_HELP.keys()), 2):
            all_commands += ("• " + '\n• '.join(map(str, ["`" + cmd + "`" for cmd in module_group])) + "\n")
        all_commands += "\n<emoji id=5397782960512444700>⚙</emoji> __Щоб получити інформацію по певному модулю, використовуйте:__ `.help [Назва модуля]`"
        await message.edit_text(all_commands)
        
