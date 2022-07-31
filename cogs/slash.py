from distutils.log import debug
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import asyncio

#bot = discord.Bot(debug_guilds=[931791681102180422])

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])
    

    @slash_command(description='test command', )
    async def test(self, ctx):
        await ctx.respond('it works')


def setup(bot):
    bot.add_cog(Slash(bot))