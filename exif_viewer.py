from PIL import Image
from PIL.ExifTags import TAGS
import sys

img_path = str(input('Enter path to the image: '))

try:
    img = Image.open(img_path)

    for tag, value in img.getexif().items():
        tag_name = TAGS.get(tag)

        if tag_name == 'MakerNote' or tag_name =='UserComment':
            continue

except:
    print('\n[-]Invalid file path!!!')
    sys.exit()