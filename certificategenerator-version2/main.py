import imghdr
from PIL import ImageDraw, ImageFont
from PIL import Image
import pandas as pd
import os
import smtplib, csv
from email.message import EmailMessage

df = pd.read_csv('list3.csv')            		# csv reader
cd = "Adora" 						# dummy course director name
ceo = "Pam"  						# dummy ceo name
font_path = '/home/../../pycharm-community-2021.1.2/jbr/lib/fonts/DroidSerif-Bold.ttf'  # path where font get installed
assert os.path.isfile(font_path)  			# check for the path
font = ImageFont.truetype(font_path, 80)  		# assigning size for the font
Sender_Email = "senderemail@gmail.com"
Password = input('Enter your email account password: ')
with smtplib.SMTP_SSL('smtp.gmail.com',
                      465) as smtp: 			 # since with is used to open the ssl need not to close at the end it will automatically get closed
    smtp.login(Sender_Email, Password)  		 # if mail id and password get match the email will  get open
    for index, j in df.iterrows():  			 # iterating each row in csv file
        # print(index)

        img = Image.open('certificate.jpg')  		 # open template certificate

        draw = ImageDraw.Draw(img)           		 # ready to write in the template
        draw.text(xy=(900, 765), text='{}'.format(j['name']), fill=(0, 0, 255), font=font)   		# to write name of candidate
        draw.text(xy=(300, 765), text='{}'.format(cd), fill=(0, 0, 255), font=font)  			# to write course director name
        draw.text(xy=(300, 1000), text='{}'.format(ceo), fill=(0, 0, 255), font=font)  			# to write ceo name
        img.save('{}.jpg'.format(j['name']))  								# writen images is save with the candidate name itself in current folder

        Reciever_Email = '{}'.format(j['email'])  							# reciever mail id is taken from the csv file itself
        newMessage = EmailMessage()

        # adding essential details for sending mail
        newMessage['Subject'] = "participating e - certificate"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content(
            'dear {},\n\n Hope you and your family good, Thank you for participating in our college hackathon programme. we encourage your effort and send this e-certifiacte to you.Once agian thank you for your valuable time stay and home stay safe\n\n                                         Thanking You\n\nwith regards,\nManeesh\nchairman of IT department'.format(
                j['name']))

        # images is open
        with open('{}.jpg'.format(j['name']), 'rb') as f:
            image_data = f.read()  									# to read the image
            image_type = imghdr.what(f.name)  								# to know the type of image like png/jpeg/gif
            image_name = f.name  									# to know image name

        # opened image is attached with the message
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        smtp.send_message(newMessage)  # to send mail
