import typing

from discord import app_commands, Interaction
from discord.ext import commands

from discord.app_commands import Choice

import services

lang_codes_autocomplete = {       
"af":"Afrikaans",
"sq":"Albanian",
"am":"Amharic",
"ar":"Arabic",
"hy":"Armenian",
"as":"Assamese",
"az":"Azerbaijani (Latin)",
"bn":"Bangla",
"ba":"Bashkir",
"eu":"Basque",
"bs":"Bosnian (Latin)",
"bg":"Bulgarian",
"yue":"Cantonese (Traditional)",
"ca":"Catalan",
"lzh":"Chinese (Literary)",
"zh-Hans":"Chinese Simplified",
"zh-Hant":"Chinese Traditional",
"hr":"Croatian",
"cs":"Czech",
"da":"Danish",
"prs":"Dari",
"dv":"Divehi",
"nl":"Dutch",
"en":"English",
"et":"Estonian",
"fo":"Faroese",
"fj":"Fijian",
"fil":"Filipino",
"fi":"Finnish",
"fr":"French",
"fr-ca":"French (Canada)",
"gl":"Galician",
"ka":"Georgian",
"de":"German",
"el":"Greek",
"gu":"Gujarati",
"ht":"Haitian Creole",
"he":"Hebrew",
"hi":"Hindi",
"mww":"Hmong Daw (Latin)",
"hu":"Hungarian",
"is":"Icelandic",
"id":"Indonesian",
"ikt":"Inuinnaqtun",
"iu":"Inuktitut",
"iu-Latn":"Inuktitut (Latin)",
"ga":"Irish",
"it":"Italian",
"ja":"Japanese",
"kn":"Kannada",
"kk":"Kazakh",
"km":"Khmer",
"tlh-Latn":"Klingon",
"tlh-Piqd":"Klingon (plqaD)",
"ko":"Korean",
"ku":"Kurdish (Central)",
"kmr":"Kurdish (Northern)",
"ky":"Kyrgyz (Cyrillic)",
"lo":"Lao",
"lv":"Latvian",
"lt":"Lithuanian",
"mk":"Macedonian",
"mg":"Malagasy",
"ms":"Malay (Latin)",
"ml":"Malayalam",
"mt":"Maltese",
"mi":"Maori",
"mr":"Marathi",
"mn-Cyrl":"Mongolian (Cyrillic)",
"mn-Mong":"Mongolian (Traditional)",
"my":"Myanmar",
"ne":"Nepali",
"nb":"Norwegian",
"or":"Odia",
"ps":"Pashto",
"fa":"Persian",
"pl":"Polish",
"pt":"Portuguese (Brazil)",
"pt-pt":"Portuguese (Portugal)",
"pa":"Punjabi",
"otq":"Queretaro Otomi",
"ro":"Romanian",
"ru":"Russian",
"sm":"Samoan (Latin)",
"sr-Cyrl":"Serbian (Cyrillic)",
"sr-Latn":"Serbian (Latin)",
"sk":"Slovak",
"sl":"Slovenian",
"so":"Somali (Arabic)",
"es":"Spanish",
"sw":"Swahili (Latin)",
"sv":"Swedish",
"ty":"Tahitian",
"ta":"Tamil",
"tt":"Tatar (Latin)",
"te":"Telugu",
"th":"Thai",
"bo":"Tibetan",
"ti":"Tigrinya",
"to":"Tongan",
"tr":"Turkish",
"tk":"Turkmen (Latin)",
"uk":"Ukrainian",
"hsb":"Upper Sorbian",
"ur":"Urdu",
"ug":"Uyghur (Arabic)",
"uz":"Uzbek (Latin",
"vi":"Vietnamese",
"cy":"Welsh",
"yua":"Yucatec Maya",
"zu":"Zulu"
}

def get_lang_code_autocomplete(current):
    data = []
    for key, value in lang_codes_autocomplete.items():
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
        
        lang_value = lang_codes_autocomplete[lang]
        to_value = lang_codes_autocomplete[to]
        
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