import discord
from discord.ext import commands
import logging
import threading
from settings import TOKEN
from stats import stats as get_stats

description = '''Jeff's Discord Bot'''

bot = commands.Bot(command_prefix='.', description=description)

@bot.event 
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def stats(ctx, ign: str):
	esea_link = get_stats(ign)
	embed = discord.Embed(title="ESEA", description=(ign + " - " + esea_link), url=esea_link, inline=True)
	embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.5NSZleerSox2ncN8uNRYpAHaDd%26pid%3DApi&f=1')
	await ctx.send(embed=embed)
	# await ctx.send(ctx.author.created_at) make .register method

@bot.command()
async def register(ctx):
	# User check if already made
	return

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot.run(TOKEN)