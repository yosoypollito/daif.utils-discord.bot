import typing

from discord import app_commands, Interaction
from discord.ext import commands

import services 

def get_lang_code_autocomplete(current):
    data = []
    for key, value in services.lang_codes.items():
        if key.lower().startswith(current.lower()) or value.lower().startswith(current.lower()):
            data.append(app_commands.Choice(name=value, value=key))
    return data[0:24]


print("loading translate commands")

class Translate(commands.Cog):
    @app_commands.command(name="translate", description="Translate text using Microsoft Translation!")
    @app_commands.describe(text="The text you want to translate", lang="The language you want to translate from", to="The language you want to translate to")
    @app_commands.rename(text="text")
    async def translate(self, interaction: Interaction, lang: str, to:str, text:str):
        translated_json = await services.translate(lang, to, text) 
        
        translated_text = translated_json["translated"]
        time_spend = translated_json["time"]
        
        lang_value = services.lang_codes[lang]
        to_value = services.lang_codes[to]
        
        await interaction.response.send_message(
            f"> {translated_text} \n```Translated from: {lang_value} to: {to_value}\nTime Spent: {time_spend}ms```"
            )
    
    @translate.autocomplete("lang")
    async def translate_autocomplete(self, interaction: Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        return get_lang_code_autocomplete(current)

    @translate.autocomplete("to")
    async def translate_autocomplete(self, interaction: Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        return get_lang_code_autocomplete(current)
        
async def setup(bot):
    await bot.add_cog(Translate(bot))