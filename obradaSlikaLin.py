import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'slika1.jpg',
    'slika2.jpg',
    'slika3.jpg',
    'slika4.jpg',
    'slika5.jpg',
    'slika6.jpg',
    'slika7.jpg',
    'slika8.jpg',
]

t1 = time.perf_counter()




def obradi_sliku(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.save(f'obradjene/{img_name}')
    print(f'{img_name} je obradjena...')


for img in img_names:
    obradi_sliku(img)


t2 = time.perf_counter()

print(f'Zavrseno u {t2-t1} sekundi')
