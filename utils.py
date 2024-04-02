async def send_file(item, message):
    if item:
        try:
            await message.reply_document(document=item)
        except Exception as e:
            await message.reply_text(
                f"⚠️ {str(e)}\n\n👉 Try manually downloading from [here]({item})\n\n👉 *Maybe This File Is Too Large Or Cannot Accessible From Terabox*",
                parse_mode="markdown"
            )
