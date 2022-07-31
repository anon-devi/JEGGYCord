import discord 
from discord.ext import commands
from discord.commands import slash_command

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])