import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the duration
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        return result  # Return the original function's result
    return wrapper
