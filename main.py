import discord
from discord.ext import commands
import os
import music


cogs = [music]

client = commands.Bot(command_prefix='>', intents = discord.Intents.all())

for i in range (len(cogs)):
    cogs[i].setup()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
# Testing
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

#

client = MyClient()
client.run(os.getenv("TOKEN"))