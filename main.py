import discord
from discord.ext.commands import Bot
import datetime
import time
from tokenid import *

token = token # discord development kanalinda

client = discord.Client()
bot = Bot(command_prefix=".")

@bot.event
async def on_ready():
        print("bot is running")
        channel = bot.get_channel(development_channel_id)
        timenow = str(datetime.datetime.now())
        while True:
            timenow = str(datetime.datetime.now())
            if timenow[0:19] == "2021-03-07 04:59:30":
                await channel.send("8 MART DÜNYA KADINLAR GÜNÜMÜZ KUTLU OLSUN @everyone")
                break
            else:
                print(datetime.datetime.now())
                # time.sleep(0.1)
            time.sleep(0.01)

        # await channel.send('hello')

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
        await message.channel.send("8 MART DÜNYA KADINLAR GÜNÜMÜZ KUTLU OLSUN @everyone")

bot.run(token)
