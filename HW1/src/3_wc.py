import re
import sys
from typing import TextIO, BinaryIO
from sys import stdin

def wc(input_stream: TextIO) -> (int, int, int):
    lines_num, words_num, bytes_num = 0, 0, 0
    for line in input_stream:
        lines_num += 1 if line[-1] == '\n' else 0
        words_num += len(re.findall(r'\w+', line))
        bytes_num += len(line)

    return lines_num, words_num, bytes_num

if __name__ == "__main__":
    args = sys.argv[1:]
    args_size = len(args)
    if args_size == 0:
        print(*wc(stdin))
    elif args_size == 1:
        print(*wc(open(args[0])), args[0])
    else:
        total_lines_num, total_words_num, total_bytes_num = 0, 0, 0
        for filename in args:
            lines_num, words_num, bytes_num = wc(open(filename))
            total_lines_num += lines_num
            total_words_num += words_num
            total_bytes_num += bytes_num
            print(lines_num, words_num, bytes_num, filename)
        print(total_lines_num, total_words_num, total_bytes_num, "total")
