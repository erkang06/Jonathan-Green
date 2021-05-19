# bot.py
import discord
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands')

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('sir, '),
    help_command = None
)

@bot.command(name='help')
async def help(ctx):
    await ctx.send("Custom help command")

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='embed')
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)

bot.run(TOKEN)
