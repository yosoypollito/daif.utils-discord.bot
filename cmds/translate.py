import typing

from discord import app_commands, Interaction
from discord.ext import commands

from discord.app_commands import Choice

import services

lang_codes_autocomplete = {
"Afrikaans":"af",
"Albanian":"sq",
"Amharic":"am",
"Arabic":"ar",
"Armenian":"hy",
"Assamese":"as",
"Azerbaijani (Latin)":"az",
"Bangla":"bn",
"Bashkir":"ba",
"Basque":"eu",
"Bosnian (Latin)":"bs",
"Bulgarian":"bg",
"Cantonese (Traditional)":"yue",
"Catalan":"ca",
"Chinese (Literary)":"lzh",
"Chinese Simplified":"zh-Hans",
"Chinese Traditional":"zh-Hant",
"Croatian":"hr",
"Czech":"cs",
"Danish":"da",
"Dari":"prs",
"Divehi":"dv",
"Dutch":"nl",
"English":"en",
"Estonian":"et",
"Faroese":"fo",
"Fijian":"fj",
"Filipino":"fil",
"Finnish":"fi",
"French":"fr",
"French (Canada)":"fr-ca",
"Galician":"gl",
"Georgian":"ka",
"German":"de",
"Greek":"el",
"Gujarati":"gu",
"Haitian Creole":"ht",
"Hebrew":"he",
"Hindi":"hi",
"Hmong Daw (Latin)":"mww",
"Hungarian":"hu",
"Icelandic":"is",
"Indonesian":"id",
"Inuinnaqtun":"ikt",
"Inuktitut":"iu",
"Inuktitut (Latin)":"iu-Latn",
"Irish":"ga",
"Italian":"it",
"Japanese":"ja",
"Kannada":"kn",
"Kazakh":"kk",
"Khmer":"km",
"Klingon":"tlh-Latn",
"Klingon (plqaD)":"tlh-Piqd",
"Korean":"ko",
"Kurdish (Central)":"ku",
"Kurdish (Northern)":"kmr",
"Kyrgyz (Cyrillic)":"ky",
"Lao":"lo",
"Latvian":"lv",
"Lithuanian":"lt",
"Macedonian":"mk",
"Malagasy":"mg",
"Malay (Latin)":"ms",
"Malayalam":"ml",
"Maltese":"mt",
"Maori":"mi",
"Marathi":"mr",
"Mongolian (Cyrillic)":"mn-Cyrl",
"Mongolian (Traditional)":"mn-Mong",
"Myanmar":"my",
"Nepali":"ne",
"Norwegian":"nb",
"Odia":"or",
"Pashto":"ps",
"Persian":"fa",
"Polish":"pl",
"Portuguese (Brazil)":"pt",
"Portuguese (Portugal)":"pt-pt",
"Punjabi":"pa",
"Queretaro Otomi":"otq",
"Romanian":"ro",
"Russian":"ru",
"Samoan (Latin)":"sm",
"Serbian (Cyrillic)":"sr-Cyrl",
"Serbian (Latin)":"sr-Latn",
"Slovak":"sk",
"Slovenian":"sl",
"Somali (Arabic)":"so",
"Spanish":"es",
"Swahili (Latin)":"sw",
"Swedish":"sv",
"Tahitian":"ty",
"Tamil":"ta",
"Tatar (Latin)":"tt",
"Telugu":"te",
"Thai":"th",
"Tibetan":"bo",
"Tigrinya":"ti",
"Tongan":"to",
"Turkish":"tr",
"Turkmen (Latin)":"tk",
"Ukrainian":"uk",
"Upper Sorbian":"hsb",
"Urdu":"ur",
"Uyghur (Arabic)":"ug",
"Uzbek (Latin":"uz",
"Vietnamese":"vi",
"Welsh":"cy",
"Yucatec Maya":"yua",
"Zulu":"zu"
}

def get_lang_code_autocomplete(current):
    data = []
    for key, value in lang_codes_autocomplete.items():
        if key.lower().startswith(current.lower()) or value.lower().startswith(current.lower()):
            data.append(app_commands.Choice(name=key, value=value))
    return data[0:24]


print("loading translate commands")

class Translate(commands.Cog):
    @app_commands.command(name="translate", description="Translate text using Microsoft Translation!")
    @app_commands.describe(text="The text you want to translate", lang="The language you want to translate from", to="The language you want to translate to")
    @app_commands.rename(text="text")
    async def translate(self, interaction: Interaction, lang: str, to:str, text:str):
        translatedText = await services.translate(lang, to, text) 
        await interaction.response.send_message(f"{translatedText}")
    
    @translate.autocomplete("lang")
    async def translate_autocomplete(self, interaction: Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        return get_lang_code_autocomplete(current)

    @translate.autocomplete("to")
    async def translate_autocomplete(self, interaction: Interaction, current: str) -> typing.List[app_commands.Choice[str]]:
        return get_lang_code_autocomplete(current)
        
async def setup(bot):
    await bot.add_cog(Translate(bot))