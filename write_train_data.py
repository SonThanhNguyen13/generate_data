import os

path = 'my_data/train_images'


def main():
    with open('train_list.txt', 'w') as f:
        for i in os.listdir(path):
            f.write(i + '\n')

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    print(file_len('train_list.txt'))

if __name__ =='__main__':
    main()