#installation
# pip install pdf2image
# pip install poppler-utils
################################################

# import module
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
poppler_path=r'C:\bhuvi\Rumble with python\poppler-0.68.0_x86\poppler-0.68.0\bin'
images = convert_from_path(r'C:\bhuvi\Rumble with python\pdf_2_img\statement.pdf',500,poppler_path=poppler_path)
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')