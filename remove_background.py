# Remove Background of Images
# pip install rembg
# pip install pillowfrom rembg import remove as rem
from PIL import Image
def Remove_bg(img):
    output = "removed_bg.png" 
    input = Image.open(img)
    output_img = rem(input)
    output_img.save(output)
    
Remove_bg('input.png')