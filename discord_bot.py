from typing import Union
from discord import User, Member, ClientUser
from discord.ext import commands
from discord.ext.commands import Context

from .token import TOKEN

client = commands.Bot(command_prefix='.')


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


@client.command(name='avatar')
async def avatar_command(ctx: Context, user: Union[User, Member, ClientUser]):
    if not isinstance(user, (User, Member, ClientUser)):
        return

    avatar_url = str(user.avatar_url_as(format='png'))

    await ctx.send(avatar_url)


client.run(TOKEN)
