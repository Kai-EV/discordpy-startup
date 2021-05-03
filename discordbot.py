from discord.ext import commands
import discord
import numpy as np
import os
import traceback
from parse import parse

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
          

def dice(dice_size):
    num = np.random.randint(1, int(dice_size))
    return num

def simple_dice(dice_size, dice_num):
    dice_val = np.array([], dtype=np.int64)
    for i in range(dice_num):
        dice_val = np.append(dice_val, dice(dice_size))
    #msg = 'dice: ' + str(np.sum(dice_val)) + ' = ' + str(dice_val)
    m = dice_val
    return m


@client.event
async def on_ready():
    print('Logged in')
    print('-----')
          

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'neko':
        await message.channel.send('にゃーん')

@client.event
async def on_message(message):
    if message.content.startswith('dice'):
          await client.send_message(message.channel, 'bot')
          

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


client.run(token)
bot.run(token)
