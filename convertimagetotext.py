import pytesseract        
from PIL import Image      
import glob

with open('extracttextfromimages.txt', mode ='w') as f:
    extensions = ('*.png', '*.jpg', '*.jpeg' , '*.gif')    
    files_list = []
    for ext in extensions:
        files_list.extend(glob.glob(ext))        
    f.write(str(files_list))
    f.write("\n\n")

 
    for eachimage in files_list:
        
        img = Image.open(eachimage)             
        f.write("{0}".format(str(eachimage)))
    

        pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
        result = pytesseract.image_to_string(img)   
        f.write(result)      