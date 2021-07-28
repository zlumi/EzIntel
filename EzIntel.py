import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
botId = os.getenv("BOT_ID")
botPrefix = ['ez.', 'Ez.', 'eZ.', 'EZ.']
bot = commands.Bot(command_prefix = botPrefix, description='Ultra Humane')

bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} with id {bot.user.id}')
    activity = discord.Activity(type=discord.ActivityType.watching, name="y'all being funny")
    await bot.change_presence(status=discord.Status.idle, activity=activity)

if __name__ == '__main__':
    cogs = []
    for subModule in os.listdir('./cogs'):
        if subModule.endswith('.py'):
            cogs.append('cogs.' + subModule[:-len('.py')])
    for subModule in cogs:
        bot.load_extension(subModule)

    bot.run(TOKEN, bot=True, reconnect=True)