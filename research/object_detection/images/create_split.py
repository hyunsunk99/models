import os, os.path

if __name__ == '__main__':

    # folders to split
    folders = ['with_mask', 'without_mask']

    for label in folders:

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        # find number of pics in the folder
        filenames = os.listdir('./{}'.format(label))
        num_pics = len(filenames)

        # split into number of training, validation, and testing pics
        train_num = int(num_pics * 0.85)
        valid_num = int(num_pics * .1)
        test_num = num_pics - train_num - valid_num

        # move correct number of images to correct folders
        for i in range(train_num):
            filename = filenames[i]
            orig_file = os.path.join(THIS_FOLDER, '{label}/{filename}'.format(label=label, filename=filename))
            new_file = os.path.join(THIS_FOLDER, 'train/{label}/{filename}'.format(label=label, filename=filename))
            os.rename(orig_file, new_file)

        for i in range(train_num, train_num + valid_num):
            filename = filenames[i]
            orig_file = os.path.join(THIS_FOLDER, '{label}/{filename}'.format(label=label, filename=filename))
            new_file = os.path.join(THIS_FOLDER, 'validation/{label}/{filename}'.format(label=label, filename=filename))
            os.rename(orig_file, new_file)

        for i in range(train_num + valid_num, train_num + valid_num + test_num):
            filename = filenames[i]
            orig_file = os.path.join(THIS_FOLDER, '{label}/{filename}'.format(label=label, filename=filename))
            new_file = os.path.join(THIS_FOLDER, 'test/{label}/{filename}'.format(label=label, filename=filename))
            os.rename(orig_file, new_file)