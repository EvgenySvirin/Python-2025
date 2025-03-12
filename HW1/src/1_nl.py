from sys import stdin, argv
from typing import TextIO

def nl(input_stream: TextIO):
    for i, line in enumerate(input_stream, 1):
        striped_line = line.rstrip('\n')
        print(f"{i:6}\t{striped_line}")

if __name__ == "__main__":
    args = argv[1:]
    args_len = len(args)

    input_stream = None

    if args_len == 0:
        input_stream = stdin
    elif args_len == 1:
        input_stream = open(args[0])
    elif 1 < args_len:
        print("Too many arguments")

    if input_stream is not None:
        nl(input_stream)
