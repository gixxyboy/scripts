#!/usr/bin/python

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Delete column from CSV.')
    parser.add_argument("-f", "--file", help="Input File", required=True)
    parser.add_argument("-o", "--out", help="Output File", required=True)
    parser.add_argument("-c", "--column", help="Column number", required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    i = 0
    col_nbr = int(args.column)

    with open(args.out, 'w') as out_file:
        with open(args.file, 'r') as in_file:
            for line in in_file:
                columns = line.rstrip("\n").split(",")
                if col_nbr < len(columns) and col_nbr >= 0:
                    del columns[col_nbr]
                    out_file.write(",".join(columns) + "\n")
                else:
                    print("Error: Line", i, "has less than", col_nbr, "columns")
                i = i + 1


if __name__ == '__main__':
    main()
