from discord.ext import commands
import numpy as np
import os
import traceback
#from parse import parse

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

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('dice'):
#         info = parse('dice {}d{}', message.content)
#         if info:
#             if info[1].isdecimal() and info[0].isdecimal():
#                 dice_num = int(info[0])
#                 dice_size = int(info[1])
#                 #key = info[2]
#                 # メッセージを書きます
#                 #m = message.author.name + ' '
#                 # if key == '一時的狂気':
#                 #     m = temp_madness()
#                 # elif key == '不定の狂気':
#                 #     m = ind_madness()
#                 #if key == 'dice':
#                 m = simple_dice(dice_size, dice_num)
#                 msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m)
#                 await message.channel.send(msg)
                
               
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
