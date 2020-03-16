from PIL import Image, ImageFilter, GifImagePlugin, ImageSequence
import os, glob
import math, random
import io
import discord
import requests
import moviepy.editor as mp
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Emoji
from discord import File
from dotenv import load_dotenv
from pygifsicle import optimize
from requests_toolbelt import MultipartEncoder
##from imgurpython import ImgurClient

X = [226,160,280,198,255,280,160]
Y = [515,530,540,550,550,585,645]
X2 = [310,220]
Y2 = [595,790]
leng = len(X)
leng2 = len(X2)
rot = []
rot2 = []
for i in range(leng):
    rot.append(random.randint(0,360))
    ##print(rot[i])
for i in range(leng2):
    rot2.append(random.randint(0,360))
    ##print(rot2[i])
    
one = Image.open("Base.png")
two = Image.open("Arm.png")
short = Image.open("BaseAwooga.png")
shorts = False

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def download(urll,gifProcess):
        r = requests.get(urll, allow_redirects=True)
        if gifProcess:
            open('whutt.gif', 'wb').write(r.content)
        else:
            open('whutt.png', 'wb').write(r.content)
        r.close()

##def authenticateImgur():
##	client_id = os.getenv('IMGUR_API_ID')
##	client_secret = os.getenv('IMGUR_API_SECRET')
##	client = ImgurClient(client_id, client_secret)

##	# Authorization flow, pin example (see docs for other auth types)
####	authorization_url = client.get_auth_url('pin')
##
####	print("Go to the following URL: {0}".format(authorization_url))
##
##	# Read in the pin, handle Python 2 or 3 here.
####	pin = input("Enter pin code: ")
##
##	# ... redirect user to `authorization_url`, obtain pin (or code or token) ...
####	credentials = client.authorize(pin, 'pin')
####	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
##	access_token = os.getenv('ACCESS_TOKEN')
##	refresh_token = os.getenv('REFRESH_TOKEN')
##	client.set_user_auth(access_token, refresh_token)
##
####	print("Authentication successful! Here are the details:")
####	print("   Access token:  {0}".format(credentials['access_token']))
####	print("   Refresh token: {0}".format(credentials['refresh_token']))
##
##	return client

##def upload_png(gif):
##    client_id = os.getenv('IMGUR_API_ID')
##    client_secret = os.getenv('IMGUR_API_SECRET')
##    if client_id is None or client_secret is None:
##        print('Cannot upload - could not find IMGUR_API_ID or IMGUR_API_SECRET environment variables')
##        return
##    ##client = ImgurClient(client_id, client_secret)
##    client = authenticateImgur()
##    print("wee")
##    response = client.upload_from_path(gif, anon=False)
##    text = ('File uploaded: {}'.format(response['link']))
##    return text

def get_token():
    payload = {
    'grant_type':'client_credentials',
    'client_id':os.getenv('GFYCAT_CLIENT_ID'),
    'client_secret':os.getenv('GFYCAT_CLIENT_SECRET')
    }

    url = "https://api.gfycat.com/v1/oauth/token"
    r = requests.post(url, data=str(payload), headers={'User-Agent': "Slow down bot"})

    response = r.json()

    access_token = response["access_token"]
    print(access_token)
    return access_token

def upload_gif(sub_id):
    print("uploading")
    title = "please work..."

    # get gfyname
    url = "https://api.gfycat.com/v1/gfycats"
    headers = {"Authorization": "Bearer " + get_token(), 'User-Agent': "Slow down bot",
                'Content-Type': 'application/json'}

    params = {}

    if title:
        params["title"] = title

    r = requests.post(url, headers=headers, data=str(params))
    print(r.text)

    metadata = r.json()

    url = "https://filedrop.gfycat.com"
    with open("S:/Image Stuff/testy/CantHoldAllThese.gif", 'rb') as f:
        files = {"key": metadata["gfyname"], "file": (metadata["gfyname"], f, "video/mp4")}
        m = MultipartEncoder(fields=files)
        r = requests.post(url, data=m, headers={'Content-Type': m.content_type, 'User-Agent': "Slowing down gifs"})
    url = "https://api.gfycat.com/v1/gfycats/fetch/status/" + metadata["gfyname"]
    headers = {'User-Agent': "Slowing down gifs"}
    print("waiting for encode...", end=" ")
    r = requests.get(url, headers=headers)
    ticket = r.json()
    print(ticket)
    print(url)
    print(metadata["gfyname"])

    # Sometimes we have to wait
    percentage = 0
    for i in range(457):
        if ticket["task"] == "encoding":
            time.sleep(7)
            r = requests.get(url, headers=headers)
            ticket = r.json()
            print(ticket)
            if float(ticket.get('progress', 0)) > percentage:
                percentage = float(ticket['progress'])
                print(percentage, end=" ")
            else:
                break


    # os.system('rm temp/slow-{}.mp4'.format(sub_id))
    return metadata["gfyname"]

bot = commands.Bot(command_prefix='!')

@bot.command(name='emoji')
async def nine_nine(ctx, test):
        start = test.find(":",3)+1
        stri2 = test[start:]
        stri3 = stri2[:-1]
        if stri3 == '681244980593164336':
            shorts = True
        else:
            shorts = False
        if shorts:
            one1 = short.copy()
        else:
            one1 = one.copy()
        two2 = two.copy()
        ##await ctx.send("https://cdn.discordapp.com/emojis/"+stri3+".png")
        url = "https://cdn.discordapp.com/emojis/"+stri3
        if exists(url+".gif"):
            gifProcess = True
            pog = download(url+".gif",gifProcess)  
        else:
            gifProcess = False
            pog = download(url+".png",gifProcess)
            pog = Image.open("whutt.png")
            ##pog.save("whatif.png")
        if gifProcess:
            images = []
            pog = Image.open("whutt.gif")
            ##pog.show()
            totalFrames = pog.n_frames
            gifDuration = pog.info['duration']
            if totalFrames < 333:
                for frame in range(0, totalFrames, 1):
                    onec = one.copy()
                    twoc = two.copy()
                    pogc = pog
                    pogc.seek(frame)    
                    pogc2 = pogc.copy().convert('RGBA')
                    ##pogc.show()
                    ##pogc2.show()
                    for i in range(leng):
                        ##print(i)
                        onec.alpha_composite(pogc2.resize((70,70), Image.LANCZOS).rotate(rot[i], Image.BICUBIC, expand=1),(X[i],Y[i]))
                    comp2 = Image.alpha_composite(onec,twoc)
                    for i in range(leng2):
                        ##print(i)
                        comp2.alpha_composite(pogc2.resize((70,70), Image.LANCZOS).rotate(rot2[i], Image.BICUBIC, expand=1),(X2[i],Y2[i]))
                    ##comp2.show()
                    print(frame)
                    images.append(comp2)
                images[0].save('CantHoldAllThese.gif', save_all=True, append_images=images[1:], duration=gifDuration, loop=0, optimize=True)
                optimize("CantHoldAllThese.gif")
                print(os.path.getsize('CantHoldAllThese.gif'))
                await ctx.channel.send("http://gfycat.com/"+upload_gif(1))
                ##await ctx.channel.send(file=discord.File('CantHoldAllThese.gif'))
            else:
                await ctx.channel.send("Emoji too long")
        else:
            for i in range(leng):
                ##print(i)
                one1.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(rot[i], Image.BICUBIC, expand=1),(X[i],Y[i]))
            comp2 = Image.alpha_composite(one1,two2)
            for i in range(leng2):
                comp2.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(rot2[i], Image.BICUBIC, expand=1),(X2[i],Y2[i]))
            ##comp2.show()
            comp2.save('CantHoldAllThese.png')
            await ctx.channel.send(file=discord.File('CantHoldAllThese.png'))
            ##await ctx.channel.send(upload_png('CantHoldAllThese.png'))


bot.run(TOKEN)
