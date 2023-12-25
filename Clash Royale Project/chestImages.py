from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen
import API
import itertools

chestInfo = API.upcomingChest
chestNumber = API.chestNumber

canvas = Image.new('RGBA', size=(1472, 338), color=(255, 255, 255, 0))

def imaging():
    global n
    global m
    global img
    global o
    global p

    filler_color = (255,255,255)
    stroke_color = (0,0,0)
    font = ImageFont.truetype(font="c:/Users/varun/Downloads/komika_axis/KOMIKAX_.ttf", size=42)

    drawer = ImageDraw.Draw(canvas)

    img = img.resize(size=(174, 159))
    if int(x) < 8:
        canvas.paste(img, box=(0+n, 0))
        n += 184
        if int(x) == 0:
            drawer.text((70 + o, 100), "Next", fill=filler_color, font=font, stroke_width=3, stroke_fill=stroke_color)
            o += 184
        else:
            drawer.text((130 + o, 100), str(x), fill=filler_color, font=font, stroke_width=3, stroke_fill=stroke_color)
            o += 184
    elif 8 <= int(x) and int(x) <= 1000:
        canvas.paste(img, box=(0+m, 169))
        m+= 184
        if x >= 100:
            drawer.text((130 + p, 269), str(x), fill=filler_color, font=font, stroke_width=3, stroke_fill=stroke_color)
            p += 184
        else:
            drawer.text((130 + p, 269), str(x), fill=filler_color, font=font, stroke_width=3, stroke_fill=stroke_color)
            p += 174
        
n = 0
m = 0
o = 0
p = 0

for i, x in itertools.zip_longest(chestInfo, chestNumber):
    if i == "Wooden Chest":
        chestUrl = "chest_images/Wooden_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Silver Chest":
        chestUrl = "chest_images/Silver_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Golden Chest":
        chestUrl = "chest_images/Golden_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Magical Chest":
        chestUrl = "chest_images/Magical_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Giant Chest":
        chestUrl = "chest_images/Giant_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Mega Lightning Chest":
        chestUrl = "chest_images/MegaLightningChest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Epic Chest":
        chestUrl = "chest_images/EpicChest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Legendary Chest":
        chestUrl = "chest_images/LegendChest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Gold Crate":
        chestUrl = "chest_images/Gold_Crate.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Plentiful Gold Crate":
        chestUrl = "chest_images/Plentiful_Gold_Crate.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Overflowing Gold Crate":
        chestUrl = "chest_images/Overflowing_Gold_Crate.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    elif i == "Royal Wild Chest":
        chestUrl = "chest_images/Royal_Wild_Chest.webp"
        img = Image.open(chestUrl)
        imaging()
        print("done")
    else:
        ValueError("Wrong chest naming: check chestImages.py for the error")

canvas.save("chest.png")