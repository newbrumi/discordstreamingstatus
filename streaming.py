import discord
import json
from discord.ext import commands
print("made by rumi")

settings = json.load(open("config.json", "r"))
token = settings["token"]
status = settings["status"]
link = settings["link"]



bot = commands.Bot(command_prefix=".", description='fuck you')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=status, url=link))
    print("status on")

bot.run(token, bot=False)
open = input("") 
