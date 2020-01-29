"""Adding session and teach discord.ext.commands.Bot how to use it on Bot.start(), Bot.close(). Logging cogs loads"""

import logging
import asyncio
import aiohttp
import socket
import uvloop

from discord.ext import commands

log = logging.getLogger('bot')

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
log.info('UVLoop has been successfully settled')


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.connector = aiohttp.TCPConnector(
            resolver=aiohttp.AsyncResolver(),
            family=socket.AF_INET,
            verify_ssl=False
        )

        kwargs['loop'] = asyncio.get_event_loop()
        kwargs['connector'] = self.connector

        super().__init__(*args, **kwargs)

    def add_cog(self, cog: commands.Cog) -> None:
        """Loading a cog and informing about it"""
        super().add_cog(cog)

        log.info(f"Cog has been successfully loaded: {cog.qualified_name}")

    async def start(self, *args, **kwargs) -> None:
        await super().start(*args, **kwargs)

    async def close(self) -> None:
        await super().close()

