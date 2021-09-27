import discord
from discord.ext import commands
from discord.ext.commands import cooldown

class Bullshit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == 'owo':
            await message.channel.send('What\'s this?')
    
def setup(bot):
    bot.add_cog(Bullshit(bot))