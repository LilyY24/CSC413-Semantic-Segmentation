import os
from glob import glob

root = os.path.join(os.getcwd(), 'data/VOCtrainval_11-May-2012/VOCdevkit/VOC2012')
our_file_path = os.path.join(root, "ImageSets/Segmentation", "person" + ".txt")
image_file_path = os.path.join(root, "ImageSets/Segmentation", "all" + ".txt")
output_file_path = os.path.join(root, "ImageSets/Segmentation", "final_person.txt")

def check_images(set, image_set):
    set = open(set, "r")
    image_set = open(image_set, 'r')
    set_files = set.readlines()

    our_files = []
    their_files = []
    for file in set_files:
        file = file.rstrip()
        our_files.append(file)
    image_files = image_set.readlines()
    for file in image_files:
        file = file.rstrip()
        their_files.append(file)

    collector = []
    for filename in our_files:
        if filename in their_files:
            collector.append(filename)
    print(len(collector))
    new = open(output_file_path, "w+")
    new.write('\n'.join(collector))
    new.close()
    set.close()
    image_set.close()


if __name__ == "__main__":
    check_images(our_file_path, image_file_path)
