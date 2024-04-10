from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_details
from utils import send_file

# Initialize the Pyrogram client with API credentials
app = Client(
    "my_bot",
    api_id=10471716,
    api_hash="f8a1b21a13af154596e2ff5bed164860",
    bot_token="6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU"
)

# Start command handler
@app.on_message(filters.command(["start"]))
async def start_command(client, message):
    await message.reply_text(
        f"Hi {message.from_user.first_name},\n\nI can Download Files from Terabox.\n\nMade with ❤️ by (.𝖎𝖔𝖉𝖊𝖛𝖘)[https://t.me/botio_devs]\n\nSend any terabox link to download.°°°° \n\n ⚠️spam is ban!!😒",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Channel", url="https://t.me/botio_devs")]])
    )

# Message handler
@app.on_message(filters.text)
async def handle_message(client, message):
    message_text = message.text
    if message_text.startswith('/start'):
        return  # Ignore /start messages here since we're handling them separately
    if "terabox.com" in message_text or "teraboxapp.com" in message_text:
        details = await get_details(message_text)
        if details and details.get("direct_link"):
            try:
                await message.reply_text("Sending Files Please Wait.!!......✨", reply_to_message_id=message.id)
                await send_file(details["direct_link"], message)
            except Exception as e:
                print(e)  # Log the error for debugging
                await message.reply_text("Something went wrong 🙃😒\n**contact admin for assistance**", reply_to_message_id=message.id)
        else:
            await message.reply_text("Something went wrong 🙃😒\n**contact admin for assistance**", reply_to_message_id=message.id)
        print(details)
    else:
        await message.reply_text("Please send a valid Terabox link.😕", reply_to_message_id=message.id)

# Start the bot
app.run()
