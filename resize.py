import os
import cv2
import numpy as np
from tqdm import tqdm
path = 'images'
RESIZE = (640, 640)


def main():
    for i in tqdm(os.listdir(path)):
        img = os.path.join(path, i)
        label = os.path.join('labels', i[:i.find('.')] + '.jpg.txt')
        img = cv2.imread(img)
        targetSize = 640
        bb1 = []
        texts = []
        with open(label, 'r', encoding='utf8') as f:
            for line in f.readlines():
                x1, y1, x2, y2, x3, y3, x4, y4, text = line.split(",")
                x1, y1, x2, y2, x3, y3, x4, y4 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4)
                bb1.append([[int(x1), int(y1)], [int(x2), int(y2)], [int(x3), int(y3)], [int(x4), int(y4)]])
                texts.append(text)
        y_ = img.shape[0]
        x_ = img.shape[1]
        x_scale = targetSize / x_
        y_scale = targetSize / y_
        new_bb = []
        for n in range(len(bb1)):
            for j in range(len(bb1[n])):
                bb1[n][j] = np.multiply(bb1[n][j], [x_scale, y_scale])
                bb1[n][j] = np.asarray(bb1[n][j], dtype='int64')

        with open('resize_labels/{}.gt'.format(i[:i.find('.')]), 'w', encoding='utf8') as f:
            for box, text in zip(bb1, texts):
                f.write(
                    '{},{},{},{},{},{},{},{},{}'.format(str(box[0][0]), str(box[0][1]),
                                                        str(box[1][0]), str(box[1][1]),
                                                        str(box[2][0]), str(box[2][1]),
                                                        str(box[3][0]), str(box[3][1]),
                                                        text))
        with open('resize_labels/{}.jpg.txt'.format(i[:i.find('.')]), 'w', encoding='utf8') as f:
            for box, text in zip(bb1, texts):
                f.write(
                    '{},{},{},{},{},{},{},{},{}'.format(str(box[0][0]), str(box[0][1]),
                                                        str(box[1][0]), str(box[1][1]),
                                                        str(box[2][0]), str(box[2][1]),
                                                        str(box[3][0]), str(box[3][1]),
                                                        text))
        img = cv2.resize(img, RESIZE)
        cv2.imwrite('resize_images/{}.jpg'.format(i[:i.find('.')]), img)


if __name__ == '__main__':
    main()