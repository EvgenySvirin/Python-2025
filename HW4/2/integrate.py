from concurrent.futures import Executor


def integrate_task(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, executor: Executor, n_jobs=1, n_iter=10000000):
    futures = []

    step = (b - a) / n_jobs
    for i in range(n_jobs):
        segment_start = a + i * step
        segment_end = a + (i + 1) * step
        iterations = n_iter // n_jobs
        futures.append(executor.submit(integrate_task, f, segment_start, segment_end, iterations))

    return sum([future.result() for future in futures])
