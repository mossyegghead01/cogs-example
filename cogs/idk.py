import discord
from discord.ext import commands
import time

class Idk(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('im ready!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

def setup(client):
    client.add_cog(Idk(client))