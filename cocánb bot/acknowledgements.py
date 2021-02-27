import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*', description='A bot for members of the Cocánb')


class Acknowledgements(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @bot.command (name='recommended', help='Sends a list of recommended servers')
  async def recommended(self, ctx):
    await ctx.send ('https://docs.google.com/document/d/1_FyyY8d9SavNzU7AHD5q6FuBLW4Wr3CkRgfXhXfckRA/edit?usp=drivesdk')
  
  @bot.command (name='server', help='Sends a link to the Cocánb server')
  async def server(self, ctx):
    await ctx.send ('https://discord.gg/V3vGPg5AFA')
  
  @bot.command (name='bot', help='Sends a link to add this bot')
  async def bot(self, ctx):
    await ctx.send ('https://discord.com/api/oauth2/authorize?client_id=801983327023398912&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D801983327023398912%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscord.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D801983&scope=bot')

