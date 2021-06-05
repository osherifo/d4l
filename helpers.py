import time 
import configs

# helper to measure time taken by function
def measure_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        total_time=t2-t1
        print(f'{func.__name__} took {total_time} seconds')
        return result
    return wrapper

def measure_insertions(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        total_time=t2-t1
        insertions_per_second=configs.token_count // total_time
        print(f'{func.__name__} did {insertions_per_second} insertions per seconds')
        return result
    return wrapper

def log_analytics(file, chunk_size, time, inserts_per_second):
    with open(file, 'a') as f:
        f.write(f'{chunk_size},{time},{inserts_per_second}\n')
