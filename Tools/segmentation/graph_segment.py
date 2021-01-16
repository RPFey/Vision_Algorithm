import numpy as np
import cv2
import argparse

arg = argparse.ArgumentParser()
arg.add_argument('--help', action = True, help="print help information")
arg.add_argument('--image', type = str, default = None)
opt = arg.parse_args()

def main():
    pass


def print_help():
    help_message = r'\
    This program is used to tune the parameter of graph segmentation method. \n'

    print(help_message)

if __name__ == '__main__':
    if(opt.help):
        print_help()
    else:
        main()