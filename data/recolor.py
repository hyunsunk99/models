import os, os.path
from PIL import Image

if __name__ == '__main__':

    # folders to split
    folders = ['test', 'train', 'validation']

    for folder in folders:

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        counter = 0
        for filename in os.listdir('./{folder}/with_mask'.format(folder=folder)):
            if filename != '.DS_Store':
                orig_file = os.path.join(THIS_FOLDER, '{folder}/with_mask/{filename}'.format(folder=folder, filename=filename))
                im = Image.open(orig_file)
                rgb_im = im.convert('RGB')
                rgb_im.save(orig_file)

        counter = 0
        for filename in os.listdir('./{folder}/without_mask'.format(folder=folder)):
            if filename != '.DS_Store':
                orig_file = os.path.join(THIS_FOLDER, '{folder}/without_mask/{filename}'.format(folder=folder, filename=filename))
                im = Image.open(orig_file)
                rgb_im = im.convert('RGB')
                rgb_im.save(orig_file)

