from discord.ext import commands
import discord
import logging
import traceback
import sys
import json, asyncio
from collections import Counter
import datetime
import re
import cogs.generic

description = """
I am Cecilia, bot by Mike Remedios (@Rem#1962) using discord.py.

Command examples:
    c.mywaifu
    C.roll 20
    cecilia.about
    Cecilia.featureRequest "SUPER COOL REQUEST!"

Features I want to add:
    Currency system based on bot usage and messages sent probably.
    Macros

Have fun!
"""

initial_extensions = [
    'cogs.generic',
    'cogs.braveFrontier'
]

discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.CRITICAL)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='cecilia.log', encoding='utf-8', mode='a')
log.addHandler(handler)

help_attrs = dict(hidden=True)

prefix = ['c.', 'C.', 'cecilia.', 'Cecilia.']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None, help_attrs=help_attrs)


@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()


@bot.event
async def on_command(command, ctx):
    bot.commands_used[command.name] += 1
    message = ctx.message
    destination = None


@bot.event
async def on_resumed():
    print('resumed...')


@bot.event
async def on_message(message):
    if message.channel.is_private:
        destination = 'Private Message'
    else:
        destination = '#{0.channel.name} ({0.server.name})'.format(message)
    #log.info('{0.timestamp}: {0.author.name} in {1}: {0.content}'.format(message, destination))
    if message.author.bot:
        return
    if re.search('cool', message.content, re.IGNORECASE):
        await bot.send_message(message.channel, 'cool cool cool')
    if re.search('ayy', message.content, re.IGNORECASE):
        await bot.send_message(message.channel, 'lmao')

    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    channels = member.server.channels
    for c in channels:
        if c.type is discord.ChannelType.text and c.position == 0:
            await bot.send_message(c, 'Welcome {0} to the server!'.format(member.mention))


if __name__ == '__main__':
    if any('debug' in arg.lower() for arg in sys.argv):
        bot.command_prefix = '$'

    bot.commands_used = Counter()
    bot.client_id = '220333798024282113'
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension %s' % extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))


bot.run('MjIwMzMzNzk4MDI0MjgyMTEz.CqexWg.cTs6uYzJ9nS8wCr-wWCaNcdpiZg')
handlers = log.handlers[:]
for hdlr in handlers:
    hdlr.close()
    log.removeHandler(hdlr)