from configparser import ConfigParser
from twitchio.ext import commands
from playsound import playsound
from random import randint as rd
from gtts import gTTS

import pygame
import time
import os

file = ['config', 'commands']
config = ConfigParser()
config.read(file)

pygame.init()
pygame.mixer.init()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token = config['settings']['token'],
            prefix = config['settings']['prefix'],
            initial_channels = [config['settings']['channels']]
        )

    async def event_ready(self):
        print('\nThe AnderBot_2201 has successfully started')
        print(f'Logged in as | {self.nick}\n')
        # print(f'User id is | {self.user_id}\n')

    @commands.command()
    @commands.cooldown( 1, 5, commands.Bucket.user)
    async def ping(self, ctx: commands.Context):
        print(f'{ctx.author.name} has use !ping')
        await ctx.send('pong')

    @commands.command()
    @commands.cooldown( 1, 1, commands.Bucket.user)
    async def comandos(self, ctx: commands.Context):
        print(f'{ctx.author.name} has use !commands')
        await ctx.send(f"{config['context']['comandos']}")

    @commands.command()
    @commands.cooldown( 1, 3, commands.Bucket.user)
    async def hola(self, ctx: commands.Context):
        print(f'{ctx.author.name} has use !hola')
        await ctx.send(f"!!Hola {ctx.author.display_name} {config['context']['saludo']}!!")

    @commands.command()
    @commands.cooldown( 1, 15, commands.Bucket.user)
    async def meow(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !meow')
        sound = pygame.mixer.Sound(f'assets/sounds/meow/meow-{rd(1, 5)}.mp3')
        sound.set_volume(0.4)
        sound.play()

    @commands.command()
    @commands.cooldown( 1, 30, commands.Bucket.user)
    async def fart(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !fart')
        sound = pygame.mixer.Sound(f'assets/sounds/fart/fart-{rd(1, 4)}.mp3')
        sound.set_volume(0.4)
        sound.play()

    @commands.command()
    @commands.cooldown( 1, 120, commands.Bucket.user)
    async def creeper(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !creeper')
        sound = pygame.mixer.Sound('assets/sounds/minecraft/creeper.mp3')
        sound.play()

    @commands.command()
    @commands.cooldown( 1, 90, commands.Bucket.user)
    async def cave(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !cave')
        sound = pygame.mixer.Sound(f'assets/sounds/minecraft/cave/cave-{rd(1, 19)}.mp3')
        sound.play()

    @commands.command()
    @commands.cooldown( 1, 15, commands.Bucket.user)
    async def boom(self, ctx: commands.Context):
        print(f'{ctx.author.name} has played !boom')
        sound = pygame.mixer.Sound('assets/sounds/memes/boom.mp3')
        sound.set_volume(0.6)
        sound.play()

    @commands.command()
    async def p(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !p')
            os.system('cmus-remote -u')
        else:
            print(f'{ctx.author.name} has use !p but is not mod')
    
    @commands.command()
    async def next(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !next')
            os.system("cmus-remote -n")
        else:
            print(f'{ctx.author.name} has use !next but is not mod')

    @commands.command()
    async def back(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !back')
            os.system("cmus-remote -r")
        else:
            print(f'{ctx.author.name} has use !back but is not mod')

    @commands.command()
    async def v25(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !v25')
            os.system("cmus-remote -v 25%")
        else:
            print(f'{ctx.author.name} has use !v25 but is not mod')

    @commands.command()
    async def v30(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !v30')
            os.system("cmus-remote -v 30%")
        else:
            print(f'{ctx.author.name} has use !v30 but is not mod')

    @commands.command()
    async def v50(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !v50')
            os.system("cmus-remote -v 50%")
        else:
            print(f'{ctx.author.name} has use !v50 but is not mod')

    @commands.command()
    async def v60(self, ctx: commands.Context):
        if ctx.author.is_mod:
            print(f'{ctx.author.name} has use !v60')
            os.system("cmus-remote -v 60%")
        else:
            print(f'{ctx.author.name} has use !v60 but is not mod')

    async def event_message(self, message):
        if message.echo:
            return
        if config['settings']['prefix'] in message.content:
            pass
        else:
            # tts = gTTS(f'{message.author.display_name} dice: {message.content}', lang='es', tld='com')
            tts = gTTS(f'{message.content}', lang='es', tld='com')
            tts.save('assets/audio/audio.mp3')
            playsound('assets/audio/audio.mp3')
            os.remove('assets/audio/audio.mp3')
            pass
        await self.handle_commands(message)

    async def event_command_error(self, ctx, error: Exception) -> None:
        print(error)

bot = Bot()
bot.run()