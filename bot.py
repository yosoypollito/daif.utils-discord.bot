import os
import discord
from discord import app_commands

class Bot(discord.Client):
  async def on_ready(self):
    await tree.sync()
    print(f'Logged on as {self.user}!')
  
  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')
    

intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents)
tree = app_commands.CommandTree(client)

client.run("token")