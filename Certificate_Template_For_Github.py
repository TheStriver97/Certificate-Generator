from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import os
import fsspec

filename = r"Your_CSV_File_Path"

df = pd.read_csv(filename, encoding = "utf-8")

font = ImageFont.truetype('Charm-Bold.ttf',60)

for index,j in df.iterrows():
	#print(index)
	#print(j[0])
	W = 2000
	H = 1414
	img = Image.open("Your_Image_Name.jpg")
	draw = ImageDraw.Draw(img)
	message = text='{}'.format(j[0])
	_, _, w, h = draw.textbbox((0, 0), message, font=font)
	draw.text(((W-w)/2, (H-h)/2),text='{}'.format(j[0]),fill=(0,0,0),font=font,align='Left')
	img.save('output_certificate/{}.jpg'.format(j[0]))