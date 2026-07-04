import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    """Check bot latency"""
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(name='hello')
async def hello(ctx):
    """Say hello"""
    await ctx.send(f'Hello {ctx.author.name}!')

# Run the bot
token = os.getenv('DISCORD_TOKEN')
if not token:
    raise ValueError("DISCORD_TOKEN environment variable not set")

bot.run(token)

