#!/usr/bin/env python3

import os
import sys

def split_fasta(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} is not a valid file.")
        return

    with open(input_file, 'r') as infile:
        sequence = ""
        header = ""
        for line in infile:
            if line.startswith(">"):
                if header and sequence:
                    write_fasta(header, sequence)
                header = line.strip()
                sequence = ""
            else:
                sequence += line.strip()

        if header and sequence:
            write_fasta(header, sequence)

def write_fasta(header, sequence):
    filename = header[1:].replace(" ", "_") + ".fasta"
    with open(filename, 'w') as outfile:
        outfile.write(f"{header}\n")
        outfile.write(f"{sequence}\n")
    print(f"Written {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: split_fasta.py <input_fasta>")
        sys.exit(1)

    input_file = sys.argv[1]
    split_fasta(input_file)

if __name__ == "__main__":
    main()
