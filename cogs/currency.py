from discord.ext import commands
import discord
import asyncio

class currency:
    """Neural net commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self):
        "-It says Hello."
        if(True and True and True):
            await self.bot.say('hello')


def setup(bot):
    bot.add_cog(currency(bot))