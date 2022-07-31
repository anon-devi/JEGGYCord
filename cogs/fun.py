import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import random
import aiohttp
import asyncio

meme_colour=[0xE8FF45,0x00FF1F,0x14B5B8,0x0859B9,0x9504B2,0xE70C0C]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = discord.Bot(debug_guilds=[931791681102180422])

    
    @slash_command(description="ask a question 👀")
    async def ball(self, ctx, *, question):

        responses = [
    discord.Embed(title='It is certain.', color=0x5865F2),
    discord.Embed(title='It is decidedly so.', color=0x5865F2),
    discord.Embed(title='Without a doubt.', color=0x5865F2),
    discord.Embed(title='Yes - definitely.', color=0x5865F2),
    discord.Embed(title='You may rely on it.', color=0x5865F2),
    discord.Embed(title='Most likely.', color=0x5865F2),
    discord.Embed(title='Outlook good.', color=0x5865F2),
    discord.Embed(title='Yes.', color=0x5865F2),
    discord.Embed(title='Signs point to yes.', color=0x5865F2),
    discord.Embed(title='Reply hazy, try again.', color=0x5865F2),
    discord.Embed(title='Ask again later.', color=0x5865F2),
    discord.Embed(title='Better not tell you now.', color=0x5865F2),
    discord.Embed(title='Cannot predict now.', color=0x5865F2),
    discord.Embed(title='Concentrate and ask again.', color=0x5865F2),
    discord.Embed(title="Don't count on it.", color=0x5865F2),
    discord.Embed(title='My reply is no.', color=0x5865F2),
    discord.Embed(title='My sources say no.', color=0x5865F2),
    discord.Embed(title='Outlook not very good.', color=0x5865F2),
    discord.Embed(title='Very doubtful.', color=0x5865F2)
        ]
        responses = random.choice(responses)
        await ctx.respond(content=f'Question: {question}\nAnswer:', embed=responses)

    
    @slash_command(description="displays random meme")
    async def meme(self, ctx):
        embed=discord.Embed(description="",colour=random.choice(meme_colour))
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))