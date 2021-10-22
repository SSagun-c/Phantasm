import discord
from discord.ext import commands

class Reviver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deletechannel(self, ctx, channel: discord.TextChannel):
        embed = discord.Embed(
            title = 'Successful!',
            description = f'The channel `{channel}` has ben deleted.'
        )
        if ctx.author.guild_permissions.manage_channels:
            await ctx.send(embed=embed)
            await channel.delete()
        

def setup(bot):
    bot.add_cog(Reviver(bot))