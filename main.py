import asyncio
import discord
import os
from discord import Intents
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='-', intents=Intents.all(), case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():      # Changes bots Activity status on discord
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="über meine Schüler"))
    print("client logged in as Mrs. Sensei")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        print(f'Unable to load {filename[:-3]}')

client.run(token)