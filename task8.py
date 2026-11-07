# Task 08 - Cache with Expiry
import time
import functools

def ttl_cache(seconds):
    def decorator(func):
        saved = {}
        stats = {"hits": 0, "misses": 0}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # sorted() -> x=2,y=3 and y=3,x=2 give the same key
            # (unhashable inputs like lists will raise TypeError)
            key = (args, tuple(sorted(kwargs.items())))
            now = time.monotonic()
            if key in saved and now - saved[key][1] < seconds:
                stats["hits"] += 1
                return saved[key][0]
            stats["misses"] += 1
            saved[key] = (func(*args, **kwargs), now)
            return saved[key][0]

        wrapper.stats = stats
        return wrapper
    return decorator

@ttl_cache(2)
def add(x, y):
    return x + y

print(add(x=2, y=3))
print(add(y=3, x=2))
print(add.stats)          # {'hits': 1, 'misses': 1}
