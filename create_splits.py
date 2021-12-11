import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    train_size = 0.8
    val_size = 0.1
    test_size = 0.1
    
    ## Checking '/' at the end of directory name because it causes getting directory name only
    arg_last = data_dir[-1]
    if(arg_last != '/'):
        data_dir = data_dir+'/'        
    paths = glob.glob(data_dir+'*')
    
    random.shuffle(paths)
    len_all = len(paths)
    len_train = int(len_all * train_size)
    len_val = int(len_all * val_size)
    len_test = int(len_all * test_size)
    
    i = 0
    for f in paths:
        i += 1
        print(f)
        if(i <= len_train):
            print('train'+str(i))
            os.rename(f,'/home/workspace/data/waymo/train/'+os.path.basename(f))
        elif(i > len_train and i <= (len_train + len_val)):
            print('val'+str(i))
            os.rename(f,'/home/workspace/data/waymo/val/'+os.path.basename(f))
        elif(i > (len_train + len_val) and i <= len_all):
            print('test'+str(i))
            os.rename(f,'/home/workspace/data/waymo/test/'+os.path.basename(f))

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)