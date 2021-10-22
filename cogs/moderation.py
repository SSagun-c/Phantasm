import discord
from discord import guild
from discord.ext import commands

class Reviver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delete(ctx, channel_name):
        # check if the channel exists
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        
        # if the channel exists
        if existing_channel is not None:
            await existing_channel.delete()
        # if the channel does not exist, inform the user
        else:
            await ctx.send(f'No channel named, "{channel_name}", was found')

def setup(bot):
    bot.add_cog(Reviver(bot))