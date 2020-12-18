import os
import cv2
import numpy as np
from tqdm import tqdm
import random

path = 'images'


def rotate(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def rotate_box(image, bb, angle):
    new_bb = list(bb)
    (h, w) = image.shape[:2]
    (cx, cy) = (w // 2, h // 2)
    for i,coord in enumerate(bb):
        # opencv calculates standard transformation matrix
        M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)
        # Grab  the rotation components of the matrix)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cx
        M[1, 2] += (nH / 2) - cy
        # Prepare the vector to be transformed
        v = [coord[0],coord[1],1]
        # Perform the actual rotation and return the image
        calculated = np.dot(M,v)
        calculated = calculated.astype('int64')
        new_bb[i] = [calculated[0],calculated[1]]
    return new_bb


def main():
        for i in tqdm(os.listdir(path)):
            angle = random.randrange(-60,60)
            img = os.path.join(path, i)
            label = os.path.join('labels', i[:i.find('.')]  + '.jpg.txt')
            img = cv2.imread(img)
            targetSize = 640
            bb1 = []
            texts = []
            with open(label, 'r', encoding='utf8') as f:
                for line in f.readlines():
                    x1, y1, x2, y2, x3, y3, x4, y4, text = line.split(",")
                    x1, y1, x2, y2, x3, y3, x4, y4 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4)
                    bb1.append([(int(x1), int(y1)),(int(x2), int(y2)), (int(x3), int(y3)), (int(x4), int(y4))])
                    texts.append(text)
            new_img = rotate(img, angle)
            y_ = new_img.shape[0]
            x_ = new_img.shape[1]
            x_scale = targetSize / x_
            y_scale = targetSize / y_
            new_bb = []
            for box in bb1:
                new_bb.append(rotate_box(img, box, angle))
            for n in range(len(new_bb)):
                for j in range(len(new_bb[n])):
                    new_bb[n][j] = np.multiply(new_bb[n][j], [x_scale, y_scale])
                    new_bb[n][j] = np.asarray(new_bb[n][j], dtype='int64')

            with open('rotated_labels/{}_{}_rotated.gt'.format(i[:i.find('.')], str(angle)), 'w', encoding='utf8') as f:
        # fix
                for box, text in zip(new_bb, texts):
                    f.write(
                    '{},{},{},{},{},{},{},{},{}'.format(str(box[0][0]), str(box[0][1]),
                                        str(box[1][0]), str(box[1][1]),
                                        str(box[2][0]), str(box[2][1]),
                                        str(box[3][0]), str(box[3][1]),
                                        text))
            with open('rotated_labels/{}_{}_rotated.jpg.txt'.format(i[:i.find('.')], str(angle)), 'w', encoding='utf8') as f:
            # fix
                for box, text in zip(new_bb, texts):
                    f.write(
                    '{},{},{},{},{},{},{},{},{}'.format(str(box[0][0]), str(box[0][1]),
                                                        str(box[1][0]), str(box[1][1]),
                                                        str(box[2][0]), str(box[2][1]),
                                                        str(box[3][0]), str(box[3][1]),
                                                        text))
            new_img = cv2.resize(new_img, (640,640))
            cv2.imwrite('rotated_images/{}_{}_rotated.jpg'.format(i[:i.find('.')], str(angle)), new_img)


if __name__ =='__main__':
    main()
