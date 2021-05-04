from discord.ext import commands
import discord
import numpy as np
import os
import traceback
from parse import parse

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
          

# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')
    
   
# @bot.command()
# async def neko(ctx):
#     await ctx.send('nyan')


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


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content.startswith('dice'):
        info = parse('dice {}d{}', message.content)
        if info:
            if info[1].isdecimal() and info[0].isdecimal():
                dice_num = int(info[0])
                dice_size = int(info[1])
                m = simple_dice(dice_size, dice_num)
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m)
                await message.channel.send(msg)
          
    if message.content == 'CCB' or message.content == 'ccb':
            m = simple_dice(100, 1)
            msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m)
            await message.channel.send(msg)
                    
    if message.content.startswith('CCB<='):     
        info = parse('CCB<={}', message.content)
        if info:
            if info[0].isdecimal():
                m = simple_dice(100, 1)
                if int(m) <= (int(info[0])/5):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Extreme!!!'
                elif (int(info[0])/5) < int(m) <= (int(info[0])/2):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Hard!!'
                elif (int(info[0])/2) < int(m) <= int(info[0]):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Succese!'
                elif int(m) > int(info[0]):
                    if int(info[0]) >= 50:
                        if int(info[0]) < int(m) <= 99:
                            msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Failure.' 
                        elif int(m) == 100:
                            msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Fanble...'
                    elif int(info[0]) < 50:
                        if int(info[0]) < int(m) <= 95:
                            msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Failure.' 
                        elif 96 <= int(m) <= 100:
                            msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Fanble...'
                #msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Succese!'
                await message.channel.send(msg)
                    
    if message.content.startswith('CCB>'):     
        info = parse('CCB>{}', message.content)
        if info:
            if info[0].isdecimal():
                m = simple_dice(100, 1)
                if int(m) > int(info[0]):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Succese!'
                elif int(m) <= int(info[0]):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Failure.' 
                #msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Succese!'
                await message.channel.send(msg)


client.run(token)
#bot.run(token)

