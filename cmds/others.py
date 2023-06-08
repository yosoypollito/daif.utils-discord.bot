import discord
from discord import app_commands
from discord.ext import commands

print("Loading Others Commands")

class Others(commands.Cog):
        @app_commands.command(name="ping", description="Ping!")
        async def ping(self, interaction: discord.Interaction):
                print(interaction.user.mention)
                await interaction.response.send_message(f"{interaction.user.mention}, pong !")

        @app_commands.command(name="melenas", description="Who is the MELENAS?")
        async def melenas(self, interaction: discord.Interaction):
                await interaction.response.send_message(f"<@621975714287321094>, MELENAS !")

        @app_commands.command(name="sudaka", description="Who is the SUDAKA?")
        async def sudaka(self, interaction: discord.Interaction):
                await interaction.response.send_message(
            f"<@632153965835976704> y <@317876695652630536>, SUDAKAS!"
        )

        @app_commands.command(name="putero", description="Who is the PUTERO?")
        async def putero(self, interaction: discord.Interaction):
                await interaction.response.send_message(f"<@621964049789222951>, putero!")
                
async def setup(bot):
    await bot.add_cog(Others(bot))