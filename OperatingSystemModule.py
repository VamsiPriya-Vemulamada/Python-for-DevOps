#Operating System is the main job in the devOps engineer where we configure the systems or any other machines. So, for handling the file system with irrespective of the type of Operating system. we can get many chances.
#So, we will use the modules that are in the python which is os module in python

# what is the module and how it works:  https://www.geeksforgeeks.org/python-modules/
# When ever we are using the module we will use the call all the functions, attributes or the classes which with .

import os
import os.path
import  shutil

# Now creating a Directory in os
# os.mkdir("myfolder")
# Creating a file in directory
# file = open('trail.txt', 'w')
# file.write("hey I've entered and typing in the file")
# Listing all the files and directories
info = os.listdir()
print(info)

# For the paths we also have other module of os which is os.path

# For checking the file exists or not which is nothing but we are checking the path of the file or folder

test1 = os.path.exists('trail.txt')
test2 = os.path.exists('myfolder')
print(test1, test2)

# For deleting files and directories
os.remove('trail.txt')
os.rmdir('myfolder')

# For recursively deletion of files below are the files that are deleted

shutil.rmtree('myfolder')
