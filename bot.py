from typing import Optional, Literal
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Greedy, Context

from decouple import config

import cmds.others as others


DISCORD_TOKEN = config('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

extensions = [
  'cmds.others',
  'cmds.translate',
  'cmds.currency',
]

@bot.event
async def on_ready():
  print("Loading commands")
  
  for extension in extensions:
    print(f'Loading {extension} ---')
    await bot.load_extension(extension)
    print(f'Loaded {extension} ---')
  
  print(f'We have logged in as {bot.user}')

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

bot.run(DISCORD_TOKEN)
