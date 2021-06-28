from PIL import ImageDraw, ImageFont
from PIL import Image
import pandas as pd
import os

df = pd.read_csv('list2.csv')
font_path = '//../fonts/DroidSerif-Bold.ttf'  #locate .ttf - this command used to locate the installed font in your system from that various select one font path
assert os.path.isfile(font_path) #check for the font path
font = ImageFont.truetype(font_path, 80) #here font size is 80
for index, j in df.iterrows(): #index is represents each row and j represents cell value 
    # print(index)
    img = Image.open('certificate.jpg') #certificate template  is opened 
    draw = ImageDraw.Draw(img) #ready to write in the template
    draw.text(xy=(900, 765), text='{}'.format(j['name']), fill=(0, 0, 255), font=font) #fill is for font color and font is for font type
    draw.text(xy=(300, 765), text='{}'.format(j['cd']), fill=(0, 0, 255), font=font)# here the coordinates are given to write the text
    draw.text(xy=(300, 1000), text='{}'.format(j['ceo']), fill=(0, 0, 255), font=font)
    img.save('pictures/{}.jpg'.format(j['name'])) #writen certificates are saved in the picture folder with the name of student itself
