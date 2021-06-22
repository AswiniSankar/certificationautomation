from PIL import ImageDraw, ImageFont
from PIL import Image
import pandas as pd
import os

df = pd.read_csv('list3.csv')
font_path = '//../fonts/DroidSerif-Bold.ttf'
assert os.path.isfile(font_path)
font = ImageFont.truetype(font_path, 80)
for index, j in df.iterrows():
    # print(index)
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(900, 765), text='{}'.format(j['name']), fill=(0, 0, 255), font=font)
    draw.text(xy=(300, 765), text='{}'.format(j['cd']), fill=(0, 0, 255), font=font)
    draw.text(xy=(300, 1000), text='{}'.format(j['ceo']), fill=(0, 0, 255), font=font)
    img.save('pictures/{}.jpg'.format(j['name']))
