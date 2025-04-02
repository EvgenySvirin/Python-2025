import multiprocessing
import threading

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def fib_multithreading(n, number_threads):
    threads = []
    for _ in range(number_threads):
        thread = threading.Thread(target=fib, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def fib_multiprocessing(n, number_processes):
    processes = []
    for _ in range(number_processes):
        process = multiprocessing.Process(target=fib, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
