# bot.py
from PIL import Image, ImageFilter
import os, glob
import math, random
import time

import discord
import requests
import io
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Emoji
from discord import File
from dotenv import load_dotenv

X = [226,160,280,198,255,280,160]
Y = [515,530,540,550,550,585,645]
X2 = [310,220]
Y2 = [595,790]
leng = len(X)
leng2 = len(X2)
one = Image.open("Base.png")
two = Image.open("Arm.png")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



bot = commands.Bot(command_prefix='!')

@bot.command(name='emoji')
async def nine_nine(ctx, test):
    one1 = one.copy()
    two2 = two.copy()
    start = test.find(":",3)+1
    stri2 = test[start:]
    stri3 = stri2[:-1]
    ##await ctx.send("https://cdn.discordapp.com/emojis/"+stri3+".png")
    url = "https://cdn.discordapp.com/emojis/"+stri3+".png"
    r = requests.get(url, stream=True)
    r.raise_for_status()
    r.raw.decode_content = True  # Required to decompress gzip/deflate compressed responses.
    with Image.open(r.raw) as img:
        ##img.show()
        ##img.save('emoji.png')
        pog = img.copy()
    r.close()
    for i in range(leng):
        ##print(i)
        one1.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(random.randint(0,360), Image.BICUBIC, expand=1),(X[i],Y[i]))
    comp2 = Image.alpha_composite(one1,two2)
    for i in range(leng2):
        comp2.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(random.randint(0,360), Image.BICUBIC, expand=1),(X2[i],Y2[i]))
    ##comp2.show()
    comp2.save('memes6.png')
    await ctx.channel.send(file=discord.File('memes6.png'))


bot.run(TOKEN)
