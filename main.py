from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_details
import requests
import io
from translation import Translation
import os
import tempfile
import moviepy.editor as mp
from database.adduser import AddUser
from config import Config
from pyrogram import Client as Tech_VJ
from utils import verify_user, check_token, check_verification, get_token

# Initialize the Pyrogram client with API credentials
app = Client(
    "my_bot",
    api_id=10471716,
    api_hash="f8a1b21a13af154596e2ff5bed164860",
    bot_token="6999401413:AAHgF1ZpUsCT5MgWX1Wky7GbegyeHvzi2AU"
)

# Start command handler



@app.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if Config.TECH_VJ_UPDATES_CHANNEL is not None:
        back = await handle_force_sub(bot, update)
        if back == 400:
            return
    if len(update.command) != 2:
      
    # logger.info(update)
        await AddUser(bot, update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            reply_to_message_id=update.id
        )
        return
    data = update.command[1]

    if data.split("-", 1)[0] == "verify":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(update.from_user.id) != str(userid):
            return await update.reply_text(
                text="<b>ᴇxᴘɪʀᴇᴅ ʟɪɴᴋ ᴏʀ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )
        is_valid = await check_token(bot, userid, token)
        if is_valid == True:
            await update.reply_text(
                text=f"<b>ʜᴇʟʟᴏ {update.from_user.mention} 👋,\nʏᴏᴜ ᴀʀᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴠᴇʀɪғɪᴇᴅ !\n\nɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ ᴀʟʟ ᴜʀʟ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛɪʟʟ ᴛᴏᴅᴀʏ ᴍɪᴅɴɪɢʜᴛ.</b>",
                protect_content=True
            )
            await verify_user(bot, userid, token)
        else:
            return await update.reply_text(
                text="<b>ᴇxᴘɪʀᴇᴅ ʟɪɴᴋ ᴏʀ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )


# Message handler
@app.on_message(filters.text)
async def echo(bot, update):
    if not await check_verification(bot, update.from_user.id) and Config.TECH_VJ == True:
        btn = [[
            InlineKeyboardButton("👨‍💻 ᴠᴇʀɪғʏ", url=await get_token(bot, update.from_user.id, f"https://telegram.me/{Config.TECH_VJ_BOT_USERNAME}?start="))
            ],[
            InlineKeyboardButton("🔻 ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ ᴀɴᴅ ᴠᴇʀɪғʏ 🔺", url=f"{Config.TECH_VJ_TUTORIAL}")
        ]]
        await update.reply_text(
            text="<b>ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ ᴏɴ ʙᴏᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴠᴇʀɪғʏ ғɪʀsᴛ\nᴋɪɴᴅʟʏ ᴠᴇʀɪғʏ ғɪʀsᴛ\n\nɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴠᴇʀɪғʏ ᴛʜᴇɴ ᴛᴀᴘ ᴏɴ ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ sᴇᴇ 60 sᴇᴄᴏɴᴅ ᴠɪᴅᴇᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ ʙᴜᴛᴛᴏɴ ᴀɴᴅ ᴠᴇʀɪғʏ</b>",
            protect_content=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return
        await AddUser(bot, update)

# Correct indentation for handle_message function
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

async def send_file(item, message, status_message):
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
                    # Get video duration
                    video_duration = get_video_duration(file_bytes)

                    # Generate thumbnail
                    thumbnail_path = generate_thumbnail(file_bytes)

                    await message.reply_video(video=file_bytes, duration=video_duration, thumb=thumbnail_path, caption=filename, reply_to_message_id=message.id)
                elif 'image' in content_type:
                    await message.reply_photo(photo=file_bytes, caption=filename, reply_to_message_id=message.id)
                else:
                    if content_disposition:
                        filename_index = content_disposition.find('filename=')
                        if filename_index != -1:
                            filename = content_disposition[filename_index + len('filename='):]
                            filename = filename.strip('"')  # Remove surrounding quotes, if any
                            file_bytes.name = filename
                            await message.reply_document(document=file_bytes, caption=filename, reply_to_message_id=message.id)
                        else:
                            await message.reply_text("Failed to extract filename from content disposition.\n\n **Use this [link]({item})** to download the file\n\n**OR**, use our **[URL UPLOADER BOT](https://t.me/UrlUploaderio_bot)**", reply_to_message_id=message.id)
                    else:
                        await message.reply_text("Failed to extract filename from content disposition.\n\n **Use this [link]({item})** to download the file\n\n**OR**, use our **[URL UPLOADER BOT](https://t.me/UrlUploaderio_bot)**", reply_to_message_id=message.id)
            else:
                await message.reply_text("Failed to determine the type of the file.\n\n **Use this [link]({item})** to download the file\n\n**OR**, use our **[URL UPLOADER BOT](https://t.me/UrlUploaderio_bot)**", reply_to_message_id=message.id)
        else:
            await message.reply_text("Failed to download the file from the provided URL.\n\n **Use this [link]({item})** to download the file\n\n**OR**, use our **[URL UPLOADER BOT](https://t.me/UrlUploaderio_bot)**", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}\n\n **Use this [link]({item})** to download the file\n\n**OR**, use our **[URL UPLOADER BOT](https://t.me/UrlUploaderio_bot)**", reply_to_message_id=message.id)
    finally:
        # Delete the status indicating message
        await status_message.delete()

def get_video_duration(file_bytes):
    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
        temp_file.write(file_bytes.getbuffer())
        temp_file_path = temp_file.name
    video = mp.VideoFileClip(temp_file_path)
    duration = int(video.duration)
    os.remove(temp_file_path)  # Remove temporary file
    return duration

def generate_thumbnail(file_bytes):
    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
        temp_file.write(file_bytes.getbuffer())
        temp_file_path = temp_file.name
    video = mp.VideoFileClip(temp_file_path)
    thumbnail_path = f"{temp_file_path}_thumbnail.jpg"
    video.save_frame(thumbnail_path, t=0)  # Save the first frame as the thumbnail
    os.remove(temp_file_path)  # Remove temporary file
    return thumbnail_path
        


# Start the bot
app.run()
