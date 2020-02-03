from typing import Union
from discord import User, Member, ClientUser
from discord.ext.commands import Context
from bot import Bot
from bot_token import BOT_TOKEN
from censor import censor

client = Bot(
    command_prefix='.'
)


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


@client.event
async def on_message(msg):

    content = list(map(lambda s: s.lower(), msg.content.split()))

    for el in censor:
        el = el.lower()
        if el in content:
            break

    else:
        return

    await msg.delete()



@client.command()
async def ping(ctx: Context):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(name='avatar')
async def avatar_command(ctx: Context, user: Union[User, Member, ClientUser]):
    if not isinstance(user, (User, Member, ClientUser)):
        return

    avatar_url = str(user.avatar_url_as(format='png'))

    await ctx.send(avatar_url)


client.run(BOT_TOKEN)
