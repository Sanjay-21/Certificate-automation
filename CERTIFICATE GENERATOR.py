from PIL import Image, ImageFont, ImageDraw
import pandas as pd
df=pd.read_csv("NAME.csv")  #file containing participants' details 
for i in range(308):
    my_image = Image.open("temp.png")   #certificate template
    title_font = ImageFont.truetype('GOTHICB.ttf', 61)  #Font name and size
    title_text = df.iloc[i,0].rstrip()  #Paticipant's name
    ascent, descent = title_font.getmetrics()
    text_width = title_font.getmask(title_text).getbbox()[2]
    text_height = title_font.getmask(title_text).getbbox()[3] + descent
    print(title_text)
    image_editable = ImageDraw.Draw(my_image)
    length=text_width/2
    x=(846-length)  #x coordinate (846 represents the middle of a name) 
    image_editable.text((x,455), title_text, (0, 0, 0), font=title_font) #y coordinate=455
    my_image.save("./certificates/"+title_text +".jpg")