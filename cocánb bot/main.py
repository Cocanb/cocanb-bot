import discord
from discord.ext import commands

import json

import os
from dotenv import load_dotenv

from unicodedata import *

from datetime import datetime, timedelta
from time import localtime, strftime
import time

from replit import db
from keep_alive import keep_alive

from cocanb import Cocanb
from unicode import Unicode
from acknowledgements import Acknowledgements

load_dotenv()
TOKEN = os.getenv('TOKEN')



def FC(id,prefixes):
    for prefix in prefixes:
        if prefix['id']==id:
            return prefix['prefix']
    
    with open("prefixes.json", "w") as fileout:
        prefixes.append({"id":id, "prefix":"!"})
        json.dump(prefixes,fileout)
        return "!"

def read(bot,message):
    with open("prefixes.json", "r") as filein:
        prefixes = json.load(filein)
        return FC(str(message.guild.id),prefixes)



bot = commands.Bot(command_prefix=read,
                   description='A bot for members of the Cocánb')



@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as filein:
        prefixes = json.load(filein)

    for prefix in prefixes:
        if prefix['id']==guild.id:
            prefixes.pop(prefixes.index(prefix))

    with open("prefixes.json", "w") as fileout:
        json.dump(prefixes,fileout)


@bot.command(aliases=['changeprefix', 'prefixset', 'prefixchange'])
async def write(ctx,NEWPREFIX):
    with open("prefixes.json", "r") as filein:
        prefixes  = json.load(filein)
        for x in range(len(prefixes)):
            if prefixes[x]['id']==str(ctx.guild.id):

                prefixes[x]['prefix'] = NEWPREFIX

    with open("prefixes.json", "w") as fileout:
        json.dump(prefixes,fileout)
        await ctx.send("Changed prefix to: " + NEWPREFIX)



@bot.event
async def on_ready():
  #for guild in bot.guilds:
        #print(guild.id)
        #to_leave = bot.get_guild(guild.id)
        #await to_leave.leave()
  await bot.change_presence(activity=discord.Game(name="help"))


@bot.command(name='time',
             help='Shows current time given a timezone (In (-)HH:MM format)')
async def time(ctx, timezone: str = '00:00'):
	if timezone[0] == '-':
		hours = int(timezone[:-3]) - int(timezone[-2:]) / 60
	else:
		hours = int(timezone[:-3]) + int(timezone[-2:]) / 60
	future_time = datetime.today() + timedelta(hours=hours)
	if timezone == '00:00':
		plus = '±'
	elif timezone[0] == '-':
		plus = ''
	elif timezone[0] == '+':
		plus = ''
	else:
		plus = '+'
	week_day = future_time.weekday()
	weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
	            "Saturday", "Sunday")
	week_day = weekdays[week_day]
	if timezone[-3] == ':':
		await ctx.send('`' + week_day + ', ' + str(future_time) + ', UTC' +
		               plus + timezone + '`')
	else:
		pass


@bot.command(name="return", help="Returns message")
async def msgreturn(ctx, *, msg):
	await ctx.send(msg)


@bot.command(
    name="delreturn",
    help=
    "Returns message (deletes original message)\n(may not work on every server)"
)
async def delmsgreturn(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send(msg)


@bot.command(
    name="emoji",
    help=
    "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illgal/illegal, void, woah\n(words separated by / output the same emoji)"
)
async def emoji(ctx, *, name):
	name = name.lower()
	if name == "ye":
		await ctx.send("<:ye:799291949273317377>")
	elif name == "amogus" or name == "amongus" or name == "among us":
		await ctx.send("<:amogus:809427238784860210>")
	elif name == "barry":
		await ctx.send("<:barry:811154017672757270>")
	elif name == "biang":
		await ctx.send("<:biang:809669658143227905>")
	elif name == "bruh" or name == "facepalm":
		await ctx.send("<:bruh:801100506251526145>")
	elif name == "surprised" or name == "that's illegal" or name == "illegal":
		await ctx.send("<:surprised:801099678988501072>")
	elif name == "void":
		await ctx.send("<:void:798150976191201313>")
	elif name == "woah":
		await ctx.send("<:woah:807905973162999818>")
	else:
		await ctx.send("Invalid emoji")


bot.add_cog(Cocanb(bot))
bot.add_cog(Unicode(bot))
bot.add_cog(Acknowledgements(bot))

keep_alive()
bot.run(TOKEN)