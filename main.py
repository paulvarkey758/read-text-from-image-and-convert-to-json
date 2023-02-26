import pytesseract
from PIL import Image
import json

image=Image.open('table.png')
text=pytesseract.image_to_string(image)
print(text)

text=text.split("\n")
print(text)
new_text=text[1:]
if new_text[-1] == "":
    new_list=[i.split(" ") for i in new_text[:-1] if i != ""]
else:
    new_list=[i.split(" ") for i in new_text if i != ""]
print(new_list)
out_list=[]
data={}
for i in new_list:
    data['person']=i[0]
    data['age']=i[1]
    out_list.append(data)
    data={}

print(out_list)

out_list=json.dumps(out_list)

json_file=open("new.json",'w+')
json_file.write(out_list)
json_file.close()

