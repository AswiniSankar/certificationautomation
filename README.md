# certificateautomation - version1
To automate a e certificate by just giving a csv file and certificate template as input using python 

pre-request to generate automation of e-certificate

1. create a folder in which it should contain csv file , certificate template and another empty folder which will used to store the generated certificates.
                      mainfolder
                         1. generator python code
                         2. csv file which contains student names
                         3. certificate template in jpg format
                         4. empty folder 
2. install PI,pillow,pandas by using commands.
                    1.pip3 install pandas
                    2.pip install PI
                    3.pip install pillow
3. make the coordinates where you want to write the student name in tha certificate template. this can by achived by using puautogui.position() which gives the cursor position in the coordinate form.

# certificateautomation - version2

In version 2 generated certificates are sent to the respective candidate email id. For that import packages like imghdr,smtplib and EmailMessage.steps involved are

1. Don’t save the certificate images in a separate folder rather than save it in the current folder. 
2. A message is created using EmailMessage(), a newly created message is stored with sender, receiver, subject, body content.
3. For each iteration the saved images are open in the read in binary format and append the image with a message object.
4. By passing a message to the smtp.send_message() function, the certificate is sent to the respective candidate.

