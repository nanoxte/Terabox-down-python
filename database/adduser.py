from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message

async def AddUser(bot: Client, update: Message):
    if not await techvj.is_user_exist(update.from_user.id):
        await techvj.add_user(update.from_user.id)
