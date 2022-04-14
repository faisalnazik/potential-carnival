
import time


def clock(func):
    """simple decorator to show the running time of functions"""
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))


# Output

'''
$ python clockdeco.py
**************************************** Calling snooze(.123)
[0.12923090s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00000110s] factorial(1) -> 1
[0.00028910s] factorial(2) -> 2
[0.00068260s] factorial(3) -> 6
[0.00106760s] factorial(4) -> 24
[0.00145990s] factorial(5) -> 120
[0.00185240s] factorial(6) -> 720
6! = 720

'''
