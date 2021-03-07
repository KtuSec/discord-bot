import discord
from discord.ext.commands import Bot

token = "" # discord development kanalinda

client = discord.Client()
bot = Bot(command_prefix=".")

@bot.event
async def on_ready():
        print("bot is running")
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "sa":
        await message.channel.send("ase bro")
    if message.content == "!deneme":
        await message.channel.send("aynen deneme @here")
    if message.content == "!8-mart":
        await message.channel.send("8 MART DÜNYA KADINLAR GÜNÜMÜZ KUTLU OLSUN @everyone")

bot.run(token)
