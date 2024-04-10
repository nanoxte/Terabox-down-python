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
                    
                    await message.reply_video(video=temp_video_path, duration=int(float(duration)), caption=filename, thumb=thumbnail_path, reply_to=message.reply_to_message.message_id)
                elif 'image' in content_type:
                    await message.reply_photo(photo=file_bytes, caption=filename, reply_to=message.reply_to_message.message_id)
                else:
                    if content_disposition:
                        filename_index = content_disposition.find('filename=')
                        if filename_index != -1:
                            filename = content_disposition[filename_index + len('filename='):]
                            filename = filename.strip('"')  # Remove surrounding quotes, if any
                            file_bytes.name = filename
                            await message.reply_document(document=file_bytes, caption=filename, reply_to=message.reply_to_message.message_id)
                        else:
                            await message.reply_text("Failed to extract filename from content disposition.", reply_to=message.reply_to_message.message_id)
                    else:
                        await message.reply_text("Failed to extract filename from content disposition.", reply_to=message.reply_to_message.message_id)
            else:
                await message.reply_text("Failed to determine the type of the file.", reply_to=message.reply_to_message.message_id)
        else:
            await message.reply_text("Failed to download the file from the provided URL. Url didn't connect.", reply_to=message.reply_to_message.message_id)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}\n\n Use this [link]({item}) to download the file\n\nOR, use our [URL UPLOADER BOT](https://t.me/UrlUploaderio_bot")
