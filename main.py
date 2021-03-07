import discord
from discord.ext.commands import Bot
import datetime
import time
from tokenid import *

# token = token # discord development kanalinda
# token ve kanal idleri icin tokenid.py dosyasini import edin

client = discord.Client()
bot = Bot(command_prefix=".")

@bot.event
async def on_ready():
        print("bot is running")
        channel = bot.get_channel(general_id)
        timenow = str(datetime.datetime.now())
        while True:
            timenow = str(datetime.datetime.now())
            if timenow[0:19] == "2021-03-08 00:00:01":
                await channel.send("8 MART DÜNYA KADINLAR GÜNÜ KUTLU OLSUN @everyone")
                break
            else:
                print(datetime.datetime.now())
            time.sleep(0.01)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!komutlar":
        await message.channel.send("not yet bro :(")
    if message.content == "sa":
        await message.channel.send("ase bro")
    if message.content == "!deneme":
        await message.channel.send("aynen deneme @here")
    if message.content == "!8-mart":
        await message.channel.send("8 MART DÜNYA KADINLAR GÜNÜ KUTLU OLSUN @everyone")

bot.run(token)
