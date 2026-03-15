import functools


def monitor(func):
    """Logs processing start and completion."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n[LOG] Processing Started")
        result = func(*args, **kwargs)
        print("[LOG] Processing Completed")
        return result
    return wrapper

def play_count_stream(limit):
    """
    Yields squared even numbers up to the limit.
    Formula: If number is even, yield number * number.
    """
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2