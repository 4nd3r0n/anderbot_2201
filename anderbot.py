import os
import time

from twitchio.ext import commands
from configparser import ConfigParser
from playsound import playsound
from random import randint as rd

file = 'config'
config = ConfigParser()
config.read(file)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token = config['settings']['token'],
            prefix = config['settings']['prefix'],
            initial_channels = [config['settings']['channels']]
        )

    async def event_ready(self):
        print('The AnderBot_2201 has successfully started\n')
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}\n')

    @commands.command()
    async def comandos(self, ctx: commands.Context):
        await ctx.send('Todos los comados están en el Server de Discord "Link"')

    @commands.command()
    async def hola(self, ctx: commands.Context):
        await ctx.send(f'¡¡Hola {ctx.author.name}!!')

    @commands.command()
    async def ban(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} a baneado a {ctx.author.name}')

    @commands.command()
    async def meow(self, ctx: commands.Context):
        playsound(f'assets/sounds/meow/meow-{rd(1, 3)}.mp3')

    @commands.command()
    async def amongus(self, ctx: commands.Context):
        playsound(f'assets/sounds/amongus/amongus.mp3')


bot = Bot()
bot.run()
