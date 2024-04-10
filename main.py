from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_details
import requests
import io
import tempfile
import ffmpeg
from http.client import IncompleteRead


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

import requests
import io
import tempfile
import ffmpeg
from http.client import IncompleteRead

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
                    # Write video file to a temporary file
                    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_video:
                        temp_video.write(response.content)
                        temp_video_path = temp_video.name
                    
                    # Retrieve video duration
                    probe = ffmpeg.probe(temp_video_path)
                    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
                    duration = video_info['duration']
                    
                    # Set a random frame from the video as thumbnail
                    thumbnail_path = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False).name
                    ffmpeg.input(temp_video_path).filter('select', 'gte(n,1)').output(thumbnail_path, vframes=1).run(overwrite_output=True)
                    
                    await message.reply_video(video=temp_video_path, duration=int(float(duration)), caption=filename, thumb=thumbnail_path, reply_to_message_id=message.id)
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
            await message.reply_text("Failed to download the file from the provided URL. Url didn't connect.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}\n\n Use this [link]({item}) to download the file\n\nOR, use our [URL UPLOADER BOT](https://t.me/UrlUploaderio_bot")


# Start the bot
app.run()
