import os
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

path = 'labels'


def main():
    font = ImageFont.truetype('fonts/KosugiMaru-Regular.ttf', 20)
    for i in tqdm(os.listdir(path)):
        label = os.path.join(path, i)
        img = os.path.join('images', i[:i.find('.')]  + '.jpg')
        img = Image.open(img)
        draw = ImageDraw.Draw(img)
        with open(label, 'r', encoding='utf8') as f:
            for line in f.readlines():
                x1, y1, x2, y2,x3, y3, x4, y4, text = line.split(",")
                x1, y1, x2, y2, x3, y3, x4, y4 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4)
                draw.rectangle(((int(x1), int(y1)), (int(x3), int(y3))), outline=(0,0,250), width=2)
                draw.text((int(x1), int(y1)), text, font=font, fill=(0, 0, 0))
        img.save('result/{}.jpg'.format(i[:i.find('.')]))


if __name__ =='__main__':
    main()

