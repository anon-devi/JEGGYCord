import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from discord import channel
import datetime
import time
from datetime import timedelta

embed = discord.Embed(

)


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])
    

    @slash_command(description='kicks a mentioned member')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason = None):
        if not reason:
            await user.kick()
            await ctx.respond(f"{user} has been kicked for an **unspecified reason**.")
        else:
            await user.kick(reason=reason)
            await ctx.respond(f"**{user}** has been kicked for **{reason}**.")
    
    @slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason = None):
        if not reason:
            await user.ban()
            await ctx.respond(f"**{user}** has been banned for an **unspecified reason**.")
        else:
            await user.ban(reason=reason)
            await ctx.respond(f"**{user}** has been banned for **{reason}**.")
    

    @slash_command()
    async def timeout(self, ctx: discord.ApplicationContext, member: discord.Member, minutes: int):

        duration = datetime.timedelta(minutes=minutes)
        await member.timeout_for(duration)
        await ctx.respond(f"Member timed out for {minutes} minutes.")

    """
    The method used above is a shortcut for:
    until = discord.utils.utcnow() + datetime.timedelta(minutes=minutes)
    await member.timeout(until)
    """


    


def setup(bot):
    bot.add_cog(Moderation(bot))