from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

api_id = int(os.getenv("37162900"))
api_hash = os.getenv("48dce9bfef7fbe85bdaab1d3e32c7960")
bot_token = os.getenv("8675956809:AAGxNFWqSXVFOkmAFzXB-7lQ03tiXlOqchg")
session_string = os.getenv("BQI3D5QAfeT5D9wgl8fYN65ImrGg2lSDbZuLUSYVz5FboieMAdDklolcpXHo9I9HFUP9CuKXhsUxsVRq1DxXIlyqJhm4s0NO9c8z3zBXX6c6_e9t1qjsbRXulgNRbgAjR8byjTuZrEgd1m3oksmezYrWMCYe9bCpinGewD968DtcpAvBI2S31A5wUxGCKoLgdhjoyH7OoUfprvhdEJa2Vwb75CUnAswz05vfQ8BeiLeps2qArjRznYRNAKitAp1OnZ2jKnOspAVkQFS3LBAX6sX8aDi88buNtzBMtw3dORaQkz1UVeW6vYaU6sAk_NaV8RYLQYWhaVHAFdtvGIr_M8ryOYqCywAAAAGi-WA2AA")

app = Client(
    "API_ID=37162900
API_HASH=48dce9bfef7fbe85bdaab3e32c7960
BOT_TOKEN=8675956809:AAGxNFWqSXVFOkmAFzXB-7lQ03tiXlOqchg
SESSION_STRING=BQI3D5QAfeT5D9wgl8fYN65ImrGg2lSDbZuLUSYVz5FboieMAdDklolcpXHo9I9HFUP9CuKXhsUxsVRq1DxXIlyqJhm4s0NO9c8z3zBXX6c6_e9t1qjsbRXulgNRbgAjR8byjTuZrEgd1m3oksmezYrWMCYe9bCpinGewD968DtcpAvBI2S31A5wUxGCKoLgdhjoyH7OoUfprvhdEJa2Vwb75CUnAswz05vfQ8BeiLeps2qArjRznYRNAKitAp1OnZ2jKnOspAVkQFS3LBAX6sX8aDi88buNtzBMtw3dORaQkz1UVeW6vYaU6sAk_NaV8RYLQYWhaVHAFdtvGIr_M8ryOYqCywAAAAGi-WA2AA",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    session_string=session_string
)

# Basic command to test bot
@app.on_message(filters.command("start") & filters.private)
def start(client: Client, message: Message):
    message.reply_text("✅ Music Bot is running!")

app.run()
