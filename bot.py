import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command(name="ping")
async def ping(ctx):
    """Check bot latency."""
    await ctx.send(f"Pong! Latency: {round(bot.latency * 1000)}ms")


if __name__ == "__main__":
    bot.run(TOKEN)
