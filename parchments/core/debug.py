import time


def execution_time(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))

    return timed