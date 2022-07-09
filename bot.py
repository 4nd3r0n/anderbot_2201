from configparser import ConfigParser
from twitchio.ext import commands
from playsound import playsound
from random import randint as rd

import time
import os

file = ['config', 'commands']
config = ConfigParser()
config.read(file)

cooldown = False

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token = config['settings']['token'],
            prefix = config['settings']['prefix'],
            initial_channels = [config['settings']['channels']]
        )

    async def event_ready(self):
        print('The AnderBot_2201 has successfully started\n')
        # print(f'Logged in as | {self.nick}')
        # print(f'User id is | {self.user_id}\n')

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send('pong')

    @commands.command()
    async def comandos(self, ctx: commands.Context):
        await ctx.send(f"{config['context']['comandos']}")

    @commands.command()
    async def hola(self, ctx: commands.Context):
        await ctx.send(f"!!Hola {ctx.author.name} {config['context']['saludo']}!!")

    @commands.command()
    async def meow(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !meow')
        playsound(f'assets/sounds/meow/meow-{rd(1, 5)}.mp3')

    @commands.command()
    async def fart(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !fart')
        playsound(f'assets/sounds/fart/fart-{rd(1, 4)}.mp3')

    @commands.command()
    async def creeper(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !creeper')
        playsound(f'assets/sounds/minecraft/creeper.mp3')

    @commands.command()
    async def boom(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !boom')
        playsound(f'assets/sounds/memes/boom.mp3')

    @commands.command()
    async def p(self, ctx: commands.Context):
        os.system('cmus-remote -u')
    
    @commands.command()
    async def next(self, ctx: commands.Context):
        os.system("cmus-remote -n")

    @commands.command()
    async def back(self, ctx: commands.Context):
        os.system("cmus-remote -r")

    @commands.command()
    async def v25(self, ctx: commands.Context):
        os.system("cmus-remote -v 25%")
    
    @commands.command()
    async def v30(self, ctx: commands.Context):
        os.system("cmus-remote -v 30%")

    @commands.command()
    async def v50(self, ctx: commands.Context):
        os.system("cmus-remote -v 50%")

    @commands.command()
    async def v60(self, ctx: commands.Context):
        os.system("cmus-remote -v 60%")

bot = Bot()
bot.run()