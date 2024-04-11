from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_details
import requests
import io

# Initialize the Pyrogram client with API credentials
app = Client(
    "my_bot",
    api_id=10471716,
    api_hash="f8a1b21a13af154596e2ff5bed164860",
    bot_token="6550995906:AAG4-krS-EohlPgDjkCRS-Fudd802eFAyPk"
)

# Start command handler



# /start command handler
@app.on_message(filters.command("start"))
def start_command(client, message):
    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Our Bots", callback_data="our_bots"),
        ],
        [InlineKeyboardButton("Join Updates Channel", url="https://t.me/botio_devs")],
    ]

    markup = InlineKeyboardMarkup(buttons)

    message.reply_text("☺︎нαι\n✦ Send Me A Terabox Link To Start My work\n\n╭──── ⋅ ⋅ ────── 𝐈𝐍𝐓𝐑𝐎 ────── ⋅ ⋅ ─────╮\n   ✇ I'm Legendary Terabox Utility Bot\n   ✇ 𝙼𝚢 𝙱𝚘𝚜𝚜 𝙸𝚜 𝙳𝚊𝚒𝚕𝚢 𝚄𝚙𝚍𝚊𝚝𝚒𝚗𝚐 𝙼𝚎\n   ✇ 𝙳𝚘𝚗𝚝 𝙵𝚘𝚛𝚐𝚎𝚝 𝚝𝚘 𝙹𝚘𝚒𝚗 𝙼𝚢 [𝙵𝚊𝚖𝚒𝚕𝚢](https://t.me/botio_devs)\n╰────── ⋅ ⋅ ────── ✩ ────── ⋅ ⋅ ──────╯\n\n[𓆩🄰🄳🄼🄸🄽𓆪](https://t.me/Appuz_007)", reply_markup=markup, disable_web_page_preview=True)


@app.on_callback_query()
def handle_callback_query(client, query):
    data = query.data

    if data == "about":
        about_text = "<b>︵‿︵‿︵‿୨ ꪑꫀ ୧‿︵‿︵‿︵\nNᴀᴍᴇ: [Terabox Downloader](https://t.me/TeraboxDownloader_l_Bot)\nAɪᴍ: To Make Your Life Easy\nFᴀᴛʜᴇʀ: [Aᴘᴘᴜs](https://t.me/APPUZ_001)\nDNA:Pʏʀᴏɢʀᴀᴍ ᴠ𝟸\n‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵</b>"
        back_button = InlineKeyboardButton("Back", callback_data="back")
        markup = InlineKeyboardMarkup([[back_button]])
        query.edit_message_text(about_text, reply_markup=markup, parse_mode=None, disable_web_page_preview=True)
    
    elif data == "our_bots":
        bots_text = "<b>═ ══ ═[🄾🅄🅁 🄶🄰🅁🄰🄶🄴](https://t.me/botio_devs)═ ══ ═\n\n[𝚄𝚛𝚕 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚛 𝙱𝚘𝚝](https://t.me/UrlUploaderio_bot)\n\n[𝙰𝚍𝚕𝚒𝚗𝚔𝚜 𝙱𝚢𝚙𝚊𝚜𝚜𝚎𝚛](https://t.me/io_Link_bypasserbot)\n\n[𝟷𝟾+ 𝚂𝚎𝚊𝚛𝚌𝚑 𝙱𝚘𝚝](https://t.me/Adult_pornsearchbot)\n\n[𝙰𝚒 𝙸𝚖𝚊𝚐𝚎 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛](https://t.me/Image_l_GeneratorBot)\n\n[𝙵𝚒𝚕𝚎 𝚂𝚝𝚘𝚛𝚎 𝙱𝚘𝚝](https://t.me/FileStore_l_Bot)\n\n[𝚃𝚎𝚛𝚊𝚋𝚘𝚡 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚛](https://t.me/TeraboxDownloader_l_Bot)\n\n\n\"Cᴏᴅᴇ ᴡɪᴛʜ ᴀ ʀᴇʙᴇʟ sᴘɪʀɪᴛ, ᴅᴇʙᴜɢ ᴡɪᴛʜ ᴀ ᴡᴀʀʀɪᴏʀ's ᴘᴀᴛɪᴇɴᴄᴇ, ᴀɴᴅ ᴄᴏɴǫᴜᴇʀ ᴄʜᴀʟʟᴇɴɢᴇs ʟɪᴋᴇ ᴀ ᴛʀᴜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴄʜᴀᴍᴘɪᴏɴ. 💻⚔️ #DᴇᴠAᴛᴛɪᴛᴜᴅᴇ\"\n\n\nѕнαяє αи∂ ѕυρρσят υѕ</b>"
        back_button = InlineKeyboardButton("Back", callback_data="back")
        markup = InlineKeyboardMarkup([[back_button]])
        query.edit_message_text(bots_text, reply_markup=markup, parse_mode=None, disable_web_page_preview=True)
    
    elif data == "back":
        # Show the initial welcome message with buttons
        buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Our Bots", callback_data="our_bots"),
        ],
        [InlineKeyboardButton("Join Updates Channel", url="https://t.me/botio_devs")],
        ]
        markup = InlineKeyboardMarkup(buttons)
        query.edit_message_text("☺︎нαι\n✦ Send Me A Terabox Link To Start My work\n\n╭──── ⋅ ⋅ ────── 𝐈𝐍𝐓𝐑𝐎 ────── ⋅ ⋅ ─────╮\n   ✇ I'm Legendary Terabox Utility Bot\n   ✇ 𝙼𝚢 𝙱𝚘𝚜𝚜 𝙸𝚜 𝙳𝚊𝚒𝚕𝚢 𝚄𝚙𝚍𝚊𝚝𝚒𝚗𝚐 𝙼𝚎\n   ✇ 𝙳𝚘𝚗𝚝 𝙵𝚘𝚛𝚐𝚎𝚝 𝚝𝚘 𝙹𝚘𝚒𝚗 𝙼𝚢 [𝙵𝚊𝚖𝚒𝚕𝚢](https://t.me/botio_devs)\n╰────── ⋅ ⋅ ────── ✩ ────── ⋅ ⋅ ──────╯\n\n[𓆩🄰🄳🄼🄸🄽𓆪](https://t.me/Appuz_007)", reply_markup=markup, disable_web_page_preview=True)




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
                status_message = await message.reply_text("Sending Files Please Wait.!!......✨", reply_to_message_id=message.id)
                await send_file(details["direct_link"], message, status_message)
            except Exception as e:
                print(e)  # Log the error for debugging
                await message.reply_text("Something went wrong 🙃😒\n**contact admin for assistance**", reply_to_message_id=message.id)
        else:
            await message.reply_text("Something went wrong 🙃😒\n**contact admin for assistance**", reply_to_message_id=message.id)
        print(details)
    else:
        await message.reply_text("Please send a valid Terabox link.😕", reply_to_message_id=message.id)






async def send_file(item, message):
    try:
        response = requests.get(item)
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            filename_index = content_disposition.find('filename=')
            if filename_index != -1:
                filename = content_disposition[filename_index + len('filename='):]
                filename = filename.strip('"')  # Remove surrounding quotes, if any
                file_bytes = io.BytesIO(response.content)  # Define file_bytes here
                file_bytes.name = filename
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if content_type:
                if 'video' in content_type:
                    await message.reply_video(video=file_bytes, caption=filename)
                elif 'image' in content_type:
                    await message.reply_photo(photo=file_bytes, caption=filename)
                else:
                    if content_disposition:
                        filename_index = content_disposition.find('filename=')
                        if filename_index != -1:
                            filename = content_disposition[filename_index + len('filename='):]
                            filename = filename.strip('"')  # Remove surrounding quotes, if any
                            file_bytes.name = filename
                            await message.reply_document(document=file_bytes, caption=filename)
                        else:
                            await message.reply_text("Failed to extract filename from content disposition.")
                    else:
                        await message.reply_text("Failed to extract filename from content disposition.")
            else:
                await message.reply_text("Failed to determine the type of the file.")
        else:
            await message.reply_text("Failed to download the file from the provided URL.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
        finally:
        # Delete the status indicating message
        await status_message.delete()
        


# Start the bot
app.run()
