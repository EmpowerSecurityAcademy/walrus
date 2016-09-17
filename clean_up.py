import os
import glob

files = glob.glob('./tmp/*')
for f in files:
    os.remove(f)