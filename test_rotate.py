import os
import cv2
import numpy as np

path = 'rotated_labels'


def main():
    for i in os.listdir(path):
        label = os.path.join(path, i)
        img = os.path.join('rotated_images', i[:i.find('.')]  + '.jpg')
        image = cv2.imread(img)
        with open(label, 'r', encoding='utf8') as f:
            for line in f.readlines():
                x1, y1, x2, y2,x3, y3, x4, y4, text = line.split(",")
                x1, y1, x2, y2, x3, y3, x4, y4 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4)
                points = np.array([[x1,y1], [x2, y2], [x3,y3], [x4, y4]])
                cv2.polylines(image,np.int32([points]),True, (0,0,255),2)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        #cv2.imwrite('result/{}.jpg'.format(i[:i.find('.')]), image)


if __name__ =='__main__':
    main()

