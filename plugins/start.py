from pyrogram import Client , filters 
@Client.on_message(filters.command("start") & filters.incoming & ~filters.edited)
async def alive(client, message):
    await message.reply(f" hey 👋 💞 Welcome Kindly Note \n Bot maybe a bit slow due to over load 🙁🙁..! please Don't spam..!")