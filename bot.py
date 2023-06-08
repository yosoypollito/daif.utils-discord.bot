import discord
from discord import app_commands
from discord.ext import commands

from decouple import config

import cmds.others as others


DISCORD_TOKEN = config('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
  print("Loading commands")
  await bot.load_extension('cmds.others')
  
  print("Syncing commands");
  await bot.tree.sync()
  print(f'We have logged in as {bot.user}')

bot.run(DISCORD_TOKEN)