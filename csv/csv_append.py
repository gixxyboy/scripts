#!/usr/bin/python

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Append column to CSV.')
    parser.add_argument("-f", "--file", help="Input File", required=True)
    parser.add_argument("-o", "--out", help="Output File", required=True)
    parser.add_argument("-c", "--column", help="Column name")
    parser.add_argument("-d", "--data", help="Data", required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    i = 0

    with open(args.out, 'w') as out_file:
        with open(args.file, 'r') as in_file:
            for line in in_file:
                if i == 0 and args.column is not None and line != "":
                    out_file.write(line.rstrip("\n") + "," + args.column + "\n")
                else:
                    out_file.write(line.rstrip("\n") + "," + args.data + "\n")
                i = i + 1

if __name__ == '__main__':
    main()
