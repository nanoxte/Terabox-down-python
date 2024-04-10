import requests
import io

async def send_file(item, message):
    try:
        response = requests.get(item)
        if response.status_code == 200:
            file_bytes = io.BytesIO(response.content)
            await message.reply_document(document=file_bytes)
        else:
            await message.reply_text("Failed to download the file from the provided URL.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
