import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')



client.run('NjcwNjgzMDQxNTc1OTkzMzY1.Xix8Zg.vakRr3Uy5SgMDtyFlICqmmi5v24')