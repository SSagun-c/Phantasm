import discord
from discord.ext import commands
from discord import Member
import datetime as dt

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome Cog is loaded")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(901221349450735616)

        if not channel:
            return

        embed = discord.Embed(title=f"Herzlich Willkommen", description=f"**Wir haben einen neuen Schüler in unserer Klasse!**\nStellt euch, {member.mention}, doch bitte einmal vor.", color=0xF280DF)
        embed.set_thumbnail(url=member.avatar_url)
        embed.timestamp = dt.datetime.utcnow()
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcome(bot))