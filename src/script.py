import os
import re
import glob
from pprint import pprint


data_dir = '../data'

files = glob.glob(os.path.join(data_dir, '*/*.htm*'))

for f in files:
    with open(f, 'r') as fh:
        data = fh.readlines()
        data = ''.join(data)
        clean_data = re.sub()
