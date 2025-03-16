#print("hello")
#python <file_name>

#import sys
#print(sys.argv)

#name = sys.argv[1]

#print("hello " + name)

import argparse

parser = argparse.ArgumentParser(
    description='This program prints name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red' , 'Yellow'}, help='the color to search for')

args = parser.parse_args()
print(args.color)