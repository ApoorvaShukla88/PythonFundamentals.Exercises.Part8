'''
Create a program called tree.py

Given a file path (absolute or relative), the program should write to a file all of the contents
of the directory and the child directories bellow it. The output file should look something like this:

./file1.py
./file2.py
./dir1/file1_in_dir1.txt
./dir1/file2_in_dir1.txt
./dir3/file1_in_dir3.txt
'''
import os


def tree(root):


    for root, dirs, files in os.walk(root):
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))

tree('/Users/amishra/DEV')



