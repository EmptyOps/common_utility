import os
from subprocess import call
import argparse

ABS_PATh = os.path.dirname(os.path.abspath(__file__)) + "/"

parser = argparse.ArgumentParser(description='a crop utility')

parser.add_argument('--dir_to_process', type=str, nargs='?',
                    help='dir_to_process')

FLAGS = parser.parse_args()


if FLAGS.dir_to_process == "":
    paths = []  #specify static here
else:
    paths = [ABS_PATh+ FLAGS.dir_to_process+"/" ]

def resize( path ):
    items = os.listdir( path )

    for filename in items:

        if (filename.endswith('.rar')): #or .avi, .mpeg, whatever. 
           
            call(["unrar", "x",path+filename,"./__out"]) 

for path in paths:
    resize( path )
