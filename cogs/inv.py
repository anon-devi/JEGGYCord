import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import channel
from discord import message



class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])
    
    @slash_command(description="generates server invite")
    async def invite(self, ctx, max_age: int, max_uses: int):
        invite = await ctx.channel.create_invite()
        await ctx.respond(f"Your invite is {invite}")

    




def setup(bot):
    bot.add_cog(Invite(bot))