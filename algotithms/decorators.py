import time


def timeit(func):
    """
    Decorator for measuring running time for function 'func'.
    """

    def measure_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print("Processing time of %s(): %.5f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time