from discord.ext import commands
import discord
import asyncio
import time
import os
import subprocess
import datetime
import re


class generic:
    """Neural net commands"""

    def __init__(self, bot):
        self.bot = bot
        self.startTime = time.time()

    @commands.command()
    async def about(self):
        "-Print some info about the bot"
        await self.bot.say("I'm cuter than you")

    @commands.command()
    async def changelog(self):
        "-Prints the changelog"
        f = open('changelog.txt', 'r')
        file_contents = f.read()
        f.close()
        await self.bot.say("```\n" + file_contents + "\n```")

    @commands.command()
    async def donate(self):
        "-Post link for donors"
        await self.bot.say("www.gimmedatcash.com")

    @commands.command()
    async def featureRequest(self, feature="placeholder"):
        "-Logs a feature request, request MUST be enclosed in quotes \"Example request\""
        try:
            f = open('requests.txt', 'a')
            f.write(feature + '\n')
            f.close()
            await self.bot.say('Added to request queue')
        except:
            await self.bot.say('Missing request. Post in form \'c.featureRequest "feature here"\'')

    @commands.command()
    async def invite(self):
        "-Posts invite link"
        perms = discord.Permissions.none()
        await self.bot.say(discord.utils.oauth_url(self.bot.client_id, perms))

    @commands.command()
    async def ping(self):
        "-ping time"
        start = time.time()
        print(os.popen(r'ping {}'.format('discord.gg')).read().strip())
        m = re.search(re.compile('Minimum = [0-9]+ms, Maximum = [0-9]+ms, Average = [0-9]+ms'),
                      os.popen(r'ping {}'.format('discord.gg')).read().strip())
        await self.bot.say(m.group(0))

    @commands.command()
    async def uptime(self):
        "-posts bot uptime"
        m, s = divmod(time.time() - self.startTime, 60)
        h, m = divmod(m, 60)

        await self.bot.say("%d:%02d:%02d" % (h, m, s))

    @commands.command()
    async def pm(self):
        "-PMs me"
        await self.bot.send_message()


def setup(bot):
    bot.add_cog(generic(bot))
