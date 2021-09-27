import discord
import aiohttp
from discord.ext import commands
import datetime as dt

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="quote", aliases=["zitat"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def anime_quote(self, ctx):
        async with aiohttp.ClientSession() as Session:
            request = await Session.get('https://animechan.vercel.app/api/random')
            aqjson = await request.json()
        embed = discord.Embed(title=f"Anime: {aqjson['anime']}", description=f"Character: {aqjson['character']}", color=0xED61D3)
        embed.add_field(name="Quote", value=aqjson['quote'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Anime(bot))