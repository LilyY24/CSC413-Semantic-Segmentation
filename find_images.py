import os
from PIL import Image
from IPython.display import display

def main():
    root_path = 'data/VOCtrainval_11-May-2012/VOCdevkit/VOC2012'
    image_dir = os.path.join(root_path, 'JPEGImages')
    train_dir = os.path.join(root_path, 'SegmentationClass')
    new_image_dir = os.path.join(root_path, 'newpjeg')
    os.mkdir(new_image_dir)
    train_files = os.listdir(train_dir)
    train_list = [f.strip('.png') for f in train_files]
    image_files = sorted([image_dir + "/" + f + ".jpg" for f in train_list])
    for image in image_files:
        image_file = os.path.basename(image).split('.')[0]
        save_to = os.path.join(new_image_dir, image_file+'.jpg')
        image = Image.open(image)
        image.save(save_to)



if __name__ == '__main__':
    main()

