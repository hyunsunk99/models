import os, os.path

if __name__ == '__main__':

    # folders to split
    folders = ['test', 'train', 'validation']

    for folder in folders:

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

        counter = 0
        for filename in os.listdir('./{folder}/with_mask'.format(folder=folder)):
            new_file_name = '{folder}_w_{count}.jpg'.format(folder=folder, count=counter)
            orig_file = os.path.join(THIS_FOLDER, '{folder}/with_mask/{filename}'.format(folder=folder, filename=filename))
            new_file = os.path.join(THIS_FOLDER, '{folder}/with_mask/{new_file_name}'.format(folder=folder, new_file_name=new_file_name))
            os.rename(orig_file, new_file)
            counter += 1

        counter = 0
        for filename in os.listdir('./{folder}/without_mask'.format(folder=folder)):
            new_file_name = '{folder}_wo_{count}.jpg'.format(folder=folder, count=counter)
            orig_file = os.path.join(THIS_FOLDER, '{folder}/without_mask/{filename}'.format(folder=folder, filename=filename))
            new_file = os.path.join(THIS_FOLDER, '{folder}/without_mask/{new_file_name}'.format(folder=folder, new_file_name=new_file_name))
            os.rename(orig_file, new_file)
            counter += 1

