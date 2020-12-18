import os

path = 'my_data/test_images'


def main():
    with open('test_list.txt', 'w') as f:
        for i in os.listdir(path):
            f.write(i + '\n')


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1


if __name__ =='__main__':
    main()
    print(file_len('train_list.txt'))