import discord
import aiohttp
from discord.ext import commands
import datetime as dt

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Anime(bot))