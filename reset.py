import discord
from discord.ext import commands

TOKEN = "BOT_TOKEN"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Resetting application commands...")
    
    try:
        await bot.tree.sync(guild=None)
        print("All application commands have been reset globally.")
    except Exception as e:
        print(f"Error resetting commands: {e}")
        
    await bot.close()

bot.run(TOKEN)