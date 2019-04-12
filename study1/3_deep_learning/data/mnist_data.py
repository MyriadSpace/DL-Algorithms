'''
Created on 2018. 6. 15.

@author: eric.hong@aidentify.io
'''

import numpy as np
import gzip
import struct

# data 읽기
def _read_data(label_path, image_path):
    with gzip.open(label_path) as flbl:
        _, _ = struct.unpack(">II", flbl.read(8))
        label = np.fromstring(flbl.read(), dtype=np.int8)

    with gzip.open(image_path, 'rb') as fimg:
        _, _, rows, cols = struct.unpack(">IIII", fimg.read(16))
        image = np.fromstring(fimg.read(), dtype=np.uint8).reshape(len(label), rows, cols)

    return (label, image)

# 튜플 형태로 반환
def get_data(path, type_val):
    if type_val == 'test':
        test_label_path = path + 't10k-labels-idx1-ubyte.gz'
        test_image_path = path + 't10k-images-idx3-ubyte.gz'
        return _read_data(test_label_path, test_image_path)

    else:
        train_label_path = path + 'train-labels-idx1-ubyte.gz'
        train_image_path = path + 'train-images-idx3-ubyte.gz'
        return _read_data(train_label_path, train_image_path)
