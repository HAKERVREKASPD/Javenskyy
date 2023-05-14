# ©️ Spribe Userbot, 2023
# This file is a part of Spribe Userbot
# >> https://github.com/Pr0n1xGH/spribe-userbot
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# >> https://www.gnu.org/licenses/agpl-3.0.html

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from .help import add_command_help


@Client.on_message(filters.command("gifspam", ".") & filters.me)
async def gifspam(client, message):
    gif = " ".join(message.command[2:])

    try:
        if not gif:
            await message.delete()
            for _ in range(int(message.command[1])):
                await sleep(0.01)
                await client.send_document(message.chat.id,
                                           "https://tenor.com/view/spam-toon-toonio-%D1%82%D1%83%D0%BD%D0%B8%D0%BE-pomidorkin-gif-24712213")
        else:
            await message.delete()
            for _ in range(int(message.command[1])):
                await sleep(0.01)
                await client.send_document(message.chat.id, gif)
    except Exception as e:
        await message.edit("🔴 ▸ Використування: `.gifspam` [Кількість] [Посилання на гфі] (Посилання на гіф можна не вводити)")
        await sleep(5)
        await message.delete()


@Client.on_message(filters.command("spam", ".") & filters.me)
async def spam(client, message):
    spam_message = " ".join(message.command[2:])

    if not spam_message:
        await message.edit(f'🔴 ▸ Використування: `.spam` [Кількість] [повідомлення]')
        await sleep(5)
        await message.delete()
    else:
        await message.delete()
        for _ in range(int(message.command[1])):
            await client.send_message(message.chat.id, spam_message)


@Client.on_message(filters.command('spamstick', '.') & filters.me)
async def spamstick(client, message):
    try:
        stick_id = str(message.text.split()[2])
        if not stick_id:
            await message.edit("🔴 ▸ Використування: `.spamstick` [Кількість] [Id стикеру]")
            await sleep(5)
            await message.delete()
        else:
            await message.delete()
            for _ in range(int(message.command[1])):
                await client.send_sticker(message.chat.id, stick_id)

    except Exception as e:
        await message.edit("🔴 ▸ Використування: `.spamstick` [Кількість] [Id стикеру]")
        await sleep(5)
        await message.delete()


@Client.on_message(filters.command("ghoul", prefixes=".") & filters.me)
async def ghoul(client, message):
    await client.send_message(message.chat.id, f'<b>1</b>')
    await sleep(2)
    await client.send_message(message.chat.id, f'<b>2</b>')
    await sleep(2)
    await client.send_message(message.chat.id, f'<i>3</i>')
    await sleep(3)
    i = 1000
    while i > 0:
        try:
            await client.send_message(message.chat.id, f'{i} - 7 = {i - 7}')
        except FloodWait as e:
            await sleep(e.x)

        i -= 7
        await sleep(0)

add_command_help(
    "spam",
    [
        [".spam [Кількість] [Повідомлення]", "Спам повідомлень"],
        [".gifspam [Кількість] [Посилання на gif]", "Спам гіфками (Посилання на гіфку брати на сайті tenor.com)"],
        [".spamstick [Кількість] [id Стикеру]", "Спам стікерами (Id стікера можно взяти тут @idstickerbot)"],
        [".ghoul", "Спам 1000-7"],
    ],
)
