import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from keep_alive import keep_alive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.bans = True
intents.dm_messages = True

bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    print('aight')

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    else:
        await msg.delete()
        await msg.author.send(f"you have been banned from {msg.guild.name}. reason: talking")
        await msg.guild.ban(msg.author, reason='talked')
        print(f'{msg.author} banned for talkin..')

    await bot.process_commands(msg)

keep_alive()
bot.run(token)
