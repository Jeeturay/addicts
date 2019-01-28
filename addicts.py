import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("boot Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
    
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name + "#" + bot.user.discriminator)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="📥DM me for help!"))
bot.run('NTA4ODY3MDUzMzYxNTYxNjAx.DzBVFg.xGJ-AJq8dr8q9fcCrCUmCqGMsJc')