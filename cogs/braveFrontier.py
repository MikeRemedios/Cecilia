from discord.ext import commands
import discord
import asyncio
from bs4 import BeautifulSoup
import requests
import urllib.request
import random
import re


def url_open(url):
    try:
        resp = requests.get(url)
        data = BeautifulSoup(resp.content, "html.parser")
    except Exception as e:
        print(e)
        running = False
    else:
        return data


class braveFrontier:
    """Neural net commands"""

    def __init__(self, bot):
        self.bot = bot
        random.seed()

    @commands.command()
    async def mywaifu(self):
        "-waifu"
        url = 'http://bravefrontierglobal.wikia.com/wiki/Category:Female_Unit'
        rand = random.randint(0, 1)
        while rand == 0:
            try:
                data = url_open(url)
                url = 'http://bravefrontierglobal.wikia.com{0}'.format(re.search(re.compile(
                    '<a href="(/wiki/Category:Female_Unit\?pagefrom=.+#mw-pages)" '
                    'title="Category:Female Unit">next 200</a>'), str(data)).group(1))
                rand = random.randint(0, 1)
            except AttributeError:
                rand = 1
        else:
            data = url_open(url)
            m = re.finditer(re.compile(
                '<li><a href="(/wiki/.+)"'
                ' title=".+">(.+)</a>'), str(data))

        m = tuple(m)
        index = random.randint(0, len(m) - 1)
        title = m[index].group(1)
        name = m[index].group(2)

        url = 'http://bravefrontierglobal.wikia.com{0}'.format(title)
        data = url_open(url)
        waifu = re.search('http://vignette\d\.wikia\.nocookie\.net/bravefrontierglobal/.+full.+\.png',
                          str(data)).group(0)

        await self.bot.reply('Your new waifu is ***{0}!***\n{1}'.format(name, waifu))


def setup(bot):
    bot.add_cog(braveFrontier(bot))
