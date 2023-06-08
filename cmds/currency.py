from discord.ext import commands
from discord import app_commands, Interaction

import services

import utils

class Currency(commands.Cog):
    @app_commands.command(name="currency", description="Convert currencies")
    @app_commands.describe(have="Currency you have", amount="Currency you have amount", want="Currency you want")
    @app_commands.rename(have="have", amount="amount", want="want")
    async def currency(self, interaction: Interaction, have:str, amount:float, want:str):
        currency_json = await services.currency_converter(have=have, want=want, amount=amount)
        
        await interaction.response.send_message(
            f"{utils.format_currency(currency_json['old_amount'])} {currency_json['old_currency']} equals to {utils.format_currency(currency_json['new_amount'])} {currency_json['new_currency']}"
        )
        
    @currency.autocomplete("have")
    @currency.autocomplete("want")
    async def currency_autocomplete(self, interaction: Interaction, current: str):
        return utils.get_auto_complete(current, services.currencies_codes)

async def setup(bot):
    await bot.add_cog(Currency(bot))