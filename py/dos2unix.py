#!/usr/bin/python3

# dos2unix 将Windows下的CRLF更换为LF

import os
import sys

def dos2unix(filename):
    temp_path = filename + ".temp" # 临时文件
    with open(filename, 'rb') as infile, open(temp_path, 'wb') as outfile:
        for line in infile:
            if line[-2:] == b'\r\n':
                line = line[:-2] + b'\n'
            outfile.write(line)
    os.remove(filename)
    os.rename(temp_path, filename)


def main():
    '''
    Usage:
        python dos2uinx.py a.txt b.txt c.txt
    '''
    args = sys.argv[1:]
    if args[0] == 'dos2unix.py':
        args = args[1:]
    for filename in args:
        dos2unix(filename)

if __name__ == "__main__":
    main()