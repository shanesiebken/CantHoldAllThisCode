from PIL import Image, ImageFilter
from PIL import GifImagePlugin
import requests
import math, random
import glob, os

##size = 128, 128
##
##for infile in glob.glob("*.png"):
##    file, ext = os.path.splitext(infile)
##    im = Image.open(infile)
##    im.thumbnail(size)
##    im.save(file + ".thumbnail", "PNG")
X = [226,160,280,198,255,280,160]
Y = [515,530,540,550,550,585,645]
X2 = [310,220]
Y2 = [595,790]
leng = len(X)
leng2 = len(X2)
rot = []
rot2 = []

one = Image.open("Base.png")
two = Image.open("Arm.png")
pog = Image.open("wee.gif")
##for i in range(leng):
##    print(i)
##    one.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(random.randint(0,360), Image.BICUBIC, expand=1),(X[i],Y[i]))
##comp2 = Image.alpha_composite(one,two)
##for i in range(leng2):
##    print(i)
##    comp2.alpha_composite(pog.resize((70,70), Image.LANCZOS).rotate(random.randint(0,360), Image.BICUBIC, expand=1),(X2[i],Y2[i]))
##comp2.show()
##comp2.save('memes5.png')

for i in range(leng):
    rot.append(random.randint(0,360))
    print(rot[i])
for i in range(leng2):
    rot2.append(random.randint(0,360))
    print(rot2[i])

imageObject = pog
##print(imageObject.info)
isThisGif = imageObject.is_animated
totalFrames = imageObject.n_frames
gifDuration = imageObject.info['duration']

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

print(exists("https://cdn.discordapp.com/emojis/586284301725990922.png"))
print(exists("https://cdn.discordapp.com/emojis/586284301725990922.gif"))

images = []

for frame in range(0, totalFrames, 1):
    onec = one.copy()
    twoc = two.copy()
    pogc = imageObject
    pogc.seek(frame)
    pogc2 = pogc.copy().convert('RGBA')
    ##pogc.show()
    ##pogc2.show()
    for i in range(leng):
        print(i)
        onec.alpha_composite(pogc2.resize((70,70), Image.LANCZOS).rotate(rot[i], Image.BICUBIC, expand=1),(X[i],Y[i]))
    comp2 = Image.alpha_composite(onec,twoc)
    for i in range(leng2):
        print(i)
        comp2.alpha_composite(pogc2.resize((70,70), Image.LANCZOS).rotate(rot2[i], Image.BICUBIC, expand=1),(X2[i],Y2[i]))
    ##comp2.show()
    images.append(comp2)
images[0].save('test3.gif', save_all=True, append_images=images[1:], duration=gifDuration, loop=0, optimize=False)



##images = []
##
##for i in range(0, 180, 1):
##    ##im = pog.resize((100,100), Image.LANCZOS).rotate(i*2,Image.BICUBIC)
##    im = pog.rotate(i*2,Image.BICUBIC)
##    testy = blank2.copy()
##    testy.alpha_composite(im)
##    images.append(testy)
##images[0].save('test2.gif', save_all=True, append_images=images[1:], duration=36, loop=0, optimize=False)


