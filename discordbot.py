from discord.ext import commands
import numpy as np
import os
import traceback
#from parse import parse

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
          
               
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
   
@bot.command()
async def neko(ctx):
    await ctx.send('nyan')


bot.run(token)
