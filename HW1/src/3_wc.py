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

def wc_only_one_file(filename: str) -> None:
    with open(filename) as file:
        new_lines_num, words_num, bytes_num = wc(file)
    print(new_lines_num, words_num, bytes_num, filename)


def wc_files(filenames: list[str]) -> None:
    total_lines_num, total_words_num, total_bytes_num = 0, 0, 0
    for filename in filenames:
        with open(filename) as file:
            lines_num, words_num, bytes_num = wc(file)
        print(lines_num, words_num, bytes_num, file.name)
        total_lines_num += lines_num
        total_words_num += words_num
        total_bytes_num += bytes_num
    print(total_lines_num, total_words_num, total_bytes_num, "total")

if __name__ == "__main__":
    args = sys.argv[1:]
    args_size = len(args)
    if args_size == 0:
        print(*wc(stdin))
    elif args_size == 1:
        print(*wc(open(args[0])), args[0])
    else:
        total_new_lines_num, total_words_num, total_bytes_num = 0, 0, 0
        for filename in args:
            lines_num, words_num, bytes_num = wc(open(filename))
            total_new_lines_num += lines_num
            total_words_num += words_num
            total_bytes_num += bytes_num
            print(lines_num, words_num, bytes_num, filename)
        print(total_new_lines_num, total_words_num, total_bytes_num, "total")
