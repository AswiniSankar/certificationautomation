# certificationautomation
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

