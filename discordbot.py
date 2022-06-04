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
    num = np.random.randint(1, int(dice_size + 1))
    return num

def simple_dice(dice_size, dice_num):
    dice_val = np.array([], dtype=np.int64)
    for i in range(dice_num):
        dice_val = np.append(dice_val, dice(dice_size))
    #msg = 'dice: ' + str(np.sum(dice_val)) + ' = ' + str(dice_val)
    m = dice_val
    return m

def CCB(m, a):
    if m <= (a/5):
        msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(a) + ' Extreme!!!'
    elif (a/5) < m <= (a/2):
        msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(a) + ' Hard!!'
    elif (a/2) < m <= a:
        msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(a) + ' Success!'
    elif m > a:
        if a >= 50:
            if a < m <= 99:
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(a) + ' Failure.'
            elif m == 100:
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(a) + ' Fanble...'
        elif a < 50:
            if a < m <= 95:
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(a) + ' Failure.'
            elif 96 <= m <= 100:
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(a) + ' Fanble...'
    return msg

def bp(m, a, M):
    if m <= (a/5):
        msg = 'dice: ' + str(M) + ' = ' + str(m) + ' <= ' + str(a) + ' Extreme!!!'
    elif (a/5) < m <= (a/2):
        msg = 'dice: ' + str(M) + ' = ' + str(m) + ' <= ' + str(a) + ' Hard!!'
    elif (a/2) < m <= a:
        msg = 'dice: ' + str(M) + ' = ' + str(m) + ' <= ' + str(a) + ' Success!'
    elif m > a:
        if a >= 50:
            if a < m <= 99:
                msg = 'dice: ' + str(M) + ' = ' + str(m) + ' > ' + str(a) + ' Failure.'
            elif m == 100:
                msg = 'dice: ' + str(M) + ' = ' + str(m) + ' > ' + str(a) + ' Fanble...'
        elif a < 50:
            if a < m <= 95:
                msg = 'dice: ' + str(M) + ' = ' + str(m) + ' > ' + str(a) + ' Failure.'
            elif 96 <= m <= 100:
                msg = 'dice: ' + str(M) + ' = ' + str(m) + ' > ' + str(a) + ' Fanble...'
    return msg

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.reply('にゃーん')

    if message.content.startswith('/dice'):
        info = parse('/dice {}d{}', message.content)
        info2 = parse('/dice {}d{}+{}', message.content)
        info3 = parse('/dice {}d{}-{}', message.content)
        info4 = parse('/dice {}d{}*{}', message.content)
        info5 = parse('/dice {}d{}/{}', message.content)
        if info:
            if info[1].isdecimal() and info[0].isdecimal():
                dice_num = int(info[0])
                dice_size = int(info[1])
                m = simple_dice(dice_size, dice_num)
                msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m)
                await message.reply(msg)
        if info2:
            if info2[1].isdecimal() and info2[0].isdecimal():
                dice_num = int(info2[0])
                dice_size = int(info2[1])
                m = simple_dice(dice_size, dice_num)
                c = int(info2[2])
                msg = 'dice: ' + str(np.sum(m))+str(m) + '+' + str(c)+ ' = ' + str(np.sum(m)+c)
                await message.reply(msg)
        if info3:
            if info3[1].isdecimal() and info3[0].isdecimal():
                dice_num = int(info3[0])
                dice_size = int(info3[1])
                m = simple_dice(dice_size, dice_num)
                c = int(info3[2])
                msg = 'dice: ' + str(np.sum(m))+str(m) + '-' + str(c)+ ' = ' + str(np.sum(m)-c)
                await message.reply(msg)
        if info4:
            if info4[1].isdecimal() and info4[0].isdecimal():
                dice_num = int(info4[0])
                dice_size = int(info4[1])
                m = simple_dice(dice_size, dice_num)
                c = int(info4[2])
                msg = 'dice: ' + str(np.sum(m))+str(m) + '*' + str(c)+ ' = ' + str(np.sum(m)*c)
                await message.reply(msg)
        if info5:
            if info5[1].isdecimal() and info5[0].isdecimal():
                dice_num = int(info5[0])
                dice_size = int(info5[1])
                m = simple_dice(dice_size, dice_num)
                c = int(info5[2])
                msg = 'dice: ' + str(np.sum(m))+str(m) + '/' + str(c)+ ' = ' + str(-(-np.sum(m)//c))
                await message.reply(msg)
          
    if message.content == 'CCB' or message.content == 'ccb':
        m = simple_dice(100, 1)
        msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m)
        await message.reply(msg)
                    
    if message.content.startswith('CCB<='):     
        info = parse('CCB<={}', message.content)
        info2 = parse('CCB<={}+{}', message.content)
        info3 = parse('CCB<={}-{}', message.content)
        info_ = parse('CCB<={} {}', message.content)
        info_2 = parse('CCB<={}+{} {}', message.content)
        info_3 = parse('CCB<={}-{} {}', message.content)

        if info:
            if info[0].isdecimal():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info[0]))
                await message.reply(msg)
        if info2:
            if info2[0].isdecimal() and info2[1].isdecimal():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info2[0])+int(info2[1]))
                await message.reply(msg)
        if info3:
            if info3[0].isdecimal() and info3[1].isdecimal():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info3[0])-int(info3[1]))
                await message.reply(msg)
        if info_:
            if info_[0].isdecimal() and info_[1].isalpha():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info_[0]))
                await message.reply(msg)
        if info_2:
            if info_2[0].isdecimal() and info_2[1].isdecimal() and info_2[2].isalpha():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info_2[0])+int(info_2[1]))
                await message.reply(msg)
        if info_3:
            if info_3[0].isdecimal() and info_3[1].isdecimal() and info_3[2].isalpha():
                m = simple_dice(100, 1)
                msg = CCB(m, int(info_3[0])-int(info_3[1]))
                await message.reply(msg)
                    
    if message.content.startswith('CCB>'):     
        info = parse('CCB>{}', message.content)
        if info:
            if info[0].isdecimal():
                m = simple_dice(100, 1)
                if int(m) > int(info[0]):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' > ' + str(info[0]) + ' Success!'
                elif int(m) <= int(info[0]):
                    msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Failure.' 
                #msg = 'dice: ' + str(np.sum(m)) + ' = ' + str(m) + ' <= ' + str(info[0]) + ' Succese!'
                await message.reply(msg)
		
    
    if message.content.startswith('/p'):
        info = parse('/p{}CCB', message.content)
        info2 = parse('/p{}CCB<={}', message.content)
        if info:
            if info[0].isdecimal():
                j = int(info[0])
                m = dice(10)
                if m == 10:
                    m = 0
                #await message.channel.send(str(j))
                M = []
                for i in range(j+1):
                    M.append(dice(10))
                    #await message.channel.send(str(M[i]))
                    if M[i] == 10:
                        M[i] = 0
                    M[i] = M[i] * 10 + m
                    if M[i] == 0:
                        M[i] = 100
                    #await message.channel.send(str(M[i]))
                msg = 'dice: ' + str(M) + ' = ' + str(max(M))
                await message.reply(msg)
        if info2:
            if info2[0].isdecimal() and info2[1].isdecimal():
                j = int(info2[0])
                m = dice(10)
                if m == 10:
                    m = 0
                #await message.channel.send(str(j))
                M = []
                for i in range(j+1):
                    M.append(dice(10))
                    #await message.channel.send(str(M[i]))
                    if M[i] == 10:
                        M[i] = 0
                    M[i] = M[i] * 10 + m
                    if M[i] == 0:
                        M[i] = 100
                    #await message.channel.send(str(M[i]))
                Mm = max(M)
                msg = bp(Mm, int(info2[1]), M)
                await message.reply(msg)
		
                    
    if message.content.startswith('/b'):
        info = parse('/b{}CCB', message.content)
        info2 = parse('/b{}CCB<={}', message.content)
        if info:
            if info[0].isdecimal():
                j = int(info[0])
                m = dice(10)
                if m == 10:
                    m = 0
                #await message.channel.send(str(j))
                M = []
                for i in range(j+1):
                    M.append(dice(10))
                    #await message.channel.send(str(M[i]))
                    if M[i] == 10:
                        M[i] = 0
                    M[i] = M[i] * 10 + m
                    if M[i] == 0:
                        M[i] = 100
                    #await message.channel.send(str(M[i]))
                msg = 'dice: ' + str(M) + ' = ' + str(min(M))
                await message.reply(msg)
        if info2:
            if info2[0].isdecimal() and info2[1].isdecimal():
                j = int(info2[0])
                m = dice(10)
                if m == 10:
                    m = 0
                #await message.channel.send(str(j))
                M = []
                for i in range(j+1):
                    M.append(dice(10))
                    #await message.channel.send(str(M[i]))
                    if M[i] == 10:
                        M[i] = 0
                    M[i] = M[i] * 10 + m
                    if M[i] == 0:
                        M[i] = 100
                    #await message.channel.send(str(M[i]))
                Mm = min(M)
                msg = bp(Mm, int(info2[1]), M)
                await message.reply(msg)
            
        

    if message.content == '/mad_rt':
        roll = []
        roll.append('a')
        roll.append('dice: [1] -> 健忘症')
        roll.append('dice: [2] -> 身体症状症')
        roll.append('dice: [3] -> 暴力衝動')
        roll.append('dice: [4] -> 偏執症')
        roll.append('dice: [5] -> 重要な人々')
        roll.append('dice: [6] -> 失神')
        roll.append('dice: [7] -> パニックになって逃亡')
        roll.append('dice: [8] -> 身体的ヒステリーもしくは感情爆発')
        roll.append('dice: [9] -> 恐怖症の獲得（1d100をロールするかKPが1つ選ぶ)')
        roll.append('dice: [0] -> マニアの獲得（1d100をロールするかKPが1つ選ぶ)')
        m = roll[dice(10)]
        a = dice(10)
        m += '\ndice: ['+ str(a) +'] -> 一時的狂気(' + str(a) + 'ラウンド) or (' + str(a) + '時間)'
        await message.reply(m)

    if message.content == '/mad_s':
        roll = []
        roll.append('a')
        roll.append('dice: [1] -> 健忘症')
        roll.append('dice: [2] -> 盗難')
        roll.append('dice: [3] -> 暴行')
        roll.append('dice: [4] -> 暴力')
        roll.append('dice: [5] -> イデオロギー・信念')
        roll.append('dice: [6] -> 重要な人々')
        roll.append('dice: [7] -> 収容')
        roll.append('dice: [8] -> パニック')
        roll.append('dice: [9] -> 恐怖症の獲得（1d100をロールするかKPが1つ選ぶ)')
        roll.append('dice: [0] -> マニアの獲得（1d100をロールするかKPが1つ選ぶ)')
        m = roll[dice(10)]
        a = dice(10)
        m += '\ndice: ['+ str(a) +'] -> 一時的狂気(' + str(a) + '時間後に意識を取り戻す)'
        await message.reply(m)


client.run(token)
#bot.run(token)

