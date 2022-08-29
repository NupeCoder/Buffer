import discord
from discord.ext import commands
import config
import FighterSearch



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print('BOT ON')


@bot.command(name="ufc")
async def find(ctx, name):
        FighterSearch.search(name)
        await ctx.reply(FighterSearch.result)


bot.run(config.TOKEN)
