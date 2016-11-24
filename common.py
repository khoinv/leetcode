import time

def time_cal(func):
    """
    caculate running time of function
    """
    def wrapper(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print "running time of {0}: {1}s".format(func.__name__, time.time() - start_time)
        return result

    return wrapper
