# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:52:24 2021

GOOGLE Text recognition API Check
"""

import os, io
from google.cloud import vision
from google.cloud import vision_v1
import pandas as pd
from PIL import Image


# Opens a image in RGB mode
im = Image.open(r'C:\Users\Visitor\Desktop\DIGICOMMS\APITest\handwriting2.jpg')

#Crop Image First Division 
left = 100
top = 200
right = 1160
bottom = 235

im1 = im.crop((left, top, right, bottom))
im1.show()
im1.save(r'C:\Users\Visitor\Desktop\DIGICOMMS\APITest\header1.jpg')

#Crop Image Second Division
left = 100
top = 304
right = 1160
bottom = 670

im1 = im.crop((left, top, right, bottom))
im1.show()
im1.save(r'C:\Users\Visitor\Desktop\DIGICOMMS\APITest\header2.jpg')


#Set Client 
request = vision_v1.GetProductSetRequest(name="name")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/Visitor/Desktop/DIGICOMMS/GoogVis.json'
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'C:/Users/Visitor/Desktop/DIGICOMMS/APITest'
#Read Image Here 
IMAGE_PATH = 'header2.jpg'
FILE_PATH = os.path.join(FOLDER_PATH,IMAGE_PATH)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.document_text_detection(image=image)
docText = response.full_text_annotation.text

print(docText)

#Split String 
str_item = docText.splitlines(0)

#Create Dataframe 
data = {'No': [],
	'Item_ID': [],
	'Nama_Barang': [],
    'Qty': [],
    'Harga': [],
    'Jumlah': []
    }


df = pd.DataFrame(data)

#Separate Documents into Pandas Dataframes 
i = 0
datasize = len(str_item)

for i in range(0, datasize, 6):
    new_row = {'No':str_item[i], 
               'Item_ID':str_item[i+1], 
               'Nama_Barang':str_item[i+2],
               'Qty':str_item[i+3],
               'Harga': str_item[i+4],
               'Jumlah': str_item[i+5],
               }
    
    df = df.append(new_row, ignore_index=True)

    
df.to_excel(r'C:\Users\Visitor\Desktop\invoice_df.xlsx', index = False)




