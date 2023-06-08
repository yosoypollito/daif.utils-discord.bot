from discord import app_commands, Interaction
from discord.ext import commands

import services

print("loading translate commands")

class Translate(commands.Cog):
    @app_commands.command(name="translate", description="Translate text using Microsoft Translation!")
    @app_commands.describe(lang="The language you want to translate from. \n Ej: es, en, jp")
    @app_commands.rename(lang="from")
    @app_commands.describe(to="The language you want to translate to. \n Ej: es, en, jp")
    @app_commands.rename(to="to")
    @app_commands.describe(text="The text you want to translate")
    @app_commands.rename(text="text")
    async def translate(self, interaction: Interaction, lang: str, to:str, text:str):
        translatedText = await services.translate(lang, to, text) 
        await interaction.response.send_message(f"{translatedText}")
        
async def setup(bot):
    await bot.add_cog(Translate(bot))