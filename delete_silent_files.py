### Deletes any audio files that are completely silent. 
### python delete_silent_files.py <top_dir_of_stems>

import numpy as np
import os
import shutil
import soundfile as sf
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    'top_dir', help='Directory structure to be copied', type=str)

args = parser.parse_args()

BASE_DIR = args.top_dir

if BASE_DIR[-1] != '/':
    BASE_DIR += '/'


def copy_dirs(dir_or_file):

    if (os.path.isdir(dir_or_file)):
        subs = os.listdir(dir_or_file)
        if subs != []:
            for s in subs:
                copy_dirs(os.path.join(dir_or_file, s))

    if (os.path.isfile(dir_or_file)):
        if any(ext in (dir_or_file ).lower() for ext in ['.flac', '.mp3', '.wav', '.aiff','.aif']):
            x, fs = sf.read(dir_or_file)
            if np.array_equal(x, np.zeros(x.shape)):
                print(dir_or_file)
                os.remove(dir_or_file)


copy_dirs(BASE_DIR)
