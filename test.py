import discord
from discord.ext import commands
import logging
from settings import TOKEN

description = '''Jeff's Discord Bot'''


bot = commands.Bot(command_prefix='.', description=description)

@bot.event 
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def stats(ctx, ign: str):
	await ctx.send(ign)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.run(TOKEN)