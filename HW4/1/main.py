from bench import *
import timeit

if __name__ == "__main__":
    n = 30
    number = 10

    time_synchronous = timeit.timeit((lambda: fib(n=n)), number=number)
    time_multithreading = timeit.timeit(lambda: fib_multithreading(n=n, number_threads=number), number=1)
    time_multiprocessing = timeit.timeit(lambda: fib_multiprocessing(n=n, number_processes=number), number=1)

    bench_result = (
        f"n equals {n} \n"
        f"Synchronous bench, {number} times: {time_synchronous:.6f} sec\n"
        f"Multithreading bench, {number} threads: {time_multithreading:.6f} sec\n"
        f"Multiprocessing bench, {number} processes : {time_multiprocessing:.6f} sec"
    )

    with open("../artifacts/1/bench.txt", "w") as file:
        file.write(bench_result)