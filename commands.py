import discord
from discord import app_commands


from bot import tree

print("Loading commands...")

@tree.command(name="ping", description="Ping!")
async def pong(interaction: discord.Interaction):
        print(interaction.user.mention)
        await interaction.response.send_message(f"{interaction.user.mention}, pong !")

@tree.command(name="melenas", description="Who is the MELENAS?")
async def melenas(interaction: discord.Interaction):
        await interaction.response.send_message(f"<@621975714287321094>, MELENAS !")

@tree.command(name="sudaka", description="Who is the SUDAKA?")
async def sudaka(interaction: discord.Interaction):
        await interaction.response.send_message(
            f"<@632153965835976704> y <@317876695652630536>, SUDAKAS!"
        )

@tree.command(name="putero", description="Who is the PUTERO?")
async def putero(interaction: discord.Interaction):
        await interaction.response.send_message(f"<@621964049789222951>, putero!")
