__author__ = 'Chance Bair'
import fnmatch
import os
import os.path
import re
import shutil

includes = ['*.reapeaks', '*.rpp', '*.jcp']# for Reaper files only
path = ['/Users/chance.bair/Desktop/']

print "Current folder being backed up:\n", path[0]
resp = raw_input('Correct? (y/n): ')
if resp == 'n':
    path[0] = raw_input('What is the absolute pathname of the folder? : ')


# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
path_reg = r'|'.join([fnmatch.translate(x) for x in path]) or r'$.'

for root, dirs, files in os.walk(path[0]):

    # exclude dirs
    dirs[:] = [os.path.join(root, d) for d in dirs]
    dirs[:] = [d for d in dirs if not re.match(path_reg, d)]

    # exclude/include files
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if not re.match(path_reg, f)]
    files = [f for f in files if re.match(includes, f)]

    for fname in files:
        shutil.copy(fname, '/Users/chance.bair/Dropbox/Ambits/Reaper Backups/')

    # If reaper files, print out filename
#    if '.reapeaks' or '.rp' or '.jcp' in filenames:
#            for filename in filenames:
#                print os.path.join(filename)