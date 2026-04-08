from pyrogram import Client
import os

# Secret keys from .env
api_id = int(os.getenv("37162900"))
api_hash = os.getenv("48dce9bfef7fbe85bdaab1d3e32c7960")
bot_token = os.getenv("8675956809:AAGxNFWqSXVFOkmAFzXB-7lQ03tiXlOqchg")

app = Client("@Music_is_important_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
def hello(client, message):
    message.reply_text("✅ Music Bot is running!")

app.run()
