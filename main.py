from http import client
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('Rin has Active on your server.')

client.run('OTcxMjY2NDgyMzc1ODg0ODEw.GjDLGt.wKt86c1yEVC9M-JuDCU1M75zjezsywhtLcxCo0')