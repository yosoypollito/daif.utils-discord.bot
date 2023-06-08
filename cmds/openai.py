import discord
from discord import app_commands
from discord.ext import commands
import io

import services



print("Loading openai Commands")

class OpenAi(app_commands.Group):
        @app_commands.command(name="chatgpt", description="Use chatgpt!")
        @app_commands.describe(question="What do you want to ask?")
        async def chatgpt(self, interaction: discord.Interaction, question: str):
            await interaction.response.defer()
            response = await services.chatgpt.chatCompletion(question)
            print(response)
            await interaction.edit_original_response(content=f">>> {response}")
        @app_commands.command(name="dalle", description="Use dall-e to create an image with text!")
        @app_commands.describe(context="What do you want to create?")
        async def dalle(self, interaction: discord.Interaction, context: str):
            # await interaction.response.defer()
            await interaction.response.send_message("Getting image")
            response = await services.dall_e.generateImage(context)
            
            print("Sending image")
            
            with io.BytesIO(response) as file:
                await interaction.edit_original_response(attachments=[discord.File(file, filename="dalle.png")])
            

                
async def setup(bot):
    bot.tree.add_command(OpenAi(name="openai"))