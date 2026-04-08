import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from dotenv import load_dotenv
import yt_dlp

load_dotenv()

api_id = int(os.getenv("37162900"))
api_hash = os.getenv("48dce9bfef7fbe85bdaab1d3e32c7960")
bot_token = os.getenv("8675956809:AAGxNFWqSXVFOkmAFzXB-7lQ03tiXlOqchg")
session_string = os.getenv("BQI3D5QAfeT5D9wgl8fYN65ImrGg2lSDbZuLUSYVz5FboieMAdDklolcpXHo9I9HFUP9CuKXhsUxsVRq1DxXIlyqJhm4s0NO9c8z3zBXX6c6_e9t1qjsbRXulgNRbgAjR8byjTuZrEgd1m3oksmezYrWMCYe9bCpinGewD968DtcpAvBI2S31A5wUxGCKoLgdhjoyH7OoUfprvhdEJa2Vwb75CUnAswz05vfQ8BeiLeps2qArjRznYRNAKitAp1OnZ2jKnOspAVkQFS3LBAX6sX8aDi88buNtzBMtw3dORaQkz1UVeW6vYaU6sAk_NaV8RYLQYWhaVHAFdtvGIr_M8ryOYqCywAAAAGi-WA2AA")

app = Client("တေးသံသာ", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
user = Client("@Music_is_important_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)

call_py = PyTgCalls(user)

# Download audio from YouTube
def download_audio(url):
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "song.%(ext)s",
        "quiet": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# /play command
@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /play <youtube link>")

    url = message.command[1]
    file = download_audio(url)

    await call_py.join_group_call(
        message.chat.id,
        AudioPiped(file)
    )

    await message.reply("▶️ Playing music...")

# /pause
@app.on_message(filters.command("pause") & filters.group)
async def pause(_, message):
    await call_py.pause_stream(message.chat.id)
    await message.reply("⏸ Paused")

# /resume
@app.on_message(filters.command("resume") & filters.group)
async def resume(_, message):
    await call_py.resume_stream(message.chat.id)
    await message.reply("▶️ Resumed")

# /stop
@app.on_message(filters.command("stop") & filters.group)
async def stop(_, message):
    await call_py.leave_group_call(message.chat.id)
    await message.reply("⏹ Stopped")

app.start()
user.start()
call_py.start()
print("✅ Music Bot Running...")
app.idle()
