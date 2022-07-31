from typing_extensions import Required
import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import datetime
import asyncio
import aiohttp
import random
from discord import Option, channel
from discord import message
from discord import Option

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])
    

    @slash_command(description="creates a poll")
    async def poll(self, ctx, question, option1=None, option2=None):
        if option1==None and option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.respond(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = #No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option1==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.respond(f"```New poll: \n{question}```\n**✅ = {option1}#**\n**❎ = No**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        elif option2==None:
            await ctx.channel.purge(limit=1)
            message = await ctx.respond(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = #{option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')
        else:
            await ctx.channel.purge(limit=1)
            message = await ctx.respond(f"```New poll: \n{question}```\n**✅ = {option1}#**\n**❎ = {option2}**")
            await message.add_reaction('❎')
            await message.add_reaction('✅')

    @slash_command(description="creates a giveaway")
    @commands.has_permissions(manage_messages=True)
    async def create(self, ctx, mins: int, *, prize: str):
        embed = discord.Embed(title="Giveaway!",
        description=f"{prize}",
        color=ctx.author.color)

        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)

        embed.add_field(name="Ends at:", value=f"{end} UTC")

        my_msg = await ctx.send(embed=embed)
        await my_msg.add_reaction("🎉")

        await asyncio.sleep(mins)

        new_msg = await ctx.channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()

        users.pop(users.index(discord.Bot.user))

        winner = random.choice(users)

        await ctx.respond(f"Congratulations! {winner.mention} won {prize}!")


    @slash_command(description="deletes selected amount of messages in a channel")
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, messages: Option(int, description="How many messages do you want to purge?", required = True)):
        await ctx.defer()
        z = await ctx.channel.purge(limit = messages)
        await ctx.respond(f'i have purged {len(z)}')

    
    @slash_command(description="displays list of all jeggy commands")
    async def help(self, ctx):
        embed=discord.Embed(title="Commands")
        embed.set_author(name="By Dxrk & Coder")
        embed.add_field(name="/meme", value="Displays random memes", inline=True)
        #embed.add_field(name=">help", value="shows this command", inline=False)
        embed.add_field(name="/kick", value="kicks selected member (only for mods)", inline=False)
        embed.add_field(name="/ban", value="bans selected member(only for mods)", inline=False)
        #embed.add_field(name=">_8ball", value="ask a question", inline=True)
        #embed.add_field(name=">bot", value="displays jeggie's invite link", inline=False)
        #embed.add_field(name=">server", value="displays main server invite link", inline=True)
        #embed.add_field(name='>commands', value='displays this embed', inline=False)
        #embed.add_field(name='>poll', value='creates a poll (must include a question and 2 options,)', inline=False)
        #embed.add_field(name='>mute', value='mutes a targeted member', inline=False)
        #embed.add_field(name='>unmute', value='unmutes a muted member (must ping member you want to unmute)', inline=False)
        embed.add_field(name='/purge', value='deletes messages on a channel(must include amount or it will delete every message in the channel)', inline=False)
        #embed.add_field(name='>slowmode', value='adds slowmode to chat (must include time as seconds)', inline=False)
        embed.add_field(name='/ball', value='answers questions with yes/no format', inline=False)
        embed.add_field(name='/create', value='Creates a giveaway', inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Poll(bot))