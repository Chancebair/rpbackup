__author__ = 'Chance Bair'
import fnmatch
import os
import os.path
import re
import shutil
import Tkinter
import sys


# class backup(Tkinter.Tk):
#     def __init__(self, parent):
#         Tkinter.Tk.__init__(self, parent)
#         self.parent = parent
#         self.initialize()
#
#     def initialize(self):
#         self.grid()
#
#         self.entry = Tkinter.Entry(self)
#         self.entry.grid(column=0, row=0, sticky='EW')
#
#         button = Tkinter.Button(self,text=u"...")
#         button.grid(column=1, row=0)
#
#         self.grid_columnconfigure(0, weight=1)
#         self.resizable(True, False)
#
#
#
# if __name__ == "__main__":
#     app = backup(None)
#     app.title('Reaper Backup')
#     app.mainloop()




includes = ['*.reapeaks', '*.rpp', '*.jcp']  # for Reaper files only
file_object = open('config.txt', 'r+')
read = file_object.read()
path = [read]
file_object.close


# Determines Reaper folder
print "Current folder to backup Reaper files from : ", read
resp = raw_input('Is this the correct path? (y/n) : ')

if resp == 'n':
    file_object = open('config.txt', 'w')
    path[0] = raw_input('What is the absolute pathname of the Reaper project folder? : ')
    file_object.write(path[0])
    file_object.close

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
