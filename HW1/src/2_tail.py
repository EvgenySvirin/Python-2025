from sys import stdin, argv
from collections import deque
from typing import TextIO

def tail(input_stream: TextIO, tail_size:int=10, last_line_end:str=""):
    deq = deque([])
    for line in input_stream:
        deq.append(line.rstrip('\n'))
        if tail_size < len(deq):
            deq.popleft()
    # у меня tail последнюю строчку принтит без \n
    # так что решил так же сделать
    last = deq.pop()
    for line in deq:
        print(line)
    if last is not None:
        print(last, end=last_line_end)

if __name__ == "__main__":
    args = argv[1:]
    args_size = len(args)
    if len(args) == 0:
        tail(input_stream=stdin, tail_size=17)
    elif len(args) == 1:
        tail(input_stream=open(args[0]), tail_size=10)
    else:
        for filename in args[:-1]:
            print(f"===> {filename} <===")
            tail(input_stream=open(filename), tail_size=10, last_line_end="\n")
        print(f"===> {args[-1]} <===")
        tail(input_stream=open(args[-1]), tail_size=10, last_line_end="")
